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

> ⚠️ **Aviso de segurança:** A API Key é armazenada apenas na sessão atual do browser via `sessionStorage` e descartada ao fechar a aba. **Não use chaves pessoais, corporativas ou de produção** nesta versão standalone — as chamadas são feitas diretamente do navegador para o provedor LLM. Para uso seguro, utilize **Ollama local** (Opção 2) ou implemente um backend/proxy.

### Opção 2 — Ollama Local (100% offline, sem enviar dados)

```bash
# Instalar Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Baixar modelo com suporte a visão
ollama pull llava

# Servir o HTML localmente (necessário para CORS)
python -m http.server 8080

# Em outro terminal — rodar Ollama com origem específica (NÃO use *)
OLLAMA_ORIGINS=http://localhost:8080 ollama serve
```

Acesse `http://localhost:8080/osint_agent.html`, selecione **🟣 OLLAMA LOCAL** e use `http://localhost:11434` como endpoint.

---

## 📸 Formatos de imagem suportados

| Formato | Suporte |
|---------|---------|
| JPEG    | ✅ |
| PNG     | ✅ |
| WebP    | ✅ |
| GIF     | ✅ |
| HEIC / HEIF | ❌ — converta para JPEG antes de usar |
| AVIF    | ❌ — converta para JPEG antes de usar |
| BMP / TIFF | ❌ — converta para JPEG antes de usar |

Para converter no Windows: abra a imagem no Paint e salve como JPEG.

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
python3 github_deploy.py
```

Ou definindo o token via variável de ambiente (recomendado):

```bash
export GITHUB_TOKEN="seu_token_aqui"
python3 github_deploy.py
unset GITHUB_TOKEN
```

### Gerando o Personal Access Token (PAT)

1. Acesse [github.com/settings/tokens](https://github.com/settings/tokens)
2. **Generate new token (classic)**
3. Escopos necessários: ✅ `repo` (acesso completo a repositórios)
4. Cole o token quando solicitado (entrada oculta — não aparece na tela)
