import time
import threading 

class RateLimiter:
    def __init__(self, max_per_second: int):
        self.max_per_second = max_per_second
        self.delay_between_requests = 1.0 / max_per_second
        self.queue = []
        self.last_run_time = 0.0

    def add_request(self, payload: str) -> None:
        self.queue.append(payload)
    def process_queue(self) -> None:
        while len(self.queue) > 0:
            task = self.queue.pop(0)

            now = time.monotonic()
            elapsed = now - self.last_run_time

            if elapsed < self.delay_between_requests:
                time.sleep(self.delay_between_requests - elapsed)

            print(f"[{time.strftime('%X')}] Processed: {task}")
            self.last_run_time = time.monotonic()
if __name__ == "__main__":
    limiter = RateLimiter(max_per_second=2)

    print("Simulating burst of 5 requests...")
    for i in range(5):
        limiter.add_request(f"Task_{i}")

    start_time = time.time()
    limiter.process_queue()
    end_time = time.time()

    duration = end_time - start_time

    print(f"Queue processed in {duration:.2f} seconds.")
    assert duration >= 2.0