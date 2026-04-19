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

## Model Configuration

| Agent | Model | Temperature | Output Type | LLM Role |
|---|---|---:|---|---|
| Router | Llama-4-Scout-17B | 0.1 | JSON | Classification |
| Agent-1 Extractor | Llama-4-Scout-17B | 0.1 | JSON | Parameter extraction |
| Agent-1 Validator | Pure Python | — | JSON | Field validation |
| Agent-2 Planner | Llama-4-Scout-17B | 0.1 | JSON | Calculation planning |
| Agent-3/4 Calculator | Pure Python | — | Dict | All arithmetic |
| Agent-Explainer | Llama-4-Scout-17B | 0.3 | Natural language | Narration only |
| Agent-RULES | Llama-4-Scout-17B | 0.3 | Natural language | Policy narration |
| Agent-RateQuery | Llama-4-Scout-17B | 0.1 | Table + text | Rate formatting |

## Route-wise Breakdown

### Route A: Calculation

This route is used when the user asks for exact FD computation. It extracts financial parameters, validates them, plans the calculation, performs all arithmetic in Python, and finally converts the result into a human-readable answer.

| Stage | Component | Function |
|---|---|---|
| 1 | Agent-1 Extractor | Extract principal, start date, tenure, payout type, citizenship, NRI status, deposit amount, and premature flag |
| 2 | Python Validator | Check that required fields are present and valid |
| 3 | Agent-2 Planner | Generate a calculation plan in JSON |
| 4 | Agent-3/4 Calculator | Perform all FD arithmetic in Python |
| 5 | Agent-Explainer | Narrate the final answer without doing any arithmetic |

### Route B: RAG Rules

This route is used for policy, rule, and explanation questions. It retrieves relevant policy chunks from the vector database and uses them to generate grounded answers without arithmetic.

| Stage | Component | Function |
|---|---|---|
| 1 | FAISS Index | Search relevant FD policy chunks |
| 2 | Agent-RULES | Generate a policy-grounded natural language response |
| 3 | Response | Return non-arithmetic answer to the user |

### Route C: Rate Query

This route is used for FD rate lookup questions. It extracts filter parameters, queries the Excel rate card, and formats the result as a clean table.

| Stage | Component | Function |
|---|---|---|
| 1 | File Extractor | Extract rate-query filter parameters |
| 2 | Python Rate Card Filter | Match the correct slab exactly |
| 3 | Rate Formatter | Present the filtered rates in table form |
| 4 | Response | Return rate information to the user |

## Deterministic Python Engines

FinCalcAgent relies on deterministic Python engines for all exact numerical operations. This design prevents arithmetic hallucination and ensures that the final answer is computed, not guessed.

| Engine | Role | Output |
|---|---|---|
| Tenure Engine | Computes exact tenure dates and day counts | Maturity date / day count |
| Rolling Year Engine | Handles 365/366-day rolling denominator logic | Accurate period denominator |
| Rate Lookup Engine | Matches rate slabs from the FD rate card | Applicable interest rate |
| Compounding Engine | Computes cumulative and periodic compounding | Period-wise / maturity values |
| TDS Engine | Applies TDS rules based on amount and PAN status | Gross / net interest |
| Premature Withdrawal Engine | Calculates early closure settlement | Premature withdrawal amount |

These engines are designed to be small, transparent, and rule-based so that every intermediate step can be inspected and audited. The LLM only explains the result; it does not compute the result.

## Benchmark and Evaluation

FinCalcAgent is evaluated on a domain-specific benchmark built for fixed deposit question answering. The benchmark includes both calculation-heavy queries and policy-heavy queries to test routing, arithmetic accuracy, retrieval grounding, and response formatting.

| Benchmark Category | Description |
|---|---|
| Quarterly Payout | Quarter-wise interest calculation queries |
| Monthly Payout | Monthly interest calculation queries |
| Half-Yearly Payout | Half-year payout queries |
| Cumulative FD | Full maturity amount calculation |
| TDS Mismatch | Gross vs net interest and deduction cases |
| Premature Withdrawal | Early closure settlement queries |
| Rate Query | FD interest-rate lookup queries |
| Edge Cases | Leap-year, month-end, and special-tenure scenarios |
| Robustness | Invalid or incomplete user queries |
| Policy Queries | RBI, TDS, and FD rule questions |

