

# Orquestador de Repositorios Codebranch

Este orquestador fue creado para facilitar la validación y pruebas de código de los microservicios de la prueba de Codebranch de forma local y ágil. Permite automatizar la descarga, instalación, configuración y arranque de los proyectos FastAPI, NestJS y NextJS desde una sola CLI.

Cada proyecto gestionado ya cuenta con su propio Dockerfile para despliegue en ambientes productivos o de desarrollo, pero este orquestador agiliza el proceso de validación y pruebas locales sin necesidad de contenedores.

## Requisitos previos

Antes de ejecutar el orquestador, asegúrate de tener instalado lo siguiente en tu sistema:

- [Python 3.8+](https://www.python.org/downloads/) (requerido para FastAPI y el orquestador)
- [pnpm](https://pnpm.io/installation) (requerido para NextJS y NestJS)
- [Git](https://git-scm.com/downloads) (para clonar los repositorios)
- [Node.js 16+](https://nodejs.org/) (requerido por pnpm, NextJS y NestJS)
- [pip](https://pip.pypa.io/en/stable/installation/) (gestor de paquetes de Python)

Opcional pero recomendado:
- Un editor de código como [VS Code](https://code.visualstudio.com/)

## Comandos principales

1. Instala dependencias del orquestador:
   ```sh
   pip install -r requirements.txt
   ```
2. Ejecuta la CLI:
   ```sh
   python -m orchestrator.main setup      # Clona repos y instala dependencias
   python -m orchestrator.main start      # Arranca los servicios
   python -m orchestrator.main clean      # Elimina los repositorios clonados y archivos generados
   ```

**Nota:** Debes personalizar las variables de entorno en `.env` según tu entorno local y verificar las URLs de los repositorios en el código.

## Estructura

- `orchestrator/main.py`: CLI principal
- `orchestrator/utils.py`: utilidades para gestión de repos y servicios
- `.env.example`: ejemplo de variables de entorno
- `requirements.txt`: dependencias del orquestador

## Repositorios gestionados
- FastAPI: codebranch-fastapi-geoprocesor-ms
- NestJS: codebranch-nestjs-mdw-ms
- NextJS: codebranch-nextjs-geoprocesor-frontend
