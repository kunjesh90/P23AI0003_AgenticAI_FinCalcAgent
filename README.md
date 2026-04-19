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
