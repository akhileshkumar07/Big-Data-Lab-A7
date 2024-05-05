# FastAPI Monitoring and Dockerization

## Overview

This repository contains a FastAPI application with integrated Prometheus monitoring and Dockerization for seamless deployment and clustering. The goal of this project is to showcase how to enhance a FastAPI application with monitoring capabilities, visualize metrics using Grafana, and dockerize the application to create a scalable cluster.

## Table of Contents

1. **FastAPI Application**: The script `main.py` contains the FastAPI application code, including the integration of Prometheus monitoring hooks and the prediction logic using a pre-trained Keras model.
2. **Dockerization**: The `Dockerfile` and `requirements.txt` files are provided to build a Docker image for the FastAPI application.
3. **Monitoring**: Prometheus and Grafana are used for monitoring the FastAPI application. Prometheus is configured to scrape metrics from the application, and Grafana is set up to visualize those metrics.
4. **Cluster Deployment**: Instructions are provided to deploy a cluster of FastAPI instances using Docker containers and monitor the cluster's health and performance.

## Prerequisites

- Python 3.9 or higher
- Docker: https://docs.docker.com/get-docker/
- Prometheus: https://prometheus.io/docs/prometheus/latest/getting_started/
- Grafana: https://grafana.com/docs/grafana/latest/getting-started/getting-started/

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/fastapi-monitoring-dockerization.git
   ```

2. Install Python dependencies:

   ```bash
   cd fastapi-monitoring-dockerization
   pip install -r requirements.txt
   ```

3. Start Prometheus and Grafana:

   Follow the official documentation to set up and run Prometheus and Grafana. Ensure they are accessible on their default ports (9090 for Prometheus and 3000 for Grafana).

4. Build and run the Docker image:

   ```bash
   docker build -t fastapi-prometheus-app .
   docker run --cpus="1" -p 8000:8000 -p 8001:8001 fastapi-prometheus-app
   ```

5. Access the FastAPI application:

   Open your web browser and navigate to `http://localhost:8000/docs` to access the FastAPI documentation and interact with the application.

6. Visualize metrics in Grafana:

   Configure Grafana to visualize the Prometheus metrics.

7. Deploy a cluster of FastAPI instances:

   Run additional Docker containers with different port mappings to create a cluster of FastAPI instances:

   ```bash
   docker run --cpus="1" -p 8000:8000 -p 8001:8001 fastapi-prometheus-app
   docker run --cpus="1" -p 8002:8000 -p 8003:8001 fastapi-prometheus-app
   # Add more instances as needed
   ```

8. Monitor the cluster:

   Update the Prometheus configuration to scrape metrics from the cluster instances. Modify the Grafana dashboard to visualize metrics from the cluster, providing insights into the cluster's health and performance.

## Docker Commands

- **Build Docker Image**:

  ```bash
  docker build -t fastapi-prometheus-app .
  ```

- **Run Docker Container**:

  ```bash
  docker run --cpus="1" -p 8000:8000 -p 8001:8001 fastapi-prometheus-app
  ```

- **Spin Up Multiple Instances**:

  ```bash
  docker run --cpus="1" -p 8000:8000 -p 8001:8001 fastapi-prometheus-app
  docker run --cpus="1" -p 8002:8000 -p 8003:8001 fastapi-prometheus-app
  # Add more instances as needed
  ```

## Prometheus and Grafana Configuration

- **Prometheus Configuration**: Update the `prometheus.yml` file to include the FastAPI application as a scrape target:

  ```yaml
  scrape_configs:
    - job_name: 'fastapi_app'
      static_configs:
        - targets: ['<your_host>:<port>', '<your_host>:<port>', '<your_host>:<port>']
  ```
