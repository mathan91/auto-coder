import os

class ContextManager:
    def __init__(self, base_path="."):
        self.base_path = base_path

    def get_file_content(self, file_path):
        """Retrieves content of a file."""
        # Simple implementation, can be extended to use VectorDB or RAG
        abs_path = os.path.abspath(os.path.join(self.base_path, file_path))
        if os.path.exists(abs_path) and os.path.isfile(abs_path):
            with open(abs_path, 'r') as f:
                return f.read()
        return "File not found."

    def summarize_context(self, context_data):
        """Mock summarization."""
        # In a real app, use an LLM to summarize
        return f"Summary: {context_data[:100]}..."
