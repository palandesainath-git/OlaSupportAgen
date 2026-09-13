import json, os

class MemoryManager:
    FILE = "agent/conversation_memory.json"

    def __init__(self):
        if not os.path.exists(self.FILE):
            with open(self.FILE, "w") as f:
                json.dump({}, f)

    def load(self):
        with open(self.FILE) as f:
            return json.load(f)

    def save(self, user_id, history):
        data = self.load()
        data[user_id] = history
        with open(self.FILE, "w") as f:
            json.dump(data, f, indent=2)
