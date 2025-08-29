

import typer
from orchestrator.utils import (
    clone_repo, 
    install_deps, 
    start_service, 
    clean_generated, 
    create_env_file, 
    create_and_activate_venv
)
from dotenv import load_dotenv
import os
import subprocess


app = typer.Typer()


# Cargar variables de entorno desde .env
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

REPOS = {
    "fastapi": {
        "url": "https://github.com/brianalvarezc/codebranch-fastapi-geoprocesor-ms.git",
        "path": "../codebranch-fastapi-geoprocesor-ms",
        "install": "pip install -r requirements.txt",
        "start": f"uvicorn src.app:app --reload --port {os.getenv('API_PORT', '8000')}"
    },
    "nestjs": {
        "url": "https://github.com/brianalvarezc/codebranch-nestjs-mdw-ms.git",
        "path": "../codebranch-nestjs-mdw-ms",
        "install": "pnpm install",
        "start": f"pnpm start:dev --port {os.getenv('NEST_PORT', '3000')}"
    },
    "nextjs": {
        "url": "https://github.com/brianalvarezc/codebranch-nextjs-geoprocesor-frontend.git",
        "path": "../codebranch-nextjs-geoprocesor-frontend",
        "install": "pnpm install",
        "start": f"pnpm dev --port {os.getenv('NEXT_PORT', '4000')}"
    }
}

@app.command()
def setup():
    """Clona los repos y instala dependencias"""
    for name, repo in REPOS.items():
        clone_repo(repo["url"], repo["path"])
        env_example = os.path.join(repo["path"], ".env.example")
        env_file = os.path.join(repo["path"], ".env")
        create_env_file(env_example, env_file)

        # Si es el repo de fastapi, crear y activar venv antes de instalar requirements
        if name == "fastapi":
            python_exe = create_and_activate_venv(repo["path"])
            req_path = os.path.join(repo["path"], "requirements.txt")
            if os.path.exists(req_path):
                print(f"Instalando requirements en entorno virtual: {python_exe}")
                subprocess.run(f'"{python_exe}" -m pip install --upgrade pip', shell=True)
                subprocess.run(f'"{python_exe}" -m pip install -r "{req_path}"', shell=True)
            else:
                print(f"No se encontró requirements.txt en {repo['path']}")
        else:
            install_deps(repo["install"], repo["path"])

    # Crear .env del orquestador si no existe
    orchestrator_env = os.path.join(os.path.dirname(__file__), '..', '.env')
    create_env_file(
        example_path=os.path.join(os.path.dirname(__file__), '..', '.env.example'),
        env_path=orchestrator_env,
        default_content="# Configuración del orquestador\n"
    )


@app.command()
def setup(
    fastapi: bool = typer.Option(False, help="Setup only FastAPI project"),
    nestjs: bool = typer.Option(False, help="Setup only NestJS project"),
    nextjs: bool = typer.Option(False, help="Setup only NextJS project")
):
    """Clone repos and install dependencies (all or per project)"""
    targets = []
    if fastapi:
        targets.append("fastapi")
    if nestjs:
        targets.append("nestjs")
    if nextjs:
        targets.append("nextjs")
    if not targets:
        targets = list(REPOS.keys())
    for name in targets:
        repo = REPOS[name]
        clone_repo(repo["url"], repo["path"])
        env_example = os.path.join(repo["path"], ".env.example")
        env_file = os.path.join(repo["path"], ".env")
        create_env_file(env_example, env_file)

        if name == "fastapi":
            python_exe = create_and_activate_venv(repo["path"])
            req_path = os.path.join(repo["path"], "requirements.txt")
            if os.path.exists(req_path):
                print(f"Instalando requirements en entorno virtual: {python_exe}")
                subprocess.run(f'"{python_exe}" -m pip install --upgrade pip', shell=True)
                subprocess.run(f'"{python_exe}" -m pip install -r "{req_path}"', shell=True)
            else:
                print(f"No se encontró requirements.txt en {repo['path']}")
        else:
            install_deps(repo["install"], repo["path"])

    # Crear .env del orquestador si no existe (solo si se hace setup global)
    if not (fastapi or nestjs or nextjs):
        orchestrator_env = os.path.join(os.path.dirname(__file__), '..', '.env')
        create_env_file(
            example_path=os.path.join(os.path.dirname(__file__), '..', '.env.example'),
            env_path=orchestrator_env,
            default_content="# Configuración del orquestador\n"
        )


@app.command()
def start(
    fastapi: bool = typer.Option(False, help="Start only FastAPI project"),
    nestjs: bool = typer.Option(False, help="Start only NestJS project"),
    nextjs: bool = typer.Option(False, help="Start only NextJS project")
):
    """Start services (all or per project)"""
    targets = []
    if fastapi:
        targets.append("fastapi")
    if nestjs:
        targets.append("nestjs")
    if nextjs:
        targets.append("nextjs")
    if not targets:
        targets = list(REPOS.keys())
    for name in targets:
        repo = REPOS[name]
        start_service(repo["start"], repo["path"], name)


@app.command()
def clean():
    """Elimina los repositorios clonados y archivos generados"""
    for name, repo in REPOS.items():
        clean_generated(repo["path"])
    print("Repositorios y archivos generados eliminados.")

if __name__ == "__main__":
    app()
