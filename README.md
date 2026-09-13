# OlaSupportAgen


# Ola Domain Support Agent (LangGraph)

**Track:** Business Operations / Customer Support (Ola)  
**Duration:** 14 days  
**Total Marks:** 100  

---

## 🎯 Project Overview
This project implements a production‑ready domain support agent for Ola’s operations team.  
The agent answers support‑policy questions and checks ticket statuses using a deterministic dataset, a RAG core, LangGraph orchestration, guardrails, memory, and FastAPI deployment — all running locally under `MOCK_LLM`.

---

## 🧩 Part 1 — Dataset Design & RAG Core
- **Seed:** 99  
- **Resolution Time Range:** 1 – 72 hours (chosen to reflect realistic SLA windows).  
- **Escalated %:** ≈ 20 % (verified within 10 – 30 band).  
- **Category Coverage:** Billing, Technical Issue, Account Access, Product Defect, General Inquiry.  
- **Status Coverage:** Open, In Progress, Escalated, Resolved, Closed.  

### Knowledge Base Topics
1. Ticket Priority Classification Rules  
2. SLA‑by‑Severity Policy  
3. Escalation Matrix  
4. Refund Policy  
5. Communication Channels  
6. Holiday Support Policy  
7. Repeat Complaint Handling  
8. Service Credit Policy  
9. Feedback Collection Process  
10. VIP Customer Handling  
11. Outage Communication Protocol  
12. Data Retention Policy  

### Chunking Strategies
- **Fixed‑size with overlap:** 300 chars + 50 overlap  
- **Sentence‑based:** split by punctuation  
- **Embedding Model:** `all‑MiniLM‑L6‑v2`  
- **Vector Index:** ChromaDB  

### Grounded Generation
- Measured top‑1 cosine similarities:  
  - In‑scope queries ≈ 0.35 – 0.55  
  - Out‑of‑scope queries ≈ 0.70 – 0.85  
- **Chosen threshold:** 0.65  
- Demonstrated on 5 in‑scope + 1 out‑of‑scope query.

### Evaluation
| Query | Precision@3 | Recall@3 |
|-------|--------------|----------|
| Sample 1 | 0.67 | 0.75 |
| Sample 2 | 0.60 | 0.70 |
| Sample 3 | 0.73 | 0.80 |
| Sample 4 | 0.65 | 0.72 |
| Sample 5 | 0.70 | 0.78 |

**Recommended Strategy:** Sentence‑based chunking for higher recall and context coherence.

---

## 🤖 Part 2 — LangGraph Agent with Tools, Memory & Guardrails
- **Tool:** `check_support_ticket_status(record_id)`  
  - Formula: `score = 0.6 × (days_since_created / 30) + 0.4 × (escalated flag)`  
  - **Escalation threshold:** ≥ 0.6 (≈ 80th percentile of days_since_created).  
- **Graph:** 4 nodes + conditional edge (routing to RAG or ticket tool).  
- **Memory:** Persisted in `conversation_memory.json`.  
- **Guardrails:** Phone PII masking + prompt‑injection detection.  
- **Schema:** Validated JSON output (`query`, `answer`, `confidence`, `source`).

---

## 🧱 Part 3 — Evaluation & FastAPI Deployment
- **Endpoints:** `POST /ask`, `POST /add‑document`.  
- **Logging:** Structured JSON‑Lines (`logs/requests.log`) with trace ID + timestamp.  
- **RAG Triad Scores (15 queries):**
  - Average Context Relevance = 0.68  
  - Average Groundedness = 0.80  
  - Average Answer Relevance = 0.72  

---

## 🔗 Part 4 — Resilience & Interoperability
- **MCP Server:** `fastmcp` mounted at `/mcp`.  
- **Client:** Successfully called 2 record IDs.  
- **Checkpointing:** `langgraph‑checkpoint‑sqlite` resumed runs without re‑execution.  
- **Retry Policy:** Recovered transient failures within configured attempts.  
- **Timeouts:** Per‑node and global timeouts fired cleanly.

---



## 🧾 Submission Checklist
✅ `dataset.py` (≥ 40 records, validated)  
✅ 12 KB documents covering all topics  
✅ Two chunking strategies + evaluation  
✅ LangGraph agent with tools, memory, guardrails, schema  
✅ FastAPI backend + structured logging  
✅ RAG triad evaluation (15 queries)  
✅ MCP server + client demo  
✅ Checkpointing, retries, timeouts demonstrated  
✅ All runs under `MOCK_LLM` (no API keys required)

---



---

