# How to Run: Codebranch Repositories Orchestrator

This guide explains how to install dependencies and run the orchestrator CLI, as well as how to manually configure and run each managed project.

## Prerequisites

Before running the orchestrator, make sure you have the following installed on your system:

- [Python 3.8+](https://www.python.org/downloads/) (required for FastAPI and the orchestrator)
- [pnpm](https://pnpm.io/installation) (required for NextJS and NestJS)
- [Git](https://git-scm.com/downloads) (to clone the repositories)
- [Node.js 16+](https://nodejs.org/) (required by pnpm, NextJS, and NestJS)
- [pip](https://pip.pypa.io/en/stable/installation/) (Python package manager)

Optional but recommended:
- A code editor like [VS Code](https://code.visualstudio.com/)

---

## Main Commands

### 1. Install orchestrator dependencies
```sh
pip install -r requirements.txt
```

### 2. Run the CLI

#### Global (All Projects)
```sh
python -m orchestrator.main setup      # Clone repos and install dependencies for all projects
python -m orchestrator.main start      # Start all services
python -m orchestrator.main clean      # Remove cloned repositories and generated files
```

#### Per Project
```sh
# FastAPI only
python -m orchestrator.main setup --fastapi
python -m orchestrator.main start --fastapi

# NestJS only
python -m orchestrator.main setup --nestjs
python -m orchestrator.main start --nestjs

# NextJS only
python -m orchestrator.main setup --nextjs
python -m orchestrator.main start --nextjs
```

When using the orchestrator, the microservice repositories (FastAPI, NestJS, NextJS) will be cloned at the same directory level as the orchestrator. You do not need to manually create folders; the orchestrator handles this automatically.

There is no required order to start the services. Each project can be tested independently, as they are not strictly interdependent. You can verify each service by accessing its main endpoint, docs url or health check (see each project's README for details).


## Environment Variables

All required environment variables for each project are listed in their respective `.env.example` files. The orchestrator automatically creates the `.env` files from these examples when you run the setup command (global or per project). You only need to edit the generated `.env` files if you want to change default ports or credentials.

If you run the microservices manually, copy the `.env.example` to `.env` and customize as needed.

If you change the default ports in the `.env` files, ensure that each service uses a unique port to avoid conflicts. The orchestrator and each microservice use conventional ports, but you can modify them as needed. If you use the orchestrator to start services, the ports in the orchestrator's `.env` must match those in each microservice's `.env`.

---

## Manual Configuration & How to Run Each Project

Below is a summary of how to manually configure and run each managed project, in case you want to review or test them individually:

### FastAPI Microservice (`codebranch-fastapi-geoprocesor-ms`)
1. Clone the repository:
   ```sh
   git clone <REPOSITORY_URL>
   cd codebranch-fastapi-geoprocesor-ms
   ```
2. (Recommended) Create and activate a Python virtual environment:
   ```sh
   python -m venv venv
   venv\Scripts\activate  # Windows
   # or
   source venv/bin/activate  # Linux/Mac
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Copy `.env.example` to `.env` and customize as needed.
5. Run the service:
   ```sh
   uvicorn src.app:app --reload --port <API_PORT>
   ```
   (You can also use Docker: see the project's README for details.)

### NestJS Microservice (`codebranch-nestjs-mdw-ms`)
1. Clone the repository:
   ```sh
   git clone <REPOSITORY_URL>
   cd codebranch-nestjs-mdw-ms
   ```
2. Install dependencies:
   ```sh
   pnpm install
   # or
   npm ci
   ```
3. Copy `.env.example.txt` to `.env` and customize as needed.
4. Run the service (development):
   ```sh
   pnpm start:dev
   # or
   npm run start:dev
   ```
   (You can also use Docker: see the project's README for details.)

### NextJS Frontend (`codebranch-nextjs-geoprocesor-frontend`)
1. Clone the repository:
   ```sh
   git clone <REPOSITORY_URL>
   cd codebranch-nextjs-geoprocesor-frontend
   ```
2. Install dependencies:
   ```sh
   pnpm install
   # or
   npm install
   ```
3. Copy `env.example` to `.env.local` and customize as needed (set port and API URLs).
4. Run the frontend:
   ```sh
   pnpm dev --port 4000
   # or
   npm run dev -- --port 4000
   ```
   (You can also use Docker: see the project's README for details.)

---
## Docker & Compose

Each project includes a Dockerfile for containerized deployment. A `docker-compose.yml` is included in the orchestrator repository to facilitate running all services together with Docker Compose. This functionality is under development and may require adjustments. Refer to the orchestrator repository for updates and usage instructions.

