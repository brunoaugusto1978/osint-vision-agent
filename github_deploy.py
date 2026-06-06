#!/usr/bin/env python3
"""
OSINT Vision Agent - GitHub Auto Deploy
Cria o repositório e faz upload de todos os arquivos via GitHub API.
Autor: Bruno Lobo
"""

import os
import sys
import json
import base64
import urllib.request
import urllib.error
from pathlib import Path

# ─── CONFIG ────────────────────────────────────────────────────────────────
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")  # ou cole aqui: "ghp_..."
REPO_NAME    = "osint-vision-agent"
REPO_DESC    = "👁 OSINT Vision Agent — Investigação forense de imagens com múltiplos LLMs (Claude, GPT-4o, Gemini, Groq, Ollama)"
PRIVATE      = False   # True = repositório privado
DEFAULT_BRANCH = "main"

# Arquivos a enviar (relativos a este script)
SCRIPT_DIR = Path(__file__).parent
FILES = [
    "osint_agent.html",
    "README.md",
    "LICENSE",
    ".gitignore",
    "github_deploy.py",
]
# ───────────────────────────────────────────────────────────────────────────


def gh_request(method: str, path: str, body: dict = None) -> dict:
    """Faz uma requisição autenticada à API do GitHub."""
    url = f"https://api.github.com{path}"
    data = json.dumps(body).encode() if body else None
    req = urllib.request.Request(
        url, data=data, method=method,
        headers={
            "Authorization": f"Bearer {GITHUB_TOKEN}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "Content-Type": "application/json",
            "User-Agent": "osint-vision-agent-deploy",
        }
    )
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        print(f"  ✗ HTTP {e.code}: {body}")
        raise


def get_username() -> str:
    print("→ Obtendo usuário autenticado...")
    user = gh_request("GET", "/user")
    username = user["login"]
    print(f"  ✔ Logado como: {username}")
    return username


def create_repo(username: str) -> str:
    """Cria o repositório. Se já existir, retorna a URL."""
    print(f"\n→ Criando repositório '{REPO_NAME}'...")
    try:
        repo = gh_request("POST", "/user/repos", {
            "name": REPO_NAME,
            "description": REPO_DESC,
            "private": PRIVATE,
            "auto_init": False,
            "has_issues": True,
            "has_wiki": False,
        })
        url = repo["html_url"]
        print(f"  ✔ Repositório criado: {url}")
        return url
    except urllib.error.HTTPError:
        # Já existe — busca a URL
        repo = gh_request("GET", f"/repos/{username}/{REPO_NAME}")
        url = repo["html_url"]
        print(f"  ℹ Repositório já existia: {url}")
        return url


def get_sha(username: str, filepath: str) -> str | None:
    """Retorna o SHA do arquivo se já existir no repo (para update)."""
    try:
        resp = gh_request("GET", f"/repos/{username}/{REPO_NAME}/contents/{filepath}")
        return resp.get("sha")
    except urllib.error.HTTPError:
        return None


def upload_file(username: str, filepath: str, local_path: Path) -> None:
    """Cria ou atualiza um arquivo no repositório via API."""
    content = local_path.read_bytes()
    b64_content = base64.b64encode(content).decode()
    sha = get_sha(username, filepath)

    payload = {
        "message": f"{'update' if sha else 'feat'}: add {filepath}",
        "content": b64_content,
        "branch": DEFAULT_BRANCH,
    }
    if sha:
        payload["sha"] = sha

    gh_request("PUT", f"/repos/{username}/{REPO_NAME}/contents/{filepath}", payload)
    action = "atualizado" if sha else "enviado"
    size_kb = len(content) / 1024
    print(f"  ✔ {filepath} {action} ({size_kb:.1f} KB)")


def set_default_branch(username: str) -> None:
    """Garante que a branch padrão seja 'main'."""
    try:
        gh_request("PATCH", f"/repos/{username}/{REPO_NAME}", {
            "default_branch": DEFAULT_BRANCH
        })
        print(f"  ✔ Branch padrão definida: {DEFAULT_BRANCH}")
    except Exception:
        pass  # Não crítico


def add_topics(username: str) -> None:
    """Adiciona tópicos/tags ao repositório."""
    topics = ["osint","cybersecurity","llm","claude","gpt4","gemini","forensics","python","image-analysis","threat-intelligence"]
    try:
        gh_request("PUT", f"/repos/{username}/{REPO_NAME}/topics", {"names": topics})
        print(f"  ✔ Tópicos adicionados: {', '.join(topics)}")
    except Exception:
        pass


def main():
    print("=" * 60)
    print("  OSINT Vision Agent — GitHub Deploy")
    print("=" * 60)

    # Validar token
    global GITHUB_TOKEN
    if not GITHUB_TOKEN or GITHUB_TOKEN == "ghp_...":
        GITHUB_TOKEN = input("\n🔑 Cole seu GitHub Personal Access Token (ghp_...): ").strip()
    if not GITHUB_TOKEN:
        print("✗ Token não fornecido. Abortando.")
        sys.exit(1)

    try:
        username = get_username()
        repo_url = create_repo(username)

        print(f"\n→ Enviando {len(FILES)} arquivo(s)...")
        for fname in FILES:
            local = SCRIPT_DIR / fname
            if not local.exists():
                print(f"  ⚠ Arquivo não encontrado, pulando: {fname}")
                continue
            upload_file(username, fname, local)

        set_default_branch(username)
        add_topics(username)

        print("\n" + "=" * 60)
        print("  ✅ DEPLOY CONCLUÍDO COM SUCESSO!")
        print(f"  🔗 {repo_url}")
        print("=" * 60)
        print(f"\n  Clone local:")
        print(f"  git clone https://github.com/{username}/{REPO_NAME}.git")

    except Exception as e:
        print(f"\n✗ Erro fatal: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
