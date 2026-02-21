# Autonomous Marketing Optimization Agent System

## Overview

This project is a modular **multi-agent AI system** that autonomously analyzes marketing campaign performance, generates strategy, creates ad variants, and executes optimization actions.

It is designed to demonstrate production-grade AI engineering concepts:

* agent orchestration
* local LLM inference
* retrieval-augmented reasoning (RAG)
* deterministic safeguards
* execution tracing
* parallel workflows
* cached inference

---

## Architecture

```
Data → Analyst → Memory → Strategist
                          ├── Copywriter
                          └── Optimizer
```

System layers:

| Layer  | Responsibility          |
| ------ | ----------------------- |
| Agents | reasoning + decisions   |
| Memory | past campaign knowledge |
| Tools  | external integrations   |
| Graph  | orchestration           |
| UI     | monitoring + control    |

---

## Agent Roles

| Agent      | Function                          |
| ---------- | --------------------------------- |
| Analyst    | Diagnoses campaign performance    |
| Memory     | Retrieves relevant past learnings |
| Strategist | Generates optimization plan       |
| Copywriter | Produces ad creatives             |
| Optimizer  | Executes changes                  |

---

## Tech Stack

| Component     | Tool                 |
| ------------- | -------------------- |
| Language      | Python               |
| Orchestration | LangGraph            |
| LLM           | Ollama (local Phi-3) |
| Embeddings    | SentenceTransformers |
| Vector DB     | FAISS                |
| UI            | Streamlit            |
| Deployment    | Local runtime        |

---

## Key Features

### Multi-Agent Reasoning

Each agent has a dedicated role and structured state inputs.

### Local AI Execution

Runs entirely offline using local models.

### Parallel Execution

Independent agents run concurrently to reduce latency.

### Memory-Augmented Decisions

Agents retrieve prior campaign insights before planning.

### Deterministic Safety Layer

Rules override LLM decisions when necessary.

### Execution Traceability

Live timeline shows agent execution order.

### Intelligent Caching

Repeated runs with identical inputs return instantly.

---

## Project Structure

```
marketing-agent/
│
├── agents/
├── tools/
├── memory/
├── workflows/
├── eval/
├── dashboard.py
├── main.py
└── state.py
```

---

## Running The System

Activate environment:

```
source venv/bin/activate
```

Launch dashboard:

```
python -m streamlit run dashboard.py
```

---

## Example Output

System returns structured result:

```
Diagnosis → Strategy → Copy → Execution
```

Sample decision:

```
Increase budget 20%
Reason: ROAS < 1.5
```

---

## Design Decisions

**Local LLM instead of API**

> avoids latency, cost, and dependency on external services

**FAISS instead of cloud vector DB**

> simpler deployment + offline capability

**Typed State Graph**

> ensures reliable data flow between agents

**Rule Layer before execution**

> prevents unsafe or illogical actions

---

## Failure Handling

System guards against:

* missing state keys
* empty memory retrieval
* model failures
* invalid outputs

Fallback defaults ensure execution continues.

---

## Performance Optimizations

Implemented:

* parallel agent branches
* cached execution results
* lightweight local model
* minimal prompt sizes

Future improvements:

* node-level caching
* async execution
* streaming outputs
* token usage tracking

---

## Future Work

Planned upgrades:

* reinforcement learning feedback loop
* automated campaign simulations
* multi-campaign optimization
* anomaly detection agent
* budget prediction model

---

## Why This Project Matters

Most AI demos show:

> prompt → response

This system demonstrates:

> perception → reasoning → planning → action → evaluation

That is the core architecture of real autonomous systems.

---

## Author Notes

This project was intentionally built using modular architecture so that:

* agents can be swapped
* models can be replaced
* tools can be extended
* workflows can scale

It is meant to serve as a **foundation framework for autonomous decision systems**, not just a demo.
