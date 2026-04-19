# P23AI0003_AgenticAI_FinCalcAgent

**When Small Beats Large: An Agentic AI Symbolic-Neural Framework for Precise Financial Calculation, Demonstrated on Fixed Deposits**

**Author:** Kunjesh Parekh (P23AI0003)

---

## Overview

**FinCalcAgent** is a hybrid symbolic-neural multi-agent framework for precise fixed deposit (FD) calculation and policy-aware financial question answering.

The core idea is simple:

> **LLMs handle language. Python handles arithmetic.**

This separation is important because large language models are strong at understanding user intent, but unreliable at exact financial computation. FinCalcAgent solves this by routing every query through specialized agents and deterministic Python engines instead of letting the model do the math directly.

The system is designed for three types of queries:

- **Calculation queries** for exact FD computation.
- **RAG rules queries** for RBI and policy-grounded responses.
- **Rate query questions** for structured interest-rate lookup.

FinCalcAgent is built to reduce arithmetic hallucination, improve transparency, and support reproducible financial AI research.

## Architecture

![FinCalcAgent Architecture](docs/assets/fincalcagent_architecture.jpg)

```text
|---------------------- USER QUERY ----------------------|
|
v
|------------- ROUTER AGENT : Llama-4-Scout-17B --------|
|
---------------------------------------------------
| | |
v v v

+================ ROUTE A : CALCULATION ================+
| Agent 1 : Parameter Extractor |
| LLM -> Structured JSON |
| |
| Python Validator |
| Field Check - No LLM |
| |
| Agent 2 : Calculation Planner |
| LLM -> Plan JSON |
| |
| Agent 3/4 : Python Calculation Engine |
| All Arithmetic - No LLM |
| |
| Agent Explainer |
| Narration Only - No Arithmetic |
| |
| Engines: Tenure | Rolling | Rate | Compound | TDS |
| Premature Withdrawal |
+======================================================+

+================== ROUTE B : RAG RULES ===============+
| FAISS Index |
| all-MiniLM-L6-v2 | Top 3 |
| |
| Agent Rules |
| Policy Narration |
| No Arithmetic |
+======================================================+

+================ ROUTE C : RATE QUERY ================+
| File Extractor |
| LLM -> Filter Params |
| |
| Python Rate Card Filter |
| Exact Slab Match |
| |
| Rate Formatter |
| LLM -> Markdown Table |
+======================================================+

\ | /
\ | /
\ | /
-------------------------------------------
|
v

|-------------------- RESPONSE TO USER ----------------|
```
The architecture uses a router-first design with three specialized routes: calculation, RAG rules, and rate query. Deterministic Python engines handle all arithmetic, while LLMs are restricted to extraction, planning, policy narration, and formatting.

