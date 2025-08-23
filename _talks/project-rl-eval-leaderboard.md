---
title: "RL‑Eval‑Leaderboard | Production‑grade RL evaluation stack"
collection: talks
excerpt: "A production‑ready, containerized leaderboard system for evaluating Reinforcement Learning agents. FastAPI backend, Celery worker evaluating submissions inside locked‑down Docker, real‑time leaderboards via Redis, persistent results in PostgreSQL, and a Gradio frontend. Includes observability (Prometheus, Grafana, Loki)."
type: "System"
permalink:
venue: "Personal Project"
date: Aug 23 '25
location: Online
---

* **Role**: System design and full‑stack implementation

* **What it is**: A secure, reproducible evaluation pipeline and leaderboard for RL agents. Submissions are validated, executed inside an isolated evaluator image, and scored; results stream to the leaderboard in real‑time.

* **Highlights** :    

- **Isolated evaluation**  
  - Celery worker runs agents in a locked‑down Docker image  
  - Deterministic, resource‑bounded execution

- **API + Frontend**  
  - FastAPI for submission, scoring, and leaderboard queries  
  - Gradio frontend for quick browsing and local demos

- **Real‑time leaderboard**  
  - Redis for live updates; PostgreSQL for persistence

- **Observability**  
  - Prometheus metrics, Grafana dashboards, Loki logs  
  - Health endpoints and structured metrics for API/worker

* **Tech Stack**:  
  Python, FastAPI, Celery, Redis, PostgreSQL, Docker, Prometheus, Grafana, Loki, Gradio

**Links**:  
[Live Leaderboard](https://rl-eval-leaderboard.onrender.com)  
[GitHub Repository](https://github.com/YuvrajSingh-mist/RL-Eval-Leaderboard)

Source: [RL‑Eval‑Leaderboard README](https://github.com/YuvrajSingh-mist/RL-Eval-Leaderboard)


