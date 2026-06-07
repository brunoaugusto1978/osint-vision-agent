# Security Policy

## Project Security Scope

OSINT Vision Agent is an experimental standalone tool for study, research, and laboratory use.

It is not intended for corporate, production, regulated, or sensitive investigation environments without significant architectural changes.

Known architectural limitations include:

* No secure backend/proxy in the standalone version.
* Direct browser-to-LLM API calls.
* API keys available on the client side during the browser session.
* `sessionStorage` used for temporary key storage.
* Optional use of public CORS proxies for URL loading.
* Inline JavaScript/CSS due to the single-file design.

These limitations are documented and currently accepted for the standalone laboratory version.

---

## Reporting a Vulnerability

If you discover a security vulnerability, please report it responsibly.

**Preferred reporting method:**

1. Use GitHub private vulnerability reporting if enabled for this repository.
2. If private reporting is not available, open a minimal public issue saying that you have a security concern, but **do not include exploit details, secrets, payloads, or sensitive data**.
3. Wait for a maintainer to provide a private communication channel.

**Please do not publicly disclose:**

* Working exploit payloads.
* API keys or tokens.
* Private images.
* Sensitive investigation data.
* Personal data.
* Abuse techniques that could harm users.

---

## What to Include

A good security report should include:

* Affected file and line number.
* Vulnerability type.
* Impact.
* Steps to reproduce.
* Proof of concept, if safe to share privately.
* Suggested fix, if available.
* Whether the issue affects the standalone version, local Ollama mode, or a proposed backend mode.

---

## Security Issues We Care About

Examples of valid security issues:

* API key exposure beyond the documented standalone risk.
* XSS or HTML injection in LLM-rendered output.
* Unsafe handling of image MIME types.
* Reintroduction of `localStorage` for secrets.
* Silent leakage of investigated URLs.
* Unsafe CORS configuration.
* Hardcoded secrets or tokens.
* Dependency or supply-chain risks, if dependencies are added in the future.
* Unsafe backend/proxy behavior, if backend support is added.

---

## Known Accepted Risks

The following are known and accepted for the experimental standalone version:

* API keys are present in the browser during the active session.
* External LLM providers may receive the image and context.
* Public CORS proxies may see URLs if the user explicitly confirms URL loading.
* CSP still allows inline script/style because the app is currently a single HTML file.

These are not considered vulnerabilities unless they exceed the documented behavior or introduce additional unintended exposure.

---

## Response Expectations

This is a community/laboratory project maintained on a best-effort basis.

Security reports will be reviewed as time allows. Critical issues involving unintended credential exposure, XSS, or unsafe data leakage will be prioritized.
