import json
import os

class JSONStorage:
    """Concrete implementation of StorageInterface for JSON storage."""

    def __init__(self, file_path="data.json"):
        self.file_path = file_path

    def save(self, data: list[dict]):
        """Save scraped data to a JSON file."""
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)

    def load(self) -> list[dict]:
        """Load existing data from a JSON file."""
        if os.path.exists(self.file_path):
            with open(self.file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        return []
