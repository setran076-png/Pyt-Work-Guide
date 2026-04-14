import time
import random
from functools import wraps

class CircuitBrokenError(Exception): pass
class FlakyNetworkError(Exception): pass

def retry(max_attempts=3, base_delay=1.0, exceptions=(Exception,)):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == max_attempts - 1:
                        raise
                    jitter = random.uniform(0.1, 0.5)
                    sleep_time = (base_delay * (2 ** attempt)) + jitter
                    print(f"Failed. Retrying in {sleep_time:.2f}s...")
                    time.sleep(sleep_time)
        return wrapper
    return decorator

if __name__ == "__main__":
    attempts_made = 0

    @retry(max_attempts=4, base_delay=0.5, exceptions=(FlakyNetworkError,))
    def flaky_api_call():
        global attempts_made
        attempts_made += 1
        print(f"Attempting API call... (Attempt {attempts_made})")
        if attempts_made < 3:
            raise FlakyNetworkError("Connection timed out!")
        return "SUCCESS!"

    start = time.time()
    result = flaky_api_call()
    duration = time.time() - start

    assert result == "SUCCESS!"
    assert attempts_made == 3
    print(f"Completed in {duration:.2f} seconds")