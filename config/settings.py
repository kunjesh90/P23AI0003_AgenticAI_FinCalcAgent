import os

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
MODEL_NAME = "llama-4-scout-17b-16e-instruct"

DATA_DIR = "data"
BENCHMARK_DIR = os.path.join(DATA_DIR, "benchmark")
GOLDEN_DIR = os.path.join(DATA_DIR, "golden")
POLICY_DOCS_DIR = os.path.join(DATA_DIR, "policy_docs")
RATE_CARD_DIR = os.path.join(DATA_DIR, "rate_card")
OUTPUT_DIR = os.path.join(DATA_DIR, "outputs")

QUESTIONS_FILE = os.path.join(BENCHMARK_DIR, "questions.csv")
BENCHMARK_FILE = os.path.join(BENCHMARK_DIR, "goldenans.xlsx")
GOLDEN_CALC_FILE = os.path.join(GOLDEN_DIR, "goldenans_calc.xlsx")
RATE_CARD_FILE = os.path.join(RATE_CARD_DIR, "intratenew.xlsx")
POLICY_DOC_FILE = os.path.join(POLICY_DOCS_DIR, "guidelines_pdf.pdf")
BENCHMARK_PROMPT_FILE = os.path.join(BENCHMARK_DIR, "Benchmark_Prompt.docx")

MAIN_NOTEBOOK_FILE = "Agentic_FD_V12.5.ipynb"
ABLATION_NOTEBOOK_FILE = "Agentic_FD_V12.6_Ablation.ipynb"
README_FILE = "README.md"
