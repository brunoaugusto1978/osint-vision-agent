# 👁 OSINT Vision Agent
> Experimental learning tool for investigative image analysis using multimodal LLMs.

**Author:** Bruno Lobo  
**License:** MIT  
**Version:** 3.0  
**Status:** Experimental / Laboratory

---

## ⚠️ Important Security Notice

This project is a **standalone** tool that runs directly in the browser. It was created for **study, demonstration, research, and laboratory purposes**.

It is **not suitable for corporate use, production environments, regulated environments, or sensitive investigations** without major architectural changes.

In the current version:

* There is no secure backend or proxy.
* Requests to Anthropic, OpenAI, Gemini, and Groq are made directly from the browser.
* The API key is exposed on the client side during the browser session.
* The key is stored only in `sessionStorage`, but it can still be accessed by any script running in the page context.
* URLs loaded through public CORS proxies may be visible to third parties.
* The tool does not implement corporate controls such as authentication, auditing, user segregation, secret vaulting, secure logging, or centralized key management.

**Do not use personal, corporate, production, or high-billing API keys with this standalone version.**

For a safer laboratory setup, prefer **Ollama Local**, where the analysis runs locally without sending the image or context to external providers.

---

## ✅ Recommended Use

This project is recommended for:

* Visual OSINT studies.
* Technical demonstrations.
* Personal labs.
* Proofs of concept.
* Academic research.
* Testing multimodal models.
* Learning about visual data exposure risks in images.

---

## ❌ Not Recommended For

This project **should not be used as-is** for:

* Corporate environments.
* Production use.
* Sensitive investigations.
* Processing personal or confidential data.
* Cases involving regulated information.
* Official forensic operations.
* Use with corporate API keys.
* Use with confidential, internal, or restricted images.
* Analysis of data that must not be sent to external providers.

For these scenarios, implement a secure backend architecture, secret vaulting, access control, auditing, sanitized logs, data retention policies, and legal/compliance review.

---

## 🔍 What Is It?

**OSINT Vision Agent** is an experimental open-source intelligence tool that analyzes images and attempts to extract investigative clues, such as:

* 📍 Probable geolocation.
* ⏱ Temporal estimation.
* 🔍 Visual entities.
* 💾 Text, brands, signs, interfaces, and watermarks.
* 👤 Possible identity indicators.
* ⚠️ Data exposure risks.
* 🧭 Suggested next OSINT actions.

The analysis is performed by multimodal AI models. Results must be treated as **investigative hypotheses**, not as conclusive evidence.

---

## 🤖 Supported Providers

| Provider           | Mode                   | Notes                             |
| ------------------ | ---------------------- | --------------------------------- |
| Claude / Anthropic | Browser → External API | Requires API key                  |
| OpenAI / GPT-4o    | Browser → External API | Requires API key                  |
| Gemini / Google    | Browser → External API | Requires API key                  |
| Groq               | Browser → External API | Requires API key                  |
| Ollama             | Local                  | Recommended for sensitive lab use |

---

## 🔐 Security Model of the Standalone Version

This version was designed for simplicity and learning, not for enterprise-grade security.

### API Keys

API keys are stored only in the current browser session using `sessionStorage`.

This means:

* The key is not persisted after closing the tab/session.
* The key is still accessible while the page is open.
* An XSS, malicious extension, injected script, or modified HTML file could access the key.

Therefore:

> **Use only disposable, low-privilege, low-spending-limit API keys.**

### Direct LLM API Calls

In the standalone version, the browser communicates directly with the LLM providers.
This exposes the API key on the client side and should not be considered safe for production.

### Public CORS Proxies

When loading images by URL, the tool may use public CORS proxies to bypass browser restrictions.
These services may see the investigated URL.

For sensitive investigations:

> Download the image locally and drag the file into the tool.  
> Do not use URL loading.

---

## 🚀 How to Use

### Option 1 — Standalone Browser Mode

1. Download the `osint_agent.html` file.
2. Open it in your browser.
3. Select the desired provider.
4. Enter a test/lab API key.
5. Drag a local image into the tool.
6. Click **Start OSINT Analysis**.

⚠️ Do not use this option with corporate keys, confidential images, or sensitive data.

---

### Option 2 — Ollama Local

This is the recommended option for a more private laboratory setup.

```bash
# Install Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Download a vision-capable model
ollama pull llava

# Serve the HTML locally
python -m http.server 8080

# In another terminal, start Ollama allowing only the local origin
OLLAMA_ORIGINS=http://localhost:8080 ollama serve
```

Then access:

```
http://localhost:8080/osint_agent.html
```

Select **Ollama Local** and use:

```
http://localhost:11434
```

---

## 📸 Supported Image Formats

| Format      | Support                       |
| ----------- | ----------------------------- |
| JPEG        | ✅                             |
| PNG         | ✅                             |
| WebP        | ✅                             |
| GIF         | ✅                             |
| HEIC / HEIF | ❌ Convert to JPEG before use |
| AVIF        | ❌ Convert to JPEG before use |
| BMP / TIFF  | ❌ Convert to JPEG before use |

---

## 🧪 Laboratory Use Examples

* Analyze a public photo to identify visual clues.
* Test how different LLMs interpret the same image.
* Evaluate data exposure risks in images.
* Study visual geolocation techniques.
* Generate OSINT hypotheses from visible elements.
* Demonstrate the limitations and risks of multimodal AI.

---

## ⚠️ Known Limitations

* The AI may hallucinate information.
* Geolocation and time estimation are approximate.
* Results should not be treated as evidence.
* The tool does not verify whether hypotheses are true.
* The standalone version does not protect API keys like a backend would.
* External providers may receive the image and investigation context.
* Public CORS proxies may expose investigated URLs.

---

## 🏗 Project Structure

```
osint-vision-agent/
├── osint_agent.html      # Main standalone application
├── README.md             # Documentation
├── LICENSE               # MIT License
├── .gitignore            # Git ignored files
└── github_deploy.py      # Optional GitHub API deployment script
```

---

## 🔒 Recommendations for a Future Corporate Version

To make this project suitable for corporate or production use, at minimum, the following would be required:

* Secure backend/proxy for LLM API calls.
* Secret vault integration.
* Authentication and authorization.
* Session management.
* Usage auditing.
* Sanitized logging.
* Rate limiting.
* Strong CSRF/XSS protection.
* CSP without `unsafe-inline`.
* Removal of public CORS proxies.
* Data retention and deletion policy.
* Legal and privacy review.
* Consent and acceptable use model.
* User/tenant isolation.
* Abuse monitoring and alerting.

---

## ⚖️ Legal Notice

This tool must be used only for legitimate, educational, defensive, and authorized purposes.

Use for unauthorized surveillance, privacy invasion, stalking, improper exposure of personal data, or any illegal purpose is strictly prohibited.

The user is solely responsible for how the tool is used, which images are analyzed, which API keys are used, and compliance with applicable laws.

---

## 🤝 Contributing

Contributions are welcome, especially in:

* Security improvements.
* Local-mode enhancements.
* Removing dependency on public proxies.
* Optional secure backend support.
* Privacy improvements.
* Usability improvements.
* Structured JSON response validation.

For major changes, please open an issue before submitting a pull request.

---

## 📄 License

MIT License.

Copyright (c) 2026 Bruno Lobo
