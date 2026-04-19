from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
BENCHMARK_DIR = DATA_DIR / "benchmark"
RULES_DIR = DATA_DIR / "rules"
RATES_DIR = DATA_DIR / "rates"
GOLDEN_DIR = DATA_DIR / "golden"
OUTPUT_DIR = BASE_DIR / "outputs"

QUESTIONS_FILE = BENCHMARK_DIR / "questions.csv"
GUIDELINES_PDF = RULES_DIR / "Guidelines_pdf.pdf"
INT_RATE_FILE = RATES_DIR / "int_rate_new.xlsx"
GOLDEN_ANSWERS_FILE = GOLDEN_DIR / "goldenans.xlsx"

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")

AVAILABLE_MODELS = {
    "llama_scout": "meta-llama/llama-4-scout-17b-16e-instruct",
    "llama_70b": "llama-3.3-70b-versatile",
    "llama_8b": "llama-3.1-8b-instant",
}

MODEL_CONFIG = {
    "router": AVAILABLE_MODELS["llama_scout"],
    "agent1": AVAILABLE_MODELS["llama_scout"],
    "agent2": AVAILABLE_MODELS["llama_scout"],
    "ragrules": AVAILABLE_MODELS["llama_scout"],
    "agentratequery": AVAILABLE_MODELS["llama_scout"],
    "agentexplainer": AVAILABLE_MODELS["llama_scout"],
    "default": AVAILABLE_MODELS["llama_scout"],
}

def get_model(agent_name: str) -> str:
    return MODEL_CONFIG.get(agent_name, MODEL_CONFIG["default"])
