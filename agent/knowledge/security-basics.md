# Fundamentos de Segurança da Informação (Security Basics)

Contexto e diretrizes fundamentais de cibersegurança e segurança em aplicações (AppSec) para o agente orientar estudantes de forma segura, ética e didática.

## 1. Princípios Fundamentais

O agente deve basear todas as suas orientações de segurança em três pilares:

- **Tríade CIA (Confidencialidade, Integridade e Disponibilidade):**
  - *Confidencialidade:* Apenas pessoas autorizadas devem acessar os dados (ex.: uso de criptografia, controle de acesso).
  - *Integridade:* Os dados devem ser confiáveis e não alterados indevidamente (ex.: hashing, validações).
  - *Disponibilidade:* O serviço e os dados devem estar acessíveis quando necessários (ex.: proteção contra DoS, redundância).
- **Menor Privilégio (Least Privilege):** Cada processo, usuário ou componente deve ter apenas o nível de acesso estritamente necessário para sua função.
- **Defesa em Profundidade:** Segurança não depende de uma barreira única; ela deve ser implementada em várias camadas (rede, aplicação, banco de dados, infraestrutura).

## 2. Shift-Left Security (Segurança Desde o Início)

Segurança não é uma etapa final antes de publicar o código; deve começar no desenvolvimento:
- Educar o estudante a validar e sanitizar **toda e qualquer entrada de dados** externa (nunca confie no input do usuário).
- Tratar dados sensíveis (senhas, tokens, chaves de API) com variáveis de ambiente e gerenciadores de segredos, nunca direto no código (*hardcoded*).
- Manter dependências e bibliotecas sempre atualizadas para evitar vulnerabilidades conhecidas.

## 3. Principais Vulnerabilidades em Código (OWASP Top 10)

O agente deve reconhecer e explicar com clareza os riscos mais comuns encontrados em projetos de estudantes:

1. **Injeção (SQL Injection, Command Injection):**
   - *Risco:* Comandos maliciosos executados no banco ou sistema operacional.
   - *Correção padrão:* Uso de consultas parametrizadas (Prepared Statements) ou ORMs seguros.
2. **Exposição de Dados Sensíveis e Segredos Expostos:**
   - *Risco:* Chaves de API, senhas ou tokens comitados no GitHub público.
   - *Correção padrão:* `.gitignore`, variáveis de ambiente (`.env`) e rotação de credenciais comprometidas.
3. **Quebra de Autenticação e Controle de Acesso:**
   - *Risco:* Um usuário acessar recursos de outros ou burlar a verificação de login.
   - *Correção padrão:* Validação de permissões no backend (não apenas no frontend), senhas com hash forte (ex.: bcrypt/argon2) e tokens seguros.
4. **Cross-Site Scripting (XSS):**
   - *Risco:* Injeção de scripts maliciosos executados no navegador de outros usuários.
   - *Correção padrão:* Escape/codificação de saídas HTML e validação rigorosa no frontend e backend.

## 4. Postura Ética do Agente (Foco Defensivo)

- **Apenas Segurança Defensiva:** O agente ensina a auditar, proteger e corrigir. Nunca gera códigos de exploração (*exploits* ou *payloads* funcionais) que possam ser usados para ataques.
- **Abordagem Construtiva:** Se o código do estudante contiver falhas graves, aponte com gentileza, explique o risco prático e mostre como consertar.
- **Mentalidade de Aprendizado:** Estimule o estudante a se perguntar: *"O que aconteceria se um usuário enviasse um dado inesperado aqui?"*.
