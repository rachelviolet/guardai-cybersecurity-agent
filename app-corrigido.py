import sqlite3
import time
from collections import OrderedDict
import bcrypt  # Requer: pip install bcrypt

# ---------------------------------------------------------------------------
# Configurações de Segurança e Rate Limiting
# ---------------------------------------------------------------------------
MAX_TENTATIVAS_IP = 10         # Bloqueia atacante que testa múltiplos usuários pelo mesmo IP
MAX_TENTATIVAS_CONTA = 5       # Limite de falhas por usuário
BLOQUEIO_IP_SEGUNDOS = 600     # 10 minutos de ban para o IP suspeito
BLOQUEIO_CONTA_SEGUNDOS = 180  # 3 minutos de atraso para o usuário específico
MAX_REGISTROS_MEMORIA = 10_000 # [Mitigação DoS de Memória]: Limite estrito de chaves em RAM

# Hash dummy pré-computado para mitigar User Enumeration / Timing Attacks
DUMMY_HASH = bcrypt.hashpw(b"senha_invalida_para_timing_defense", bcrypt.gensalt(rounds=12))


class LimitedMemoryRateLimiter:
    """
    Gerenciador de tentativas de login em memória baseado em OrderedDict (LRU Cache).
    Mitiga Memory Exhaustion DoS limitando o tamanho máximo de entradas e expurgando
    registros antigos automaticamente sem dependências externas.
    """
    def __init__(self, max_entries: int = MAX_REGISTROS_MEMORIA):
        self.max_entries = max_entries
        self.records = OrderedDict()

    def get(self, key: str) -> dict:
        agora = time.time()
        if key in self.records:
            # Move para o final para marcar como recentemente acessado
            self.records.move_to_end(key)
            data = self.records[key]
            # Se já expirou o bloqueio e a janela de retenção, reseta os contadores
            if agora > data.get("bloqueado_ate", 0) and agora - data.get("ultimo_acesso", 0) > 3600:
                data["falhas"] = 0
            return data
        
        # Cria novo registro expurgando o mais antigo se atingir a capacidade máxima
        if len(self.records) >= self.max_entries:
            self.records.popitem(last=False)  # Remove o item mais antigo (FIFO/LRU)

        novo_registro = {"falhas": 0, "bloqueado_ate": 0, "ultimo_acesso": agora}
        self.records[key] = novo_registro
        return novo_registro

    def reset(self, key: str):
        if key in self.records:
            del self.records[key]


# Instâncias de rate limiting para IP e Usuário
limiter_ip = LimitedMemoryRateLimiter()
limiter_usuario = LimitedMemoryRateLimiter()


def fazer_login(usuario: str, senha: str, ip_origem: str = "127.0.0.1") -> str:
    """
    Autenticação com Defesa em Profundidade contra:
    1. SQL Injection (Prepared Statements).
    2. Armazenamento inseguro de senhas (bcrypt com salt individual e custo 12).
    3. User Enumeration / Timing Attacks (DUMMY_HASH para tempo constante de resposta).
    4. Memory Exhaustion DoS (OrderedDict LRU Cache com limite fixo de chaves).
    5. Account Denial of Service (Duplo Rate Limiting: IP e Usuário com penalidades distintas).
    """
    agora = time.time()
    usuario_normalizado = usuario.strip().lower()

    registro_ip = limiter_ip.get(f"ip:{ip_origem}")
    registro_usuario = limiter_usuario.get(f"usr:{usuario_normalizado}")

    # 1. Verifica bloqueio do IP (impede força bruta e ataque distribuído de DoS na conta)
    if agora < registro_ip["bloqueado_ate"]:
        espera = int(registro_ip["bloqueado_ate"] - agora)
        return f"Acesso Negado. Muitas tentativas a partir deste IP. Bloqueado por mais {espera} segundos."

    # 2. Verifica bloqueio temporário por usuário
    if agora < registro_usuario["bloqueado_ate"]:
        espera = int(registro_usuario["bloqueado_ate"] - agora)
        return f"Acesso Negado. Conta temporariamente suspensa para novas tentativas. Aguarde {espera} segundos."

    senha_bytes = senha.encode("utf-8")
    usuario_encontrado = False
    stored_hash = DUMMY_HASH

    # 3. Consulta ao banco com Prepared Statements (Mitiga SQL Injection)
    with sqlite3.connect("banco_de_dados.db") as conexao:
        cursor = conexao.cursor()
        query = "SELECT password_hash FROM usuarios WHERE username = ?"
        cursor.execute(query, (usuario_normalizado,))
        resultado = cursor.fetchone()

        if resultado:
            usuario_encontrado = True
            stored_hash = resultado[0].encode("utf-8")

    # 4. Verificação de senha com bcrypt (Sempre executada para evitar Timing Attack)
    senha_valida = bcrypt.checkpw(senha_bytes, stored_hash)

    # 5. Sucesso na autenticação
    if usuario_encontrado and senha_valida:
        # Reseta os limites de falhas do usuário e do IP
        limiter_usuario.reset(f"usr:{usuario_normalizado}")
        limiter_ip.reset(f"ip:{ip_origem}")
        return "Acesso Permitido!"

    # 6. Tratamento de Falha: Atualiza contadores de IP e Usuário
    registro_ip["falhas"] += 1
    registro_ip["ultimo_acesso"] = agora

    registro_usuario["falhas"] += 1
    registro_usuario["ultimo_acesso"] = agora

    # Bloqueio do IP agressor
    if registro_ip["falhas"] >= MAX_TENTATIVAS_IP:
        registro_ip["bloqueado_ate"] = agora + BLOQUEIO_IP_SEGUNDOS
        return f"Acesso Negado. Limite de requisições excedido para este IP. Bloqueado temporariamente."

    # Bloqueio com backoff da conta
    if registro_usuario["falhas"] >= MAX_TENTATIVAS_CONTA:
        registro_usuario["bloqueado_ate"] = agora + BLOQUEIO_CONTA_SEGUNDOS
        return f"Acesso Negado. Limite de tentativas para esta conta atingido. Aguarde {BLOQUEIO_CONTA_SEGUNDOS} segundos."

    return "Acesso Negado."
