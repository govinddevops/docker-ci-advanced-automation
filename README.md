# CI Advanced - DockerHub Auto Push

This project automates the Docker build and push process using GitHub Actions with unique Git SHA tagging.

## Features
- Automatic Docker Image Build
- Unique Tagging using Commit SHA
- Secure Push to DockerHub via Secrets

## Project Structure
- `app.py`: Flask Application
- `Dockerfile`: Container Configuration
- `.github/workflows/docker-ci-advanced.yml`: CI Pipeline logic

## How it works
1. Code push to `main` branch triggers the workflow.
2. GitHub Actions logs into DockerHub using secrets.
3. Image is built and tagged with the first 7 characters of Git SHA.
4. Image is pushed to DockerHub repository.
