import json
import os
import time

class FeedbackLogger:
    def __init__(self, log_file="feedback_log.jsonl"):
        self.log_file = log_file

    def log_run(self, prompt, result, feedback_score=None, feedback_text=None):
        """Logs a single run with optional feedback."""
        entry = {
            "timestamp": time.time(),
            "prompt": prompt,
            "result": str(result),
            "feedback_score": feedback_score,
            "feedback_text": feedback_text
        }
        self._append_entry(entry)

    def log_preference(self, prompt, chosen, rejected):
        """Logs a DPO preference pair."""
        entry = {
            "timestamp": time.time(),
            "type": "dpo_preference",
            "prompt": prompt,
            "chosen": chosen,
            "rejected": rejected
        }
        self._append_entry(entry)

    def _append_entry(self, entry):
        with open(self.log_file, "a") as f:
            f.write(json.dumps(entry) + "\n")
