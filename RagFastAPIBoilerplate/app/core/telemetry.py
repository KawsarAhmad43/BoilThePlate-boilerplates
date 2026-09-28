from langchain.callbacks.base import BaseCallbackHandler
import time

class AnalyticsCallback(BaseCallbackHandler):
    # custom callback to track speed and token cost
    def __init__(self):
        self.start_time = 0
        
    def on_llm_start(self, serialized, prompts, **kwargs):
        self.start_time = time.time()
        print("\n[TELEMETRY] LLM Started...")
        
    def on_llm_end(self, response, **kwargs):
        print(f"[TELEMETRY] Finished in {time.time() - self.start_time:.2f}s")
        if response.llm_output and "token_usage" in response.llm_output:
            print(f"[TELEMETRY] Tokens: {response.llm_output['token_usage']}")
