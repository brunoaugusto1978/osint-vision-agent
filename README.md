# 👁 OSINT Vision Agent

> Ferramenta de investigação forense de imagens com suporte a múltiplos LLMs via visão computacional.

**Autor:** Bruno Lobo  
**Licença:** MIT  
**Versão:** 3.0

---

## 🔍 O que é?

O **OSINT Vision Agent** é uma ferramenta de inteligência de fontes abertas (OSINT) que analisa qualquer imagem e extrai o máximo de informações investigativas possível, incluindo:

- 📍 **Geolocalização implícita** — país, cidade, local específico, coordenadas estimadas
- ⏱ **Análise temporal** — hora do dia, estação do ano, data provável
- 🔍 **Entidades identificadas** — pessoas, veículos, aeronaves, estabelecimentos
- 💾 **Pistas digitais** — textos visíveis, watermarks, interface de UI, QR codes
- 👤 **Perfil de identidade** — usuários possíveis, plataformas suspeitas
- ⚠️ **Indicadores de risco** — dados sensíveis expostos, riscos de privacidade
- 🧭 **Plano investigativo** — hipótese principal, próximas ações, queries de busca reversa

---

## 🤖 Providers suportados

| Provider | Modelos | API Key |
|----------|---------|---------|
| 🟢 **Claude (Anthropic)** | claude-opus-4-5, sonnet-4-5, haiku-4-5 | [console.anthropic.com](https://console.anthropic.com) |
| ⚪ **GPT-4o (OpenAI)** | gpt-4o, gpt-4o-mini, gpt-4-turbo | [platform.openai.com](https://platform.openai.com) |
| 🔵 **Gemini (Google)** | gemini-2.0-flash, 1.5-pro, 1.5-flash | [aistudio.google.com](https://aistudio.google.com) |
| 🔴 **Groq (Cloud)** | llama-4-scout, llava, llama-3.2-vision | [console.groq.com](https://console.groq.com) *(tier gratuito)* |
| 🟣 **Ollama (Local)** | llava, moondream, llama3.2-vision | Sem key — roda offline |

---

## 🚀 Como usar

### Opção 1 — Direto no browser (sem instalação)

1. Baixe o arquivo `osint_agent.html`
2. Abra no seu browser (Chrome, Firefox, Edge)
3. Selecione o provider LLM desejado
4. Insira sua API Key e clique em **SALVAR**
5. Arraste uma imagem ou cole uma URL
6. Clique em **⚡ INICIAR ANÁLISE OSINT**

> A API Key é salva apenas no `localStorage` do seu browser. Nenhum dado é enviado para servidores terceiros além do LLM escolhido.

### Opção 2 — Ollama Local (100% offline, sem enviar dados)

```bash
# Instalar Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Baixar modelo com suporte a visão
ollama pull llava

# Rodar com CORS habilitado
OLLAMA_ORIGINS=* ollama serve
```

Depois abra o `osint_agent.html`, selecione **🟣 OLLAMA LOCAL** e use `http://localhost:11434` como endpoint.

---

## 📸 Formatos de imagem suportados

O agente converte automaticamente qualquer formato para JPEG antes de enviar à API:

| Formato | Suporte nativo API | Conversão automática |
|---------|--------------------|----------------------|
| JPEG    | ✅ | — |
| PNG     | ✅ | — |
| WebP    | ✅ | — |
| GIF     | ✅ | — |
| AVIF    | ❌ | ✅ via canvas |
| HEIC    | ❌ | ✅ via canvas* |
| BMP     | ❌ | ✅ via canvas |
| TIFF    | ❌ | ✅ via canvas |

*HEIC pode requerer browser com suporte nativo (Safari no macOS/iOS).

---

## 🔎 Exemplos de uso investigativo

- **Foto de janela de avião** → identifica companhia aérea, rota provável, aeroporto de origem/destino
- **Foto de rua** → determina país e cidade pela arquitetura, sinalização, veículos e vegetação
- **Selfie em local público** → identifica estabelecimento ao fundo, horário pela luz solar
- **Print de tela** → extrai hora da barra de status, aplicativo, operadora, idioma do sistema
- **Foto de evento** → identifica local pelo palco/banner, data provável, pessoas visíveis
- **Imagem de pessoa desaparecida** → extrai todas as pistas visuais para investigação

---

## ⚠️ Aviso legal

Esta ferramenta é destinada exclusivamente para:
- Investigações de segurança legítimas
- Pesquisa acadêmica em OSINT
- Análise forense autorizada
- Proteção e localização de pessoas desaparecidas

**O uso para fins ilegais, vigilância não autorizada ou invasão de privacidade é expressamente proibido e de responsabilidade exclusiva do usuário.**

---

## 🏗 Estrutura do repositório

```
osint-vision-agent/
├── osint_agent.html     # Aplicação principal (single-file, zero dependências)
├── README.md            # Esta documentação
├── LICENSE              # MIT License
└── .gitignore           # Arquivos ignorados pelo Git
```

---

## 🤝 Contribuindo

Pull requests são bem-vindos. Para mudanças maiores, abra uma issue primeiro para discutir o que você gostaria de modificar.

1. Fork o repositório
2. Crie sua feature branch (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -m 'feat: adiciona suporte a X'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

---

## 📄 Licença

MIT License — veja o arquivo [LICENSE](LICENSE) para detalhes.

Copyright (c) 2026 Bruno Lobo

---

## ⚡ Deploy automático no GitHub

Use o script incluso para criar e popular o repositório automaticamente via API:

```bash
# Instalar dependências (apenas stdlib Python, zero dependências externas)
python3 github_deploy.py
```

Ou passando o token via variável de ambiente:

```bash
GITHUB_TOKEN=ghp_seu_token python3 github_deploy.py
```

### Gerando o Personal Access Token (PAT)

1. Acesse [github.com/settings/tokens](https://github.com/settings/tokens)
2. **Generate new token (classic)**
3. Escopos necessários: ✅ `repo` (acesso completo a repositórios)
4. Cole o token quando o script solicitar
