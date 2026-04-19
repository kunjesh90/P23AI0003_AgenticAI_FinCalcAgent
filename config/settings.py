import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

# ---------------------------
# DATA FILE PATHS
# ---------------------------
QUESTIONS_FILE = os.path.join(DATA_DIR, "questions.csv")
GUIDELINES_PDF = os.path.join(DATA_DIR, "Guidelines_pdf.pdf")
INT_RATE_FILE = os.path.join(DATA_DIR, "int_rate_new.xlsx")

# Optional legacy / extra file if you still use calculation RAG anywhere
FD_DOCX_FILE = os.path.join(DATA_DIR, "fd_int.docx")

# ---------------------------
# API KEYS
# ---------------------------
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")

# ---------------------------
# DEFAULT MODEL LIST
# ---------------------------
AVAILABLE_MODELS = {
    "llama_scout": "meta-llama/llama-4-scout-17b-16e-instruct",
    "llama_70b": "llama-3.3-70b-versatile",
    "llama_8b": "llama-3.1-8b-instant",
    "qwen_32b": "qwen/qwen3-32b",
    "gpt_oss_20b": "openai/gpt-oss-20b",
    "gpt_oss_120b": "openai/gpt-oss-120b",
}

# ---------------------------
# ACTIVE MODEL CONFIG
# ---------------------------
MODEL_CONFIG = {
    "router": AVAILABLE_MODELS["llama_scout"],
    "agent1": AVAILABLE_MODELS["llama_scout"],
    "agent2": AVAILABLE_MODELS["llama_scout"],
    "ragrules": AVAILABLE_MODELS["llama_scout"],
    "agentexplainer": AVAILABLE_MODELS["llama_scout"],
    "agentratequery": AVAILABLE_MODELS["llama_scout"],
    "default": AVAILABLE_MODELS["llama_scout"],
}

def get_model(agent_name: str) -> str:
    return MODEL_CONFIG.get(agent_name, MODEL_CONFIG["default"])
