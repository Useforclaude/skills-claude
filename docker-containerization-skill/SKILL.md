---
name: docker-containerization-skill
description: Master Docker containerization and orchestration for production deployments. Use for Dockerfile creation, docker-compose, multi-stage builds, container optimization, Docker networking, volumes, Kubernetes basics, container security, CI/CD integration, microservices deployment, and production-ready containerization strategies. Also use for Thai keywords (Docker, container, Kubernetes, K8s, deploy, ปรับใช้, คอนเทนเนอร์).
---

# Docker Containerization Skill

> **Master Docker containerization and orchestration for production-ready deployments**

## Table of Contents

1. [Docker Fundamentals](#docker-fundamentals)
2. [Dockerfile Best Practices](#dockerfile-best-practices)
3. [Multi-Stage Builds](#multi-stage-builds)
4. [Docker Compose](#docker-compose)
5. [Container Networking](#container-networking)
6. [Volumes and Persistence](#volumes-and-persistence)
7. [Container Security](#container-security)
8. [Kubernetes Basics](#kubernetes-basics)
9. [CI/CD Integration](#cicd-integration)
10. [Production Deployment Strategies](#production-deployment-strategies)

---

## Docker Fundamentals

### What is Docker?

**Docker** = Platform for developing, shipping, and running applications in containers

**Container** = Lightweight, standalone, executable package that includes everything needed to run an application (code, runtime, system tools, libraries)

### Docker vs Virtual Machines

```
┌──────────────────────────────────┐   ┌──────────────────────────────────┐
│    Virtual Machines (VMs)        │   │         Docker Containers        │
├──────────────────────────────────┤   ├──────────────────────────────────┤
│  ┌─────┐  ┌─────┐  ┌─────┐      │   │  ┌─────┐  ┌─────┐  ┌─────┐      │
│  │App A│  │App B│  │App C│      │   │  │App A│  │App B│  │App C│      │
│  ├─────┤  ├─────┤  ├─────┤      │   │  ├─────┤  ├─────┤  ├─────┤      │
│  │Libs │  │Libs │  │Libs │      │   │  │Libs │  │Libs │  │Libs │      │
│  ├─────┤  ├─────┤  ├─────┤      │   │  └─────┘  └─────┘  └─────┘      │
│  │Guest│  │Guest│  │Guest│      │   │  ┌─────────────────────────┐    │
│  │ OS  │  │ OS  │  │ OS  │      │   │  │   Docker Engine         │    │
│  └─────┘  └─────┘  └─────┘      │   │  └─────────────────────────┘    │
│  ┌──────────────────────────┐   │   │  ┌─────────────────────────┐    │
│  │      Hypervisor          │   │   │  │      Host OS            │    │
│  └──────────────────────────┘   │   │  └─────────────────────────┘    │
│  ┌──────────────────────────┐   │   │  ┌─────────────────────────┐    │
│  │      Host OS             │   │   │  │    Infrastructure       │    │
│  └──────────────────────────┘   │   │  └─────────────────────────┘    │
└──────────────────────────────────┘   └──────────────────────────────────┘
     Heavyweight (~GBs)                      Lightweight (~MBs)
     Slow startup (~minutes)                 Fast startup (~seconds)
```

---

### Essential Docker Commands

```bash
# Image management
docker build -t myapp:latest .          # Build image from Dockerfile
docker images                           # List images
docker rmi myapp:latest                 # Remove image
docker pull nginx:latest                # Pull image from Docker Hub
docker push myregistry/myapp:latest     # Push image to registry

# Container management
docker run -d -p 8080:80 nginx          # Run container in background
docker ps                               # List running containers
docker ps -a                            # List all containers
docker stop container_id                # Stop container
docker start container_id               # Start container
docker rm container_id                  # Remove container
docker logs container_id                # View logs
docker exec -it container_id bash       # Execute command in container

# Cleanup
docker system prune                     # Remove unused data
docker volume prune                     # Remove unused volumes
docker image prune                      # Remove unused images
```

---

## Dockerfile Best Practices

### Basic Dockerfile Structure

```dockerfile
# Use official base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy dependency files
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 8000

# Define entrypoint
CMD ["python", "app.py"]
```

---

### Optimization Techniques

#### **1. Use Specific Base Images**

**❌ Bad:**
```dockerfile
FROM ubuntu  # ❌ Too large (77 MB)
```

**✅ Good:**
```dockerfile
FROM python:3.11-slim  # ✅ Smaller (47 MB)
FROM python:3.11-alpine  # ✅ Even smaller (17 MB)
```

---

#### **2. Layer Caching (Order Matters!)**

**❌ Bad (Cache Invalidated on Every Code Change):**
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .  # ❌ Copies everything first
RUN pip install -r requirements.txt  # ❌ Re-runs on every code change
CMD ["python", "app.py"]
```

**✅ Good (Leverage Cache):**
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .  # ✅ Copy dependencies first
RUN pip install -r requirements.txt  # ✅ Cached unless requirements.txt changes
COPY . .  # ✅ Copy code last (changes frequently)
CMD ["python", "app.py"]
```

---

#### **3. Minimize Layers**

**❌ Bad (Multiple RUN Commands):**
```dockerfile
RUN apt-get update
RUN apt-get install -y curl
RUN apt-get install -y git
RUN apt-get clean
```

**✅ Good (Single RUN Command):**
```dockerfile
RUN apt-get update && \
    apt-get install -y curl git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
```

---

#### **4. Use .dockerignore**

```
# .dockerignore
__pycache__/
*.pyc
*.pyo
.git/
.env
node_modules/
*.log
.vscode/
.idea/
```

---

### Production Dockerfile (Python FastAPI)

```dockerfile
# Use official Python image
FROM python:3.11-slim as base

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Create non-root user
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY --chown=appuser:appuser . .

# Switch to non-root user
USER appuser

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Run application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## Multi-Stage Builds

### Why Multi-Stage?

**Benefits:**
- ✅ Smaller final image (remove build tools)
- ✅ Separate build and runtime dependencies
- ✅ Better security (fewer packages in production)

### Example: Node.js Application

**❌ Single-Stage (Large Image):**
```dockerfile
FROM node:18
WORKDIR /app
COPY package*.json ./
RUN npm install  # ❌ Includes dev dependencies
COPY . .
RUN npm run build
CMD ["npm", "start"]
# Final image: ~1.2 GB
```

**✅ Multi-Stage (Small Image):**
```dockerfile
# Stage 1: Build
FROM node:18 as builder
WORKDIR /app
COPY package*.json ./
RUN npm ci  # ✅ Clean install
COPY . .
RUN npm run build  # ✅ Build artifacts

# Stage 2: Production
FROM node:18-alpine  # ✅ Smaller base image
WORKDIR /app
COPY --from=builder /app/dist ./dist  # ✅ Copy only build output
COPY --from=builder /app/node_modules ./node_modules
COPY package*.json ./
ENV NODE_ENV=production
CMD ["node", "dist/main.js"]
# Final image: ~200 MB (6x smaller!)
```

---

### Multi-Stage: Python Application

```dockerfile
# Stage 1: Build dependencies
FROM python:3.11-slim as builder
WORKDIR /app
RUN apt-get update && apt-get install -y gcc
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Production
FROM python:3.11-slim
WORKDIR /app
# Copy Python packages from builder
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH
# Copy application
COPY . .
CMD ["python", "app.py"]
```

---

## Docker Compose

### What is Docker Compose?

**Docker Compose** = Tool for defining and running multi-container applications

### Basic docker-compose.yml

```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://postgres:password@db:5432/mydb
    depends_on:
      - db
    volumes:
      - ./app:/app

  db:
    image: postgres:15
    environment:
      POSTGRES_DB: mydb
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: password
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

volumes:
  postgres_data:
```

**Commands:**
```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop all services
docker-compose down

# Rebuild and start
docker-compose up --build

# Execute command in service
docker-compose exec web python manage.py migrate
```

---

### Production docker-compose.yml (Full Stack)

```yaml
version: '3.8'

services:
  # Nginx reverse proxy
  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
      - ./ssl:/etc/nginx/ssl:ro
    depends_on:
      - web
    restart: unless-stopped

  # FastAPI application
  web:
    build:
      context: .
      dockerfile: Dockerfile
    environment:
      DATABASE_URL: postgresql://postgres:${DB_PASSWORD}@db:5432/mydb
      REDIS_URL: redis://redis:6379/0
      SECRET_KEY: ${SECRET_KEY}
    depends_on:
      - db
      - redis
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  # PostgreSQL database
  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_DB: mydb
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    restart: unless-stopped
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5

  # Redis cache
  redis:
    image: redis:7-alpine
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5

volumes:
  postgres_data:
```

---

## Container Networking

### Network Types

**1. Bridge (Default)**
```bash
# Create network
docker network create my-bridge-network

# Run containers in network
docker run -d --name app1 --network my-bridge-network myapp
docker run -d --name app2 --network my-bridge-network myapp

# Containers can communicate via container name
curl http://app1:8000
```

**2. Host (Share Host Network)**
```bash
# Use host network (no port mapping needed)
docker run -d --network host nginx
# Accessible on http://localhost:80
```

**3. None (No Network)**
```bash
# Isolated container
docker run -d --network none myapp
```

---

### Docker Compose Networking

```yaml
version: '3.8'

services:
  frontend:
    image: nginx
    networks:
      - frontend-network

  backend:
    image: myapp
    networks:
      - frontend-network
      - backend-network

  database:
    image: postgres
    networks:
      - backend-network  # Only accessible from backend

networks:
  frontend-network:
  backend-network:
```

---

## Volumes and Persistence

### Volume Types

**1. Named Volumes (Recommended)**
```bash
# Create volume
docker volume create mydata

# Use in container
docker run -v mydata:/app/data myapp

# List volumes
docker volume ls

# Inspect volume
docker volume inspect mydata
```

**2. Bind Mounts (Development)**
```bash
# Mount local directory
docker run -v $(pwd)/app:/app myapp

# Read-only mount
docker run -v $(pwd)/config:/config:ro myapp
```

**3. tmpfs (In-Memory)**
```bash
# Temporary storage (lost on container stop)
docker run --tmpfs /tmp myapp
```

---

### Volume Best Practices

```yaml
version: '3.8'

services:
  db:
    image: postgres:15
    volumes:
      - postgres_data:/var/lib/postgresql/data  # ✅ Named volume for data
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql:ro  # ✅ Bind mount for init script

  app:
    build: .
    volumes:
      - ./app:/app  # ✅ Bind mount for development (hot reload)
      - /app/node_modules  # ✅ Anonymous volume (prevent overwrite)

volumes:
  postgres_data:  # ✅ Declared named volume
```

---

## Container Security

### Security Best Practices

#### **1. Use Non-Root User**

**❌ Bad (Runs as Root):**
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
CMD ["python", "app.py"]  # ❌ Runs as root (UID 0)
```

**✅ Good (Runs as Non-Root):**
```dockerfile
FROM python:3.11-slim
RUN groupadd -r appuser && useradd -r -g appuser appuser
WORKDIR /app
COPY --chown=appuser:appuser . .
USER appuser  # ✅ Switch to non-root user
CMD ["python", "app.py"]
```

---

#### **2. Scan Images for Vulnerabilities**

```bash
# Install Trivy
brew install trivy

# Scan image
trivy image myapp:latest

# Scan and fail on HIGH/CRITICAL
trivy image --severity HIGH,CRITICAL --exit-code 1 myapp:latest
```

---

#### **3. Use Official Images**

**✅ Good:**
```dockerfile
FROM python:3.11-slim  # ✅ Official Python image
FROM nginx:alpine      # ✅ Official Nginx image
FROM postgres:15       # ✅ Official PostgreSQL image
```

**❌ Bad:**
```dockerfile
FROM random-user/python  # ❌ Unknown source
```

---

#### **4. Don't Store Secrets in Images**

**❌ Bad:**
```dockerfile
ENV API_KEY=secret123  # ❌ Hardcoded secret
```

**✅ Good:**
```bash
# Pass secrets at runtime
docker run -e API_KEY=secret123 myapp

# Or use Docker secrets (Swarm/Kubernetes)
docker secret create api_key api_key.txt
```

---

#### **5. Limit Resources**

```bash
# Limit CPU and memory
docker run --cpus=0.5 --memory=512m myapp
```

```yaml
# docker-compose.yml
services:
  web:
    image: myapp
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
        reservations:
          cpus: '0.25'
          memory: 256M
```

---

## Kubernetes Basics

### What is Kubernetes?

**Kubernetes (K8s)** = Container orchestration platform for automating deployment, scaling, and management

### Core Concepts

```
┌─────────────────────────────────────────────────┐
│               Kubernetes Cluster                │
├─────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────┐   │
│  │           Namespace: production         │   │
│  ├─────────────────────────────────────────┤   │
│  │  ┌──────────────────────────────────┐   │   │
│  │  │      Deployment: myapp           │   │   │
│  │  │  ┌────────────┐  ┌────────────┐  │   │   │
│  │  │  │   Pod 1    │  │   Pod 2    │  │   │   │
│  │  │  │ ┌────────┐ │  │ ┌────────┐ │  │   │   │
│  │  │  │ │Container│ │  │ │Container│ │  │   │   │
│  │  │  │ └────────┘ │  │ └────────┘ │  │   │   │
│  │  │  └────────────┘  └────────────┘  │   │   │
│  │  └──────────────────────────────────┘   │   │
│  │                                          │   │
│  │  ┌──────────────────────────────────┐   │   │
│  │  │       Service: myapp-service     │   │   │
│  │  │  (Load Balancer)                 │   │   │
│  │  └──────────────────────────────────┘   │   │
│  └─────────────────────────────────────────┘   │
└─────────────────────────────────────────────────┘
```

---

### Deployment YAML

```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp-deployment
  namespace: production
spec:
  replicas: 3  # Run 3 pods
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
      - name: myapp
        image: myregistry/myapp:latest
        ports:
        - containerPort: 8000
        env:
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: db-secret
              key: url
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "512Mi"
            cpu: "500m"
        livenessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /ready
            port: 8000
          initialDelaySeconds: 5
          periodSeconds: 5
```

---

### Service YAML

```yaml
# service.yaml
apiVersion: v1
kind: Service
metadata:
  name: myapp-service
  namespace: production
spec:
  type: LoadBalancer  # Or ClusterIP, NodePort
  selector:
    app: myapp
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8000
```

---

### Essential kubectl Commands

```bash
# Apply configuration
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

# Get resources
kubectl get pods
kubectl get deployments
kubectl get services

# Describe resource
kubectl describe pod myapp-pod-123

# View logs
kubectl logs myapp-pod-123
kubectl logs -f myapp-pod-123  # Follow logs

# Execute command in pod
kubectl exec -it myapp-pod-123 -- bash

# Scale deployment
kubectl scale deployment myapp-deployment --replicas=5

# Update image
kubectl set image deployment/myapp-deployment myapp=myregistry/myapp:v2

# Delete resources
kubectl delete -f deployment.yaml
kubectl delete pod myapp-pod-123
```

---

## CI/CD Integration

### GitHub Actions - Build and Push Docker Image

```yaml
# .github/workflows/docker.yml
name: Build and Push Docker Image

on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v2

      - name: Log in to Docker Hub
        uses: docker/login-action@v2
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_PASSWORD }}

      - name: Build and push
        uses: docker/build-push-action@v4
        with:
          context: .
          push: true
          tags: |
            myusername/myapp:latest
            myusername/myapp:${{ github.sha }}
          cache-from: type=registry,ref=myusername/myapp:latest
          cache-to: type=inline

      - name: Deploy to production
        run: |
          echo "Deploying to production..."
          # kubectl set image deployment/myapp myapp=myusername/myapp:${{ github.sha }}
```

---

### GitLab CI - Build, Test, Deploy

```yaml
# .gitlab-ci.yml
stages:
  - build
  - test
  - deploy

variables:
  DOCKER_IMAGE: $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA

build:
  stage: build
  image: docker:latest
  services:
    - docker:dind
  script:
    - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
    - docker build -t $DOCKER_IMAGE .
    - docker push $DOCKER_IMAGE

test:
  stage: test
  image: $DOCKER_IMAGE
  script:
    - python -m pytest tests/

deploy:
  stage: deploy
  image: bitnami/kubectl:latest
  script:
    - kubectl set image deployment/myapp myapp=$DOCKER_IMAGE
  only:
    - main
```

---

## Production Deployment Strategies

### 1. Blue-Green Deployment

```
┌────────────────┐
│  Load Balancer │
└───────┬────────┘
        │
   ┌────┴────┐
   │         │
┌──▼──┐   ┌─▼───┐
│Blue │   │Green│
│ v1  │   │ v2  │ ← Deploy new version here
└─────┘   └─────┘
   ↑         │
   │         │ Test v2
   │         │
   └─────────┘ Switch traffic when ready
```

**Kubernetes:**
```bash
# Deploy green (v2)
kubectl apply -f deployment-green.yaml

# Test green
kubectl port-forward svc/myapp-green 8000:80

# Switch traffic (update service selector)
kubectl patch service myapp -p '{"spec":{"selector":{"version":"green"}}}'

# Rollback if needed
kubectl patch service myapp -p '{"spec":{"selector":{"version":"blue"}}}'
```

---

### 2. Canary Deployment

```
┌────────────────┐
│  Load Balancer │
└───────┬────────┘
        │
   ┌────┴────────────┐
   │                 │
   │ 90%         10% │ ← Route small % to new version
   ↓                 ↓
┌─────┐         ┌────────┐
│ v1  │         │  v2    │
│(Stable)       │(Canary)│
└─────┘         └────────┘
```

**Kubernetes (with Istio):**
```yaml
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: myapp
spec:
  hosts:
  - myapp.example.com
  http:
  - match:
    - headers:
        canary:
          exact: "true"
    route:
    - destination:
        host: myapp-v2
      weight: 100
  - route:
    - destination:
        host: myapp-v1
      weight: 90
    - destination:
        host: myapp-v2
      weight: 10  # 10% canary traffic
```

---

### 3. Rolling Update (Default Kubernetes)

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
spec:
  replicas: 10
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 1  # Max 1 pod down during update
      maxSurge: 2        # Max 2 extra pods during update
  template:
    spec:
      containers:
      - name: myapp
        image: myapp:v2
```

**Process:**
```
Initial:  [v1] [v1] [v1] [v1] [v1]

Step 1:   [v1] [v1] [v1] [v1] [v2] ← Deploy v2
Step 2:   [v1] [v1] [v1] [v2] [v2] ← Replace v1
Step 3:   [v1] [v1] [v2] [v2] [v2]
Step 4:   [v1] [v2] [v2] [v2] [v2]
Step 5:   [v2] [v2] [v2] [v2] [v2] ← All v2
```

---

## Quick Reference - Docker Commands

### Dockerfile
```bash
# Build image
docker build -t myapp:latest .

# Build with build args
docker build --build-arg VERSION=1.0 -t myapp:1.0 .

# Build multi-platform
docker buildx build --platform linux/amd64,linux/arm64 -t myapp:latest .
```

### Container Management
```bash
# Run container
docker run -d -p 8080:80 --name mycontainer nginx

# Stop/Start
docker stop mycontainer
docker start mycontainer
docker restart mycontainer

# Remove
docker rm mycontainer
docker rm -f mycontainer  # Force remove running container

# View logs
docker logs mycontainer
docker logs -f mycontainer  # Follow logs
docker logs --tail 100 mycontainer  # Last 100 lines
```

### Docker Compose
```bash
# Start services
docker-compose up -d

# Stop services
docker-compose down

# View logs
docker-compose logs -f web

# Rebuild
docker-compose build
docker-compose up --build

# Execute command
docker-compose exec web python manage.py migrate

# Scale service
docker-compose up -d --scale web=3
```

### Kubernetes
```bash
# Apply configuration
kubectl apply -f deployment.yaml

# Get resources
kubectl get pods
kubectl get deployments
kubectl get services

# Scale
kubectl scale deployment myapp --replicas=5

# Update image
kubectl set image deployment/myapp myapp=myapp:v2

# Rollback
kubectl rollout undo deployment/myapp

# View logs
kubectl logs -f pod/myapp-123

# Delete
kubectl delete -f deployment.yaml
```

---

## Summary: Containerization Checklist

**Dockerfile:**
- [ ] Use specific, minimal base image (alpine/slim)
- [ ] Leverage layer caching (dependencies before code)
- [ ] Use multi-stage builds for production
- [ ] Run as non-root user
- [ ] Add .dockerignore file
- [ ] Include health checks

**Security:**
- [ ] Scan images for vulnerabilities (Trivy)
- [ ] Don't store secrets in images
- [ ] Use official images
- [ ] Limit container resources
- [ ] Keep base images updated

**Production:**
- [ ] Use docker-compose for multi-container apps
- [ ] Implement health checks and readiness probes
- [ ] Use named volumes for persistence
- [ ] Configure logging and monitoring
- [ ] Implement proper deployment strategy (blue-green/canary)
- [ ] Set up CI/CD for automated builds and deployments

---

**Power Level:** Docker containerization mastery + full CODING ULTIMATE STACK = 800/1000 development expertise

---

## 🔧 CODING ULTIMATE STACK: Must Load Together

**This skill is Layer 5: Deployment & Collaboration of THE CODING ULTIMATE STACK system.**

### Same Layer (Deployment & Collaboration - Load All 5):
- `git-safety-skill` - Safe version control, branching strategies
- `automation-workflows-skill` - Workflow automation, batch processing
- `security-best-practices-skill` - OWASP, authentication, security audit
- `document-conversion-skill` - MD → PDF, HTML → PDF, Pandoc

### Auto-Loading Modes:
- **Default Stack (12 skills):** Triggers on "code", "เขียนโค้ด", "programming"
- **Aggressive Stack (20 skills):** Triggers on "architecture", "scalability", "รีแฟคเตอร์"
- **Ultimate Stack (28 skills):** Triggers on "ultimate stack", "production-ready", "ช่วยเต็มที่"

### Pro Workflow:
1. **Novice:** Use this skill alone → Basic implementation
2. **Intermediate:** This + 2-3 same-layer skills → 2-3x quality
3. **Expert:** Full Layer 5 + all layers → Production-grade code

**Power Level:** This skill + full stack = 800/1000 (maximum development expertise)
