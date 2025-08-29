# Codebranch Repositories Orchestrator

## Project Overview & Architecture Decision

This ecosystem is designed as a multi-repository architecture, with each microservice (FastAPI, NestJS, NextJS) in its own repository. This separation allows for independent development, testing, and deployment, following best practices for microservices and clean architecture. Each service is stateless and can be deployed or scaled individually.

**Justification:**
- **Separation of concerns:** Each service has a clear responsibility (core processing, API gateway/caching, frontend visualization).
- **Technology fit:** FastAPI is used for efficient Python-based geoprocessing, NestJS for scalable API orchestration and caching, and NextJS for a modern frontend experience.
- **Deployment flexibility:** Each repo includes a Dockerfile for containerized deployment, but local validation is streamlined by the orchestrator CLI.

## Service Interaction & Data Flow

1. **NextJS Frontend**: Allows users to input geographic coordinates and visualizes results on a map. Sends requests to the NestJS API.
2. **NestJS API**: Acts as a middleware, validating input, caching results, and forwarding requests to the FastAPI microservice. Handles error management and response formatting.
3. **FastAPI Microservice**: Receives coordinate data, validates it, calculates centroid and bounding box, and returns results in a structured JSON format.

**Error Handling:**
- Each service validates its input and returns clear error messages (400 for invalid data, 401 for authentication, 500 for unexpected errors).
- Error responses and validation logic are documented in each service's README.

**Stateless Design:**
- All services are stateless, with no persistent storage. Caching in NestJS is in-memory and ephemeral.

**Documentation:**
- Each repository contains a README with installation, configuration, endpoints, and usage instructions. The orchestrator README summarizes manual and automated setup for all services.

---

This orchestrator was created to facilitate the validation and testing of the Codebranch microservices locally and quickly. It automates the download, installation, configuration, and startup of the FastAPI, NestJS, and NextJS projects from a single CLI.

Each managed project already includes its own Dockerfile for deployment in production or development environments, but this orchestrator streamlines the process of local validation and testing without the need for containers.


## How to Run

For installation, CLI usage, and manual setup of each managed project, see [HowToRun.md](./HowToRun.md).

---

## Structure

- `orchestrator/main.py`: Main CLI
- `orchestrator/utils.py`: Utilities for repo and service management
- `.env.example`: Example environment variables
- `requirements.txt`: Orchestrator dependencies

## Managed Repositories
- FastAPI: codebranch-fastapi-geoprocesor-ms
- NestJS: codebranch-nestjs-mdw-ms
- NextJS: codebranch-nextjs-geoprocesor-frontend

