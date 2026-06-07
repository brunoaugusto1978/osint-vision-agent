# 👁 OSINT Vision Agent

> Forensic image investigation tool powered by multiple LLMs via computer vision.

**Author:** Bruno Lobo  
**License:** MIT  
**Version:** 3.0

---

## 🔍 What is it?

**OSINT Vision Agent** is an open-source intelligence (OSINT) tool that analyzes any image and extracts the maximum amount of investigative information, including:

- 📍 **Implicit geolocation** — country, city, specific location, estimated coordinates
- ⏱ **Temporal analysis** — time of day, season, probable date
- 🔍 **Identified entities** — people, vehicles, aircraft, establishments
- 💾 **Digital clues** — visible text, watermarks, UI interfaces, QR codes
- 👤 **Identity profile** — possible usernames, suspected platforms
- ⚠️ **Threat indicators** — exposed sensitive data, privacy risks
- 🧭 **Investigation plan** — main hypothesis, next actions, reverse search queries

---

## 🤖 Supported providers

| Provider | Models | API Key |
|----------|--------|---------|
| 🟢 **Claude (Anthropic)** | claude-opus-4-5, sonnet-4-5, haiku-4-5 | [console.anthropic.com](https://console.anthropic.com) |
| ⚪ **GPT-4o (OpenAI)** | gpt-4o, gpt-4o-mini, gpt-4-turbo | [platform.openai.com](https://platform.openai.com) |
| 🔵 **Gemini (Google)** | gemini-2.0-flash, 1.5-pro, 1.5-flash | [aistudio.google.com](https://aistudio.google.com) |
| 🔴 **Groq (Cloud)** | llama-4-scout, llava, llama-3.2-vision | [console.groq.com](https://console.groq.com) *(free tier)* |
| 🟣 **Ollama (Local)** | llava, moondream, llama3.2-vision | No key — runs offline |

---

## 🚀 How to use

### Option 1 — Direct in browser (no installation)

1. Download `osint_agent.html`
2. Open it in your browser (Chrome, Firefox, Edge)
3. Select your LLM provider
4. Enter your API Key and click **SAVE**
5. Drag an image or paste a URL
6. Click **⚡ START OSINT ANALYSIS**

> ⚠️ **Security notice:** The API Key is stored only for the current browser session via `sessionStorage` and discarded when the tab is closed. **Do not use personal, corporate or production keys** in this standalone version — calls are made directly from the browser to the LLM provider. For safe use, run **Ollama locally** (Option 2) or implement a backend proxy.

### Option 2 — Local Ollama (100% offline, no data sent)

```bash
# Install Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Pull a vision-capable model
ollama pull llava

# Serve the HTML locally (required for CORS)
python -m http.server 8080

# In another terminal — run Ollama with a specific origin (do NOT use *)
OLLAMA_ORIGINS=http://localhost:8080 ollama serve
```

Open `http://localhost:8080/osint_agent.html`, select **🟣 OLLAMA LOCAL** and use `http://localhost:11434` as the endpoint.

---

## 📸 Supported image formats

| Format | Support |
|--------|---------|
| JPEG   | ✅ |
| PNG    | ✅ |
| WebP   | ✅ |
| GIF    | ✅ |
| HEIC / HEIF | ❌ — convert to JPEG first |
| AVIF   | ❌ — convert to JPEG first |
| BMP / TIFF  | ❌ — convert to JPEG first |

On Windows: open the image in Paint and save as JPEG.

---

## 🔎 Investigative use cases

- **Airplane window photo** → identifies airline, probable route, origin/destination airport
- **Street photo** → determines country and city from architecture, signs, vehicles and vegetation
- **Public place selfie** → identifies establishment in the background, time from sunlight angle
- **Screenshot** → extracts status bar time, app, carrier, system language
- **Event photo** → identifies venue from stage/banner, probable date, visible people
- **Missing person image** → extracts all visual clues for investigation

---

## ⚠️ Legal disclaimer

This tool is intended exclusively for:
- Legitimate security investigations
- Academic OSINT research
- Authorized forensic analysis
- Protection and location of missing persons

**Use for illegal purposes, unauthorized surveillance or privacy invasion is expressly prohibited and solely the user's responsibility.**

---

## 🏗 Repository structure

```
osint-vision-agent/
├── osint_agent.html     # Main application (single-file, zero dependencies)
├── github_deploy.py     # Optional deploy script via GitHub API
├── README.md            # This documentation
├── LICENSE              # MIT License
└── .gitignore           # Git ignore rules
```

---

## 🤝 Contributing

Pull requests are welcome. For major changes, open an issue first to discuss what you'd like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m 'feat: add support for X'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Pull Request

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

Copyright (c) 2026 Bruno Lobo
