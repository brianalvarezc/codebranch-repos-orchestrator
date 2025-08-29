# Proyecto Orquestador CLI en Python

Este ejemplo implementa una CLI básica usando Typer para orquestar la descarga, instalación y arranque de los tres proyectos (FastAPI, NestJS, Next.js).

## Estructura sugerida
```
codebranch-repos-orchestrator/
├── orchestrator/
│   ├── __init__.py
│   ├── main.py
│   ├── utils.py
│   └── config.py
├── README.md
├── opciones.md
├── requirements.txt
```

## Ejemplo de código principal (`orchestrator/main.py`)
```python
import typer
import subprocess
import os
from orchestrator.utils import clone_repo, install_deps, start_service

app = typer.Typer()

REPOS = {
    "fastapi": {
        "url": "<FASTAPI_REPO_URL>",
        "path": "../codebranch-fastapi-geoprocesor-ms",
        "install": "pip install -r requirements.txt",
        "start": "uvicorn src.app:app --reload --port 8000"
    },
    "nestjs": {
        "url": "<NESTJS_REPO_URL>",
        "path": "../codebranch-nestjs-mdw-ms",
        "install": "npm ci",
        "start": "npm run start:dev"
    },
    "nextjs": {
        "url": "<NEXTJS_REPO_URL>",
        "path": "../codebranch-nextjs-geoprocesor-frontend",
        "install": "pnpm install",
        "start": "pnpm dev --port 4000"
    }
}

@app.command()
def setup():
    """Clona los repos y instala dependencias"""
    for name, repo in REPOS.items():
        clone_repo(repo["url"], repo["path"])
        install_deps(repo["install"], repo["path"])

@app.command()
def start():
    """Arranca los servicios en terminales separados"""
    for name, repo in REPOS.items():
        start_service(repo["start"], repo["path"], name)

if __name__ == "__main__":
    app()
```

## Ejemplo de utilidades (`orchestrator/utils.py`)
```python
import subprocess
import os

def clone_repo(url, path):
    if not os.path.exists(path):
        subprocess.run(["git", "clone", url, path])
    else:
        print(f"Repo {path} ya existe.")

def install_deps(command, path):
    print(f"Instalando dependencias en {path}...")
    subprocess.run(command, cwd=path, shell=True)

def start_service(command, path, name):
    print(f"Arrancando {name}...")
    subprocess.Popen(command, cwd=path, shell=True)
```

## `requirements.txt`
```
typer
```

## Uso
1. Instala dependencias del orquestador:
   ```sh
   pip install -r requirements.txt
   ```
2. Ejecuta la CLI:
   ```sh
   python -m orchestrator.main setup
   python -m orchestrator.main start
   ```

**Nota:** Debes reemplazar `<FASTAPI_REPO_URL>`, `<NESTJS_REPO_URL>`, `<NEXTJS_REPO_URL>` por las URLs reales de tus repositorios.
