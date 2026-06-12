# Hadoop Single Node Cluster (Docker)

A complete self-contained Hadoop single-node cluster that runs with Docker only.

## Prerequisites

- Git
- Docker Desktop (Windows/macOS) or Docker Engine + Docker Compose plugin (Linux)

## Quick Start

```bash
git clone https://github.com/nareshkarthigeyan/ml-lab-sem6.git
cd ml-lab-sem6
docker compose up -d
```

## Verify Cluster

- HDFS NameNode UI: http://localhost:9870
- YARN ResourceManager UI: http://localhost:8088

Check running daemons:

```bash
docker exec -u hadoop -it hadoop-single-node bash -lc "hdfs dfsadmin -report | head -n 20"
docker exec -u hadoop -it hadoop-single-node yarn node -list
```

## Basic HDFS Smoke Test

```bash
docker exec -it hadoop-single-node bash -lc "hdfs dfs -mkdir -p /tmp/hadoop-test"
docker exec -it hadoop-single-node bash -lc "hdfs dfs -ls /tmp"
```

## Stop Cluster

```bash
docker compose down
```

To also remove persisted HDFS data volumes:

```bash
docker compose down -v
```
