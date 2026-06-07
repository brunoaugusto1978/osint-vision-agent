# Contributing to OSINT Vision Agent

Thank you for your interest in contributing to OSINT Vision Agent.

This project is an experimental, standalone, browser-based tool for visual OSINT research and laboratory use. It is not intended for corporate or production environments without significant architectural changes.

Please keep that scope in mind when proposing changes.

---

## Project Scope

Accepted contributions should align with one or more of the following goals:

* Improve security for the standalone version.
* Improve privacy and reduce unnecessary data exposure.
* Improve local/offline analysis using Ollama.
* Improve usability and accessibility.
* Improve JSON parsing and response validation.
* Improve documentation and legal/safety notices.
* Reduce reliance on public CORS proxies.
* Add an optional secure backend/proxy architecture.
* Improve browser compatibility.

Out-of-scope contributions include:

* Features designed for covert surveillance.
* Features that encourage unauthorized tracking.
* Collection or enrichment of personal data without consent.
* Credential harvesting or token extraction.
* Any functionality intended for illegal activity.

---

## Local Development

This project is currently a standalone HTML application.

To run it locally:

```bash
python -m http.server 8080
```

Then open:

```
http://localhost:8080/osint_agent.html
```

For local LLM testing with Ollama:

```bash
ollama pull llava
OLLAMA_ORIGINS=http://localhost:8080 ollama serve
```

Then select **Ollama Local** in the UI and use:

```
http://localhost:11434
```

---

## Security Expectations

Do not submit pull requests that:

* Add real API keys, tokens, credentials, or secrets.
* Store API keys in `localStorage`.
* Remove existing security warnings.
* Reintroduce `OLLAMA_ORIGINS=*`.
* Send sensitive data to third-party services without explicit user confirmation.
* Force unsupported image formats into incorrect MIME types.
* Render LLM output without escaping or sanitization.
* Add public proxies without clear privacy warnings and user consent.

API keys must remain temporary and session-based in the standalone version.

For production-grade use, the preferred architecture is a backend/proxy with proper secret management.

---

## Testing Checklist

Before opening a pull request, please test:

### Browser

* Open `osint_agent.html` locally.
* Confirm the browser console has no JavaScript syntax errors.
* Test image upload with:
  * JPEG
  * PNG
  * WebP
  * GIF
* Confirm unsupported formats are blocked:
  * HEIC
  * AVIF
  * TIFF
  * BMP

### Security

Check that your change does not introduce:

* `localStorage` for secrets.
* Hardcoded API keys.
* Hardcoded GitHub tokens.
* Unescaped LLM-rendered HTML.
* Forced MIME type conversion for unsupported images.
* `OLLAMA_ORIGINS=*`.

Useful local checks:

```bash
grep -RniE "localStorage|ghp_|sk-|api_key|token|password|secret|Authorization|Bearer" .
grep -RniE "innerHTML|outerHTML|insertAdjacentHTML" osint_agent.html
```

### Python Deploy Script

If you change `github_deploy.py`, validate:

```bash
python -m py_compile github_deploy.py
```

The deploy script must not upload itself if there is any risk of accidental token exposure.

---

## Commit Style

Please use clear commit messages. Preferred style:

```
feat: add local model configuration
fix: block unsupported image format before upload
security: escape LLM-rendered fields
docs: clarify standalone security limitations
refactor: simplify provider configuration
```

---

## Pull Request Guidelines

Before submitting a pull request:

1. Open an issue first for major changes.
2. Keep pull requests focused and small when possible.
3. Explain the security/privacy impact of your change.
4. Include screenshots for UI changes.
5. Confirm you tested locally.
6. Do not include real investigation data, private images, or secrets.

A good pull request should include:

* What changed.
* Why it changed.
* How it was tested.
* Any security or privacy considerations.

---

## Responsible Use

This project is intended for legitimate, educational, defensive, and authorized research only.

Do not contribute features that facilitate unauthorized surveillance, stalking, privacy invasion, or illegal activity.
