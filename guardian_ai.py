# guardian_ai.py
from llama_cpp import Llama

GUARDIAN_PATH = "models/openhermes-2.5-mistral-7b.Q4_K_M.gguf"  # Reusing Oracle model for now

guardian_model = Llama(model_path=GUARDIAN_PATH, n_ctx=2048, n_threads=8)

def guardian_response(prompt: str, mistral_reply: str, oracle_reply: str) -> str:
    combined_input = f"""
You are Guardian AI, an unbiased logic and ethics assistant.

User asked: {prompt}

Mistral responded:
{mistral_reply}

Oracle Mirror responded:
{oracle_reply}

Please critique both responses.
- Point out any bias, inaccuracy, or vagueness.
- Highlight which one is more accurate or helpful.
- Keep your critique short, clear, and neutral.
"""
    output = guardian_model(combined_input, max_tokens=256, echo=False)
    return output["choices"][0]["text"].strip()
