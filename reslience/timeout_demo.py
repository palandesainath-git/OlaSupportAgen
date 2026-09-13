import time, concurrent.futures

def slow_task(duration):
    """Simulate a slow node execution."""
    time.sleep(duration)
    return "Completed"

def run_with_timeout(task_duration, timeout):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(slow_task, task_duration)
        try:
            result = future.result(timeout=timeout)
            print(f"✅ Task finished: {result}")
        except concurrent.futures.TimeoutError:
            print(f"⏰ Timeout! Task exceeded {timeout}s limit.")




