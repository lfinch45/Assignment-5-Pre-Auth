import time
from functools import wraps


def retry(retries=3, delay=10):
    def decorator_retry(func):
        @wraps(func)
        def wrapper_retry(*args, **kwargs):
            for _ in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Error: {e}. Retrying in {delay} seconds...")
                    time.sleep(delay)
            else:
                print(f"Failed after {retries} attempts")
                pass
        return wrapper_retry
    return decorator_retry