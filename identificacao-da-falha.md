# Histórico de Auditoria e Identificação de Falhas (GuardAI)

Este documento registra a evolução das auditorias de segurança realizadas no ciclo de vida da aplicação de autenticação, seguindo o padrão da skill `vulnerability-analysis`: matriz com **Impacto**, **Probabilidade**, **Severidade Geral** e recomendações de trilha de estudos.

---

# Primeira Verificação (`app.py` original)

## Matriz de Avaliação de Risco

| Métrica | Classificação | Justificativa |
| :--- | :---: | :--- |
| **Vulnerabilidade** | **SQL Injection (SQLi)**<br>([CWE-89](https://cwe.mitre.org/data/definitions/89.html) / OWASP A03:2021) | Concatenação direta de parâmetros de entrada do usuário via f-strings na query SQL. |
| **Impacto** | **Crítico** | Permite contornar autenticação sem senha, ler dados confidenciais de outros usuários ou modificar a base. |
| **Probabilidade** | **Muito Alta** | Vetor público direto no formulário de login; facilmente descoberto manualmente ou por ferramentas automatizadas (ex: sqlmap). |
| **Severidade Geral** | **Crítica** | Combinação de impacto máximo com facilidade trivial de exploração. |

## Detalhes Técnicos

- **Localização:** Linha 7 do arquivo [app.py](app.py#L7):
  ```python
  query = f"SELECT * FROM usuarios WHERE username = '{usuario}' AND password = '{senha}'"
  ```
- **Vetor de Exploração:** Inserção do payload `admin' --` no campo de usuário. A aspa fecha a string e os hífens comentam a checagem da senha, permitindo login como administrador sem credenciais.
- **Mapeamento MITRE ATT&CK®:**
  - **Tática:** [TA0001 - Initial Access](https://attack.mitre.org/tactics/TA0001/) / [TA0006 - Credential Access](https://attack.mitre.org/tactics/TA0006/)
  - **Técnica:** [T1190 - Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190/)

## Mitigação Aplicada

1. Substituição por **Prepared Statements** com placeholders (`?`) no SQLite.
2. Uso de context manager (`with`) para garantir liberação adequada de recursos de conexão.

---

# Segunda Verificação (`app-corrigido.py` v1)

Após mitigar o SQL Injection, uma nova auditoria estática revelou vulnerabilidades na camada criptográfica e temporal:

## Matrizes de Avaliação de Risco

### Falha 1: Uso de Hash Rápido sem Salt para Senhas (SHA-256)

| Métrica | Classificação | Justificativa |
| :--- | :---: | :--- |
| **Vulnerabilidade** | **Algoritmo de Hash Rápido sem Salt**<br>([CWE-328](https://cwe.mitre.org/data/definitions/328.html) / OWASP A02:2021) | Uso de SHA-256 linear para proteção de senhas em repouso. |
| **Impacto** | **Alto** | Em caso de vazamento da base, permite recuperação em massa de senhas via Rainbow Tables e ataques com GPU. |
| **Probabilidade** | **Média** | Requer acesso prévio ao dump do banco de dados para realizar a quebra offline. |
| **Severidade Geral** | **Alta** | Risco substancial à confidencialidade das credenciais de todos os usuários cadastrados. |

### Falha 2: Enumeração de Usuários por Discrepância Temporal (Timing Attack)

| Métrica | Classificação | Justificativa |
| :--- | :---: | :--- |
| **Vulnerabilidade** | **Observable Timing Discrepancy**<br>([CWE-208](https://cwe.mitre.org/data/definitions/208.html)) | Retorno imediato quando o usuário não existe vs cálculo de hash quando existe. |
| **Impacto** | **Baixo** | Permite descobrir quais nomes de usuário existem no sistema (reconhecimento). |
| **Probabilidade** | **Alta** | Atacantes podem medir latência de resposta em scripts automatizados com facilidade. |
| **Severidade Geral** | **Baixa** | Facilita ataques subsequentes direcionados, mas não compromete a senha diretamente. |

### Falha 3: Ausência de Controle de Taxa e Força Bruta

| Métrica | Classificação | Justificativa |
| :--- | :---: | :--- |
| **Vulnerabilidade** | **Falta de Rate Limiting**<br>([CWE-307](https://cwe.mitre.org/data/definitions/307.html)) | Inexistência de bloqueio ou limite de requisições de login por tempo. |
| **Impacto** | **Médio** | Tentativas ilimitadas permitem adivinhação de senhas fracas por força bruta. |
| **Probabilidade** | **Alta** | Scripts automatizados conseguem testar milhares de senhas sem penalidade. |
| **Severidade Geral** | **Média** | Ameaça direta a usuários com senhas comuns do cotidiano. |

## Mitigações Aplicadas

- Substituição do SHA-256 por **bcrypt** com salt automático e fator de trabalho 12.
- Adição de `DUMMY_HASH` para manter o tempo de processamento estritamente idêntico mesmo quando o usuário não existe.
- Criação de controle em memória de tentativas falhas com bloqueio temporário.

---

# Terceira Verificação (`app-corrigido.py` v2)

Com a adição do controle de tentativas, a análise de resiliência e DoS identificou:

## Matrizes de Avaliação de Risco

### Falha 1: Esgotamento de Memória por Requisições Fictícias (State DoS)

| Métrica | Classificação | Justificativa |
| :--- | :---: | :--- |
| **Vulnerabilidade** | **Uncontrolled Resource Consumption**<br>([CWE-400](https://cwe.mitre.org/data/definitions/400.html) / OWASP A04:2021) | Armazenamento de tentativas em `defaultdict` sem teto máximo de chaves. |
| **Impacto** | **Alto** | Esgotamento da memória RAM (Out of Memory - OOM), derrubando o servidor da aplicação. |
| **Probabilidade** | **Média** | Requer envio contínuo de milhares de usernames aleatórios para saturar a memória. |
| **Severidade Geral** | **Média** | Comprometimento da disponibilidade geral do serviço. |

### Falha 2: Negação de Serviço contra Contas Legítimas (Account DoS)

| Métrica | Classificação | Justificativa |
| :--- | :---: | :--- |
| **Vulnerabilidade** | **Over-Restricted Authentication**<br>([CWE-645](https://cwe.mitre.org/data/definitions/645.html)) | Bloqueio atrelado estritamente ao nome de usuário sem validar o IP de origem. |
| **Impacto** | **Médio** | Um invasor externo pode bloquear propositalmente o usuário legítimo (ex: admin). |
| **Probabilidade** | **Alta** | Trivial de executar: basta errar a senha da vítima 5 vezes consecutivas. |
| **Severidade Geral** | **Média** | Indisponibilidade de acesso para usuários legítimos. |

## Mitigações Aplicadas
- Implementação da classe `LimitedMemoryRateLimiter` com política **LRU Cache** (`OrderedDict`), com teto estrito de 10.000 entradas para mitigar consumo de RAM.
- **Rate limiting em duas camadas**: bloqueio agressivo do IP atacante (10 minutos) e atraso reduzido para a conta (3 minutos), impedindo que o invasor mantenha a vítima travada.

---

# Trilha de Estudos Recomendada (Conexão DIO)

Para aprofundar e consolidar as práticas de segurança defensiva abordadas nestas análises:

1. **Conceitos Essenciais:**
   - **OWASP Top 10 para Desenvolvedores:** Injeção, falhas criptográficas e desenho seguro.
   - **Criptografia Aplicada:** Diferença entre funções de hash rápido (SHA/MD5) e funções KDF para senhas (Argon2, bcrypt, PBKDF2).
   - **Defesa em Profundidade:** Validação de entradas, rate limiting em múltiplas camadas e tratamento de recursos.

2. **Formações e Bootcamps na DIO:**
   - **Formação de Cibersegurança:** Fundamentos defensivos, análise de ameaças e postura de segurança.
   - **Cursos de Desenvolvimento Seguro (AppSec):** Boas práticas para APIs Python/Node, sanitização de inputs e mitigação de brechas OWASP.
   - **Desafios de Código de Autenticação e Segurança:** Exercícios práticos para fixar o uso de Prepared Statements e gerenciamento seguro de sessões.
