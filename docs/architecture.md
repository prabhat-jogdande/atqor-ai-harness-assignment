# AI Harness Architecture

## Overview

The system converts natural language business questions into executable SQL queries using a modular AI Harness architecture.

The design is cloud agnostic and currently runs locally using SQLite and AWS Bedrock. The architecture is designed for seamless migration to Azure AI services.

---

# High Level Architecture

```
                        User

                         │

                         ▼

                  FastAPI REST API

                         │

                         ▼

                 Input Processor

        - Sanitization
        - Intent Detection
        - Ambiguity Detection

                         │

                         ▼

                  Prompt Builder

        - Prompt Versioning
        - Schema Metadata
        - Business Dictionary
        - Few-shot Retrieval
        - Conversation Memory

                         │

                         ▼

                      LLM

         Current : AWS Bedrock

         Future : Azure OpenAI

                         │

                         ▼

                  SQL Validator

                         │

                         ▼

                   Guardrails

        - RBAC
        - PII Masking

                         │

                         ▼

                  Query Executor

                      SQLite

                         │

                         ▼

                  Result Summary

                         │

                         ▼

                    JSON Response

```

---

# Project Modules

## API Layer

Handles incoming REST requests.

Responsible for

- Request validation
- Response generation
- Session handling

---

## Input Processor

Performs

- Input sanitization
- Intent classification
- Ambiguity detection

---

## Prompt Manager

Responsible for

- Prompt Versioning
- Dynamic Prompt Construction
- Schema Injection
- Few-shot Examples

---

## Retrieval Layer

Uses Sentence Transformer embeddings and FAISS to retrieve similar examples.

Future replacement

Azure AI Search

---

## LLM Layer

Current

AWS Bedrock

Future

Azure OpenAI GPT-5

---

## SQL Validator

Ensures

- Valid SQL
- No dangerous statements
- Read-only execution

---

## Guardrails

Responsible for

- Role Based Access Control
- PII Masking

---

## Query Executor

Executes SQL against SQLite.

Future

Azure SQL Database

---

## Feedback Layer

Stores

- User Rating
- Corrected SQL
- Future Training Data

---

## Observability

Tracks

- Trace ID
- Latency
- Pipeline Logs

Future

Azure Application Insights

---

# Azure Migration

| Current | Azure |
|----------|--------|
| AWS Bedrock | Azure OpenAI |
| SQLite | Azure SQL |
| JSON | Azure Blob Storage |
| FAISS | Azure AI Search |
| Local Memory | Azure Redis |
| Local Logs | Azure Application Insights |

---

# Security

- SQL Validation
- RBAC
- PII Masking
- Environment Variables
- Read-only Queries

---

# Future Improvements

- Streaming Responses
- Query Cache
- Cost Tracking
- Retry Logic
- Multi-turn SQL Planning
- Prompt A/B Testing