import subprocess
import os

import shutil

def clone_repo(url, path):
    if not os.path.exists(path):
        subprocess.run(["git", "clone", url, path])
    else:
        print(f"Repo {path} ya existe.")

def create_env_file(example_path, env_path, default_content=None):
    """
    Crea un archivo .env a partir de .env.example. Si no existe .env.example, usa default_content si se provee.
    """
    if os.path.exists(example_path):
        with open(example_path, "r", encoding="utf-8") as f:
            content = f.read()
        with open(env_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Archivo .env creado en {env_path}")
    elif default_content is not None:
        with open(env_path, "w", encoding="utf-8") as f:
            f.write(default_content)
        print(f"Archivo .env creado en {env_path} con contenido por defecto")
    else:
        print(f"No se pudo crear .env en {env_path}: no existe .env.example y no se proporcionó contenido por defecto.")

def create_and_activate_venv(path):
    """
    Crea un entorno virtual en el path dado si no existe y retorna la ruta al ejecutable de python del venv.
    """
    venv_path = os.path.join(path, 'venv')
    if not os.path.exists(venv_path):
        print(f"Creando entorno virtual en {venv_path}...")
        subprocess.run(f'python -m venv "{venv_path}"', shell=True, cwd=path)
    else:
        print(f"El entorno virtual ya existe en {venv_path}.")
    # Retornar ruta al ejecutable python del venv
    if os.name == 'nt':
        python_exe = os.path.join(venv_path, 'Scripts', 'python.exe')
    else:
        python_exe = os.path.join(venv_path, 'bin', 'python')
    return python_exe

def install_deps(command, path):
    print(f"Instalando dependencias en {path}...")
    subprocess.run(command, cwd=path, shell=True)

def start_service(command, path, name):
    print(f"Arrancando {name}...")
    subprocess.Popen(command, cwd=path, shell=True)

def clean_generated(path):
    if os.path.exists(path):
        print(f"Eliminando {path}...")
        shutil.rmtree(path)
    else:
        print(f"{path} no existe, nada que eliminar.")
