# basic human-centric guardrail logic
def is_safe_query(query: str) -> bool:
    # simple keyword blocklist (can be upgraded to NeMo guardrails later)
    unsafe_words = ["hack", "bypass", "ignore previous instructions"]
    for word in unsafe_words:
        if word in query.lower():
            return False
    return True

def sanitize_output(output: str) -> str:
    # ensuring ai doesn't leak sensitive data
    if "API_KEY" in output or "secret" in output.lower():
        return "I cannot provide sensitive information."
    return output
