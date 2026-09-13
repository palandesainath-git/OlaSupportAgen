import time, random

def transient_task():
    """Simulate a task that fails twice before succeeding."""
    if transient_task.attempts < 2:
        transient_task.attempts += 1
        raise RuntimeError("Simulated transient failure")
    return "Success after retries"

transient_task.attempts = 0

def exponential_backoff(max_attempts=5, initial_interval=1, max_interval=8, jitter=0.3):
    for attempt in range(max_attempts):
        try:
            result = transient_task()
            print(f"✅ Attempt {attempt+1}: {result}")
            return
        except Exception as e:
            wait = min(initial_interval * (2 ** attempt), max_interval)
            wait += random.uniform(-jitter, jitter)
            print(f"⚠️ Attempt {attempt+1} failed: {e}. Retrying in {wait:.2f}s...")
            time.sleep(wait)
    print("❌ All attempts failed.")
