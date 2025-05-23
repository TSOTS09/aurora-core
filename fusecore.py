from llama_cpp import llama
from oracle_mirror import oracle_response
from guardian_ai import guardian_response
from dreamweaver import mistral_response

def fusecore_response(prompt: str) -> str:
    mistral_out = mistral_response(prompt)
    oracle_out = oracle_response(prompt)
    guardian_out = guardian_response(prompt, mistral_out, oracle_out)

    return guardian_out
