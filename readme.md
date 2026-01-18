# 🎌 Anime Recommender System – LLMOps Project

An **end-to-end Anime Recommendation System** built using **LLMs (Groq + HuggingFace)** and deployed on **Google Cloud** using **Docker, Kubernetes (Minikube)** with **Grafana Cloud** for observability.

This project demonstrates a **full LLMOps lifecycle** — from model integration and containerization to cloud deployment and monitoring. 

---<img width="1915" height="1022" alt="Anime_recommender_Ss1" src="https://github.com/user-attachments/assets/5d8c7d26-0cc2-40b2-90d2-cfe7e5a61cd7" />


## 🚀 Project Overview

This system recommends anime titles based on user queries using:
- **LLM-powered semantic understanding**
- **Vector-based retrieval**
- **Modern MLOps & LLMOps deployment practices**

The application is:
- Containerized using **Docker**
- Deployed on **Kubernetes (Minikube)** inside a **Google Cloud VM**
- Monitored using **Grafana Cloud (Kubernetes observability)**

---

## 🧠 Architecture Overview

User Query → Retriever → Prompt Template → LLM (Groq / HuggingFace) → Response

Deployment runs on a Google Cloud VM with Docker, Minikube, and Grafana Cloud.

---

## 🛠️ Tech Stack

### AI & LLM
- Groq API
- HuggingFace Models
- LangChain (LCEL-based pipeline)

### Backend & MLOps
- Python
- FastAPI
- Docker
- Kubernetes (Minikube)

### Cloud & DevOps
- Google Cloud VM (Ubuntu 24.04 LTS)
- kubectl
- Helm

### Monitoring
- Grafana Cloud
- Kubernetes Metrics

---

## 📂 Project Structure

```
Anime_Recommender_system_llmops/
├── src/
│   ├── prompt_template.py
│   ├── recommender.py
│   └── utils/
├── pipeline/
│   └── build_pipeline.py
├── llmops-k8s.yaml
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## ☁️ Google Cloud VM Setup

- Machine Type: E2 Standard
- RAM: 16 GB
- Disk: 256 GB
- OS: Ubuntu 24.04 LTS
- HTTP/HTTPS enabled

---

## 🐳 Docker Setup

```bash
docker build -t llmops-app:latest .
```

---

## ☸️ Kubernetes Setup (Minikube)

```bash
minikube start
```

Install kubectl:

```bash
sudo snap install kubectl --classic
```

---

## 🔐 Kubernetes Secrets

```bash
kubectl create secret generic llmops-secrets   --from-literal=GROQ_API_KEY="YOUR_KEY"   --from-literal=HUGGINGFACEHUB_API_TOKEN="YOUR_TOKEN"
```

---

## 🚀 Deploy Application

```bash
eval $(minikube docker-env)
docker build -t llmops-app:latest .
kubectl apply -f llmops-k8s.yaml
kubectl get pods
```

---

## 🌐 Access the Application

Terminal 1:
```bash
minikube tunnel
```

Terminal 2:
```bash
kubectl port-forward svc/llmops-service 8501:80 --address 0.0.0.0
```

Open:
```
http://<EXTERNAL_IP>:8501
```

---

## 📊 Grafana Cloud Monitoring

```bash
kubectl create ns monitoring
```

Deploy Grafana monitoring using Helm with the provided values.yaml.

Verify:
```bash
kubectl get pods -n monitoring
```

---

## 🧹 Cleanup

```bash
minikube delete
docker system prune -a
kubectl delete ns monitoring
```

---

## 📌 Future Improvements

- Fully local open-source LLMs
- MLflow integration
- CI/CD with GitHub Actions
- Kubernetes Ingress
- User feedback loop

---

## 👤 Author

**Rana5884**  
LLMOps | MLOps | Cloud | Kubernetes
