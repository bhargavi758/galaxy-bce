# Galaxy BCE

A Flask-based web application deployed on Kubernetes with production-grade configuration.

## Overview

Galaxy BCE is a simple Flask application designed to demonstrate production-ready Kubernetes deployment patterns including high availability, scalability, security, and multi-tenant awareness.

## Features

- Flask web application with health check and API endpoints
- Containerized with Docker
- Kubernetes deployment with high availability (3 replicas)
- Horizontal Pod Autoscaling (3-10 replicas)
- Shared ingress with TLS
- Namespace isolation for multi-tenant environments
- Production security best practices

## Quick Start

### Prerequisites

- Docker
- Kubernetes cluster (1.24+)
- kubectl configured
- kustomize (or use `kubectl apply -k`)

### Build Image

```bash
docker build -t galaxy-bce:1.0.0 .
```

### Deploy to Kubernetes

```bash
# Apply all manifests
kubectl apply -k k8s/

# Verify deployment
kubectl get all -n galaxy-web

# Check pod status
kubectl get pods -n galaxy-web -l app=galaxy-bce
```

### Access the Application

The application is exposed via ingress at `galaxy-bce.galaxy.local` (configure as needed).

**Endpoints:**
- `GET /` - Returns "Hello World!"
- `GET /health` - Health check endpoint
- `GET /api/dummy` - Dummy API endpoint

## Project Structure

```
galaxy-bce/
├── app.py                    # Flask application
├── requirements.txt          # Python dependencies
├── Dockerfile               # Container definition
├── .dockerignore            # Docker build exclusions
├── README.md                # This file
├── DEPLOYMENT_DOCUMENTATION.md  # Detailed deployment docs
└── k8s/                     # Kubernetes manifests
    ├── namespace.yaml       # Namespace definition
    ├── configmap.yaml       # Application configuration
    ├── deployment.yaml      # Deployment manifest
    ├── service.yaml         # Service manifest
    ├── ingress.yaml         # Ingress manifest
    ├── hpa.yaml             # Horizontal Pod Autoscaler
    ├── pdb.yaml             # Pod Disruption Budget
    └── kustomization.yaml   # Kustomize configuration
```

## Updating Image Version

```bash
# Update kustomization.yaml with new image tag
cd k8s
kustomize edit set image galaxy-bce:1.0.1
cd ..

# Apply updated manifests
kubectl apply -k k8s/
```

## Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run locally
python app.py

# Access at http://localhost:5000
```

## Configuration

### Environment Variables

- `PORT` - Application port (default: 5000)
- `APP_VERSION` - Application version (from ConfigMap)

### Kubernetes Configuration

All Kubernetes configuration is in the `k8s/` directory. Key settings:

- **Namespace**: `galaxy-web`
- **Replicas**: 3 (min), 10 (max via HPA)
- **Resources**: 100m CPU / 128Mi memory (requests), 500m CPU / 256Mi memory (limits)

## Monitoring

### Health Checks

- **Liveness**: `/health` endpoint
- **Readiness**: `/health` endpoint

### View Logs

```bash
kubectl logs -n galaxy-web -l app=galaxy-bce --tail=50 -f
```

### Check HPA Status

```bash
kubectl get hpa -n galaxy-web
```

## Troubleshooting

### Pods Not Starting

```bash
kubectl describe pod -n galaxy-web <pod-name>
```

### Service Not Accessible

```bash
kubectl get endpoints -n galaxy-web galaxy-bce
```

### Ingress Issues

```bash
kubectl describe ingress -n galaxy-web galaxy-bce
```

## Documentation

For detailed deployment documentation, architecture decisions, and rationale, see [DEPLOYMENT_DOCUMENTATION.md](./DEPLOYMENT_DOCUMENTATION.md).
