# 🤖 DIO Agent

> Seu mentor de Inteligência Artificial para aprender mais e melhor na [DIO](https://dio.me).

O **DIO Agent** é um agente de IA que acompanha você na sua jornada de estudos. Ele conhece as experiências da DIO (Bootcamps, Formações, Cursos, Desafios e muito mais) e ajuda você a estudar com mais clareza, destravar desafios e entender qualquer conceito.

E você não precisa instalar nada complicado. Em **3 passos simples**, o seu mentor de IA estará pronto para usar.

---

## ✨ Antes de começar: dois conceitos rápidos

Para usar o DIO Agent, basta entender duas palavras. As duas estão no [Glossário completo](docs/glossary.md), mas aqui vai a versão rápida:

- 🧠 **Agente de IA:** um chatbot comum responde perguntas, como um buscador mais esperto. Um *agente* de IA vai além: ele lê, planeja e executa passos para te ajudar a alcançar um objetivo. É a diferença entre alguém que te explica o caminho e alguém que caminha junto com você. O DIO Agent é um agente desse tipo: um tutor particular que acompanha a sua evolução.

- 🖥️ **Harness:** é o programa onde a conversa com o agente acontece. Vale a comparação: o agente é o professor, e o harness é a sala de aula. O mesmo professor pode dar aula em salas diferentes. Por isso o DIO Agent funciona em qualquer harness: você escolhe a "sala" no Passo 1, e o seu mentor continua o mesmo.

Pronto. Com isso já dá para começar.

---

## 🎯 O que o DIO Agent faz por você

| Você precisa de... | O DIO Agent... |
|--------------------|----------------|
| Saber por onde começar | Monta um plano de estudos no seu ritmo |
| Destravar um desafio | Te guia até a solução, sem entregar a resposta pronta |
| Entender um conceito | Explica de forma simples, com analogias e exemplos |
| Auditar código e segurança | Analisa vulnerabilidades com matriz de risco e boas práticas defensivas |

Ele conhece os formatos da DIO: Bootcamps, Formações, Acelerações, Cursos, English4Tech, Desafios de Código, Desafios de Projeto, Desafios Criativos, Lives e Mentorias. Assim, as recomendações sempre apontam para algo que você já tem na plataforma.

---

## 🚀 Comece em 3 passos

### 1️⃣ Instale um Harness

O harness é o programa que dá vida ao agente. Recomendamos o **Google Antigravity**, que tem limites de uso mais generosos para quem está começando. Mas qualquer harness moderno funciona.

| Harness | Documentação oficial |
|---------|----------------------|
| Google Antigravity (recomendado) | https://antigravity.google/docs |
| Claude Code | https://docs.claude.com/en/docs/claude-code |
| Codex | https://developers.openai.com/codex |
| OpenCode | https://opencode.ai/docs |
| Hermes | https://hermes-agent.nousresearch.com/docs |

Escolha um e siga o passo a passo da documentação oficial dele. Cada documentação já traz tudo certinho para o seu sistema, então a instalação é tranquila.

### 2️⃣ Configure o DIO Agent

Agora você vai baixar este repositório para o seu computador. Escolha a forma mais simples para você:

**Opção A: com Git** (se você já usa Git)

```bash
git clone https://github.com/digitalinnovationone/dio-agent.git
```

**Opção B: baixando o .zip** (se você não usa Git)

Na página do repositório no GitHub, clique no botão verde **Code** e depois em **Download ZIP**. Em seguida, extraia a pasta em um lugar fácil de encontrar.

Com o repositório baixado, abra a pasta `dio-agent` no harness que você instalou. Cada harness tem o seu jeito de abrir uma pasta de projeto, e a documentação dele mostra como fazer isso.

E é só isso! O harness lê automaticamente o arquivo `AGENTS.md` e o agente já sabe quem é: o seu mentor de estudos da DIO.

> 🔄 **Fique de olho nas atualizações.** Não importa se você usou o Git ou o .zip: o repositório do DIO Agent evolui com o tempo. De tempos em tempos, vale voltar aqui e pegar a versão mais recente. Quem usou Git pode rodar `git pull` (ou pedir pro próprio DIO Agent rodar); quem baixou o .zip pode baixar de novo. Assim o seu mentor está sempre com o melhor que a gente tem a oferecer.

### 3️⃣ Hands On!

Agora é só conversar. Você pode falar naturalmente, com as suas palavras. Mas, principalmente nas primeiras vezes, vale usar um modelo de prompt pronto: é só copiar e preencher os campos entre colchetes. Quanto mais contexto você dá, melhor o agente ajuda.

**🗺️ Plano de estudos**

```
Quero montar um plano de estudos (se possível, com materiais complementares).
- Meu objetivo: [ex: aprender mais sobre IA, ser dev back-end, concluir um bootcamp]
- Experiência ou carreira da DIO: [URL ou nome do bootcamp/formação, ou de uma carreira da DIO]
- Meu nível hoje: [iniciante, intermediário, avançado]
- Tempo disponível: [ex: 1 hora por dia, de segunda a sexta]
```

**🔓 Destravar desafio**

```
Estou travado em um Desafio de [Código, Projeto ou Criativo] da DIO.
- O que o desafio pede: [cole o enunciado ou descreva]
- Onde eu travei: [explique o ponto da dificuldade]
- Meu código atual: [cole aqui, se for Desafio de Código]
- Link do repositório base: [cole aqui, se for Desafio de Projeto]
Me ajuda a destravar sem dar a resposta pronta.
```

**💡 Explicar conceito**

```
Me explica o conceito de [ex: API, laço de repetição, herança].
- Meu nível: [nunca vi, já ouvi falar, quero aprofundar]
- Onde apareceu: [ex: no curso X de um bootcamp] (opcional)
```

**🛡️ Análise de vulnerabilidades**

```
Analise este trecho de código ou configuração em busca de falhas de segurança.
- Contexto da aplicação: [ex: API Flask de login, script de automação, etc.]
- Código: [cole o trecho de código aqui]
- Objetivo: [ex: auditar contra OWASP Top 10, verificar se há falhas e sugerir trilha de estudos]
```

Não precisa de comando especial nem de formato perfeito: o agente conduz a conversa a partir daí e pede mais detalhes se precisar.

---

## 🧩 As skills do agente

Uma **skill** é uma habilidade do agente, descrita em um guia passo a passo:

| Skill | Para que serve |
|-------|----------------|
| [Plano de estudos](skills/study-plan/SKILL.md) | Organiza o que estudar, em que ordem e em quanto tempo |
| [Destravar desafio](skills/unblock-challenge/SKILL.md) | Conduz você até a solução de um desafio, sem dar a resposta pronta |
| [Explicar conceito](skills/explain-concept/SKILL.md) | Explica conceitos de forma didática, com analogias e exemplos |
| [Análise de vulnerabilidades](skills/vulnerability-analysis/SKILL.md) | Analisa falhas de segurança (OWASP), gera matriz de risco e orienta a correção defensiva |

Você não precisa "chamar" uma skill. O agente percebe o que você precisa e usa a skill certa sozinho.

---

## 🗂️ Estrutura do repositório

```
dio-agent/
├── README.md                        Este guia
├── AGENTS.md                        Definição do agente (lida por qualquer harness)
├── CLAUDE.md                        Atalho para o Claude Code
│
├── agent/
│   ├── persona.md                   A personalidade e o tom do agente
│   └── knowledge/
│       ├── dio-platform.md          O que é a DIO
│       ├── learning-experiences.md  Os formatos de aprendizado da DIO
│       └── security-basics.md       Fundamentos de segurança defensiva e AppSec
│
├── skills/
│   ├── README.md                    O que são skills
│   ├── study-plan/                  Skill: plano de estudos
│   ├── unblock-challenge/           Skill: destravar desafio
│   ├── explain-concept/             Skill: explicar conceito
│   └── vulnerability-analysis/      Skill: análise de vulnerabilidades (GuardAI)
│
└── docs/
    └── glossary.md                  Glossário de termos
```

> 🔍 **Por que funciona em qualquer harness?** O coração do projeto é o arquivo `AGENTS.md`, um padrão aberto que harnesses modernos sabem ler. O `CLAUDE.md` apenas aponta para ele, então você pode usar o harness que preferir.

---

## 📖 Glossário rápido

Termos como *agente*, *harness*, *skill* e *prompt* estão explicados com analogias simples no **[Glossário completo](docs/glossary.md)**. Se algum termo soar estranho, comece por lá.

---

## 💬 Sobre este projeto

O DIO Agent foi criado para acompanhar você desde o início dos Bootcamps e Formações da DIO. A ideia é simples: aprender na era da IA fica mais fácil quando você tem um mentor disponível a qualquer hora.

Bons estudos, e vem com a gente. 🚀

---

## 🛡️ Evolução e Customização do Agente (GuardAI)

Esta seção detalha as implementações, customizações e testes práticos realizados no projeto para especializar o **DIO Agent** em mentoria de cibersegurança e análise defensiva de vulnerabilidades (AppSec).

### 🎯 Especialização e Propósito

O agente foi especializado como um **Mentor Educacional em Cibersegurança e Análise de Vulnerabilidades**. 

O objetivo principal dessa especialização é evitar que a segurança da informação seja vista como um tópico intimidador para iniciantes. Além de auditar falhas técnicas segundo referências da indústria (OWASP Top 10 e CWE) e mensurar os riscos de forma estruturada, o agente foi calibrado para gerar **analogias com situações do cotidiano**. Dessa forma, estudantes que estão começando a programar conseguem compreender o impacto real de uma vulnerabilidade intuitivamente, sem depender de jargões complexos logo de início.

### 📝 Modificações e Arquivos Criados/Alterados

1. **Nova Skill de Segurança (`skills/vulnerability-analysis/`):**
   - [`SKILL.md`](skills/vulnerability-analysis/SKILL.md): Instruções operacionais padronizando a avaliação em matriz de risco 3x3 (Probabilidade x Impacto = Severidade Geral), análise simultânea de múltiplas falhas com tabelas dedicadas, inclusão obrigatória de analogias cotidianas e proteção da integridade de desafios educacionais (sem entrega de código pronto).
   - [`README.md`](skills/vulnerability-analysis/README.md): Documentação voltada a humanos explicando os objetivos, o formato padronizado de saída e os prompts de teste da skill.

2. **Base de Conhecimento (`agent/knowledge/security-basics.md`):**
   - Criação do documento de referência contendo os princípios da Tríade CIA (Confidencialidade, Integridade e Disponibilidade), mentalidade *Shift-Left*, conceitos de vulnerabilidade, ameaça e risco, além das principais falhas do OWASP Top 10 e diretrizes éticas defensivas.

3. **Persona e Comportamento (`agent/persona.md` e `AGENTS.md`):**
   - [`agent/persona.md`](agent/persona.md): Transformação do agente em um mentor educacional socrático. O agente foi explicitamente configurado para **investigar o contexto antes de sugerir comandos ou scripts**, acolher erros como oportunidades pedagógicas e orientar com dicas reflexivas.
   - [`AGENTS.md`](AGENTS.md): Registro da nova skill na tabela de roteamento oficial e inclusão da referência ao `security-basics.md` na base de conhecimento.

4. **Auditoria Prática e Evolutiva (`identificacao-da-falha.md`):**
   - Criação e condução de um ciclo de auditoria contínua a partir de um código vulnerável (`app.py`), aplicando defesas em profundidade em `app-corrigido.py`:
     - **Ciclo 1:** Identificação e correção de SQL Injection (CWE-89) com Prepared Statements.
     - **Ciclo 2:** Identificação de riscos criptográficos (SHA-256 sem salt) e enumeração temporal (Timing Attack), mitigados com `bcrypt` e `DUMMY_HASH`.
     - **Ciclo 3:** Identificação de riscos de DoS em memória (CWE-400) e DoS de conta (CWE-645), mitigados com cache LRU em memória e rate limiting em duas camadas (IP + Conta).
   - Padronização completa do relatório [`identificacao-da-falha.md`](identificacao-da-falha.md) utilizando matrizes de risco padronizadas e recomendações de trilhas de estudo da DIO.

5. **Validação Prática da Nova Persona:**
   - Realização de teste prático em cenário real de um servidor Ubuntu de laboratório exposto na internet. O agente validou seu novo comportamento com sucesso: em vez de disparar comandos de terminal de imediato, iniciou a interação questionando o propósito do ambiente, o estado da máquina e o objetivo da análise antes de recomendar qualquer ação.

### 🚀 Como Executar no Harness

1. **Harness Utilizado:** Google Antigravity (harness oficial indicado no começo do curso).
2. **Execução:**
   - Abra a pasta raiz deste repositório (`dio-agent/`) no Google Antigravity. O harness carregará automaticamente as diretrizes de `AGENTS.md`, a persona e todas as skills.
   - Para interagir com a especialização criada, basta perguntar sobre a segurança de um código, configuração ou cenário (ex.: *"Analise a segurança deste código em busca de falhas"*, ou *"Tenho um servidor exposto na internet, como começo a avaliar a segurança?"*).
   - O agente conduzirá a conversa de forma socrática e didática, aplicando as matrizes de risco, analogias do cotidiano e recomendações de estudo da DIO.
