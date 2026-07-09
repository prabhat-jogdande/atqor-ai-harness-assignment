# AI Harness - NLP to SQL

## Overview

An AI-powered Natural Language to SQL application built using a modular AI Harness architecture.

The application converts natural language questions into SQL queries, executes them on the database, validates generated SQL, applies guardrails, and summarizes results using an LLM.

---

## Features

- Natural Language to SQL
- SQL Validation
- Prompt Versioning
- Few-shot Retrieval
- Conversation Memory
- Input Processing
- Guardrails
- Role Based Access
- PII Masking
- Feedback Collection
- Logging & Observability
- FastAPI REST API
- Docker Support
- Azure Ready Architecture

---

## Project Structure

```text
src/
│
├── api/
├── cloud/
├── config/
├── harness/
├── nlp_to_sql/
├── pipeline/
│
schema/
prompts/
evaluation/
docs/
data/
logs/
```

---

## Technology Stack

| Layer | Technology |
|--------|------------|
| Backend | FastAPI |
| Database | SQLite |
| LLM | AWS Bedrock (Azure Ready) |
| Embeddings | Sentence Transformers |
| Vector Search | FAISS |
| Validation | sqlglot |
| Container | Docker |

---

## API Endpoints

### POST /query

Generate SQL and execute.

### POST /feedback

Store user feedback.

---

## Run

```bash
pip install -r requirements.txt

uvicorn src.api.main:app --reload
```

Swagger

```
http://127.0.0.1:8000/docs
```

---

## Docker

```bash
docker build -t nl2sql .

docker run -p 8000:8000 --env-file .env nl2sql
```

---

## Future Azure Migration

Current implementation uses:

- AWS Bedrock
- SQLite
- Local JSON
- FAISS

Production deployment will use:

- Azure OpenAI
- Azure SQL
- Azure AI Search
- Azure Blob Storage
- Azure Redis
- Azure Application Insights

---

## Author

Prabhat Jogdande