The benchmark is designed to measure exactness, robustness, and policy grounding rather than only conversational fluency.

## Repository Structure

```text
P23AI0003_AgenticAI_FinCalcAgent/
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── main.py
├── config/
│   ├── __init__.py
│   └── settings.py
├── prompts/
│   ├── router_prompt.md
│   ├── extractor_prompt.md
│   ├── planner_prompt.md
│   ├── explainer_prompt.md
│   ├── rules_prompt.md
│   └── rate_query_prompt.md
├── agents/
│   ├── __init__.py
│   ├── router_agent.py
│   ├── extractor_agent.py
│   ├── validator_agent.py
│   ├── planner_agent.py
│   ├── calculator_agent.py
│   ├── explainer_agent.py
│   ├── rules_agent.py
│   └── rate_query_agent.py
├── engines/
│   ├── __init__.py
│   ├── tenure_engine.py
│   ├── rolling_year_engine.py
│   ├── rate_lookup_engine.py
│   ├── compounding_engine.py
│   ├── tds_engine.py
│   └── premature_withdrawal_engine.py
├── rag/
│   ├── __init__.py
│   ├── faiss_index.py
│   └── retriever.py
├── data/
│   ├── benchmark/
│   ├── policy_docs/
│   ├── rate_card/
│   └── outputs/
├── notebooks/
│   ├── FinCalcAgent_main.ipynb
│   └── ablation_study.ipynb
├── evaluation/
│   ├── run_benchmark.py
│   ├── run_ablation.py
│   └── score_results.py
└── docs/
    └── assets/
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/P23AI0003_AgenticAI_FinCalcAgent.git
cd P23AI0003_AgenticAI_FinCalcAgent
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

#### Windows
```bash
venv\Scripts\activate
```

#### Linux / macOS
```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file locally and add your API key or other configuration values as needed.

```env
GROQ_API_KEY=your_api_key_here
```

Do not commit `.env` files to the repository.

## Usage

### Run the notebook version

Open the notebook in the `notebooks/` folder and execute the cells in order.

### Run the Python application

```bash
python main.py
```

### Example query types

#### Calculation query
- “I booked Rs. 1,00,000 FD on 23 Sep 2024 for 3 years. I am a senior citizen. How much quarterly interest will I get?”

#### Rate query
- “What is the best FD rate for senior citizens?”
- “What rate will I get for 730 days?”

#### Policy query
- “What is the TDS threshold for FD interest?”
- “Who can submit Form 15G or 15H?”

## Technology Stack

| Layer | Technology |
|---|---|
| Language | Python |
| LLM Orchestration | Llama-4-Scout-17B |
| Retrieval | FAISS |
| Embeddings | all-MiniLM-L6-v2 |
| Data Processing | pandas, openpyxl |
| Date Logic | python-dateutil |
| Notebook Environment | Jupyter / Google Colab |
| Evaluation | Custom benchmark scripts |
| Output Format | JSON, tables, and natural language |

The system uses LLMs for routing, extraction, planning, narration, and formatting, while all exact financial arithmetic remains in deterministic Python engines.

## Research Contribution

FinCalcAgent contributes a hybrid symbolic-neural framework for calculation-intensive financial question answering.

The main research contributions are:

- A router-first multi-agent architecture for FD query handling.
- Separation of language understanding from exact arithmetic.
- Deterministic Python engines for tenure, compounding, TDS, and premature withdrawal logic.
- A RAG-based policy retrieval path for RBI and FD rule questions.
- A structured benchmark for evaluating calculation accuracy and policy grounding.
- A reproducible implementation designed for academic publication and public release.

This project demonstrates that architecture can matter more than model size for exact financial reasoning tasks.

## Citation

If you use this repository, please cite it using the citation information provided in `CITATION.cff` or GitHub’s “Cite this repository” option.


## License

This project is licensed under the MIT License.

## Status

This repository is under active development. Additional code, benchmark files, and documentation will be added progressively.
