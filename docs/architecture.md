# AI Harness Architecture

## Overview

The system converts natural language business questions into executable SQL queries using a modular AI Harness architecture.

The solution is cloud-ready and supports both AWS and Azure through a provider abstraction layer. The current implementation is fully integrated with Azure OpenAI, Azure SQL Database, and Azure Blob Storage.

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

             LLM Provider Abstraction

         AWS Bedrock / Azure OpenAI

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

          SQLite / Azure SQL Database

                         │

                         ▼

                 Business Summary

                  Azure OpenAI

                         │

                         ▼

                    JSON Response
```

---

# Project Modules

## API Layer

Handles REST API requests.

Responsible for

- Request validation
- Response generation
- Session management

---

## Input Processor

Responsible for

- Input sanitization
- Intent classification
- Ambiguity detection

---

## Prompt Manager

Responsible for

- Prompt versioning
- Dynamic prompt construction
- Schema injection
- Business dictionary
- Few-shot examples
- Conversation history

---

## Retrieval Layer

Current

- Local Few-shot Retriever

Future

- Azure AI Search

---

## LLM Layer

Supported Providers

- Azure OpenAI (Primary)
- AWS Bedrock

Responsibilities

- SQL Generation
- Business Summary Generation

---

## SQL Validator

Ensures

- Valid SQL
- Read-only execution
- Prevents dangerous statements

---

## Guardrails

Responsible for

- Role-Based Access Control (RBAC)
- PII masking

---

## Query Executor

Supported Databases

- SQLite
- Azure SQL Database

---

## Feedback Layer

Stores

- User feedback
- Corrected SQL
- Future improvements

---

## Observability

Tracks

- Trace ID
- Request latency
- Application logs

Future

- Azure Application Insights

---

# Azure Services Used

| Service | Purpose |
|----------|----------|
| Azure OpenAI | SQL generation & summarization |
| Azure SQL Database | Execute business queries |
| Azure Blob Storage | Store prompts, schema and metadata |
| Azure AI Search | Prepared for semantic retrieval (future integration) |

---

# Provider Abstraction

| Component | Supported Providers |
|-----------|---------------------|
| LLM | AWS Bedrock / Azure OpenAI |
| Database | SQLite / Azure SQL |

---

# Security

- SQL Validation
- Read-only Queries
- RBAC
- PII Masking
- Environment Variables

---

# Future Improvements

- Azure AI Search Vector Index
- Azure Key Vault
- Azure Application Insights
- Azure Managed Identity
- Azure Redis Cache
- Streaming Responses
- Prompt A/B Testing
- Query Cache
- Retry Logic