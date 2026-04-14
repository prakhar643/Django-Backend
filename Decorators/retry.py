from functools import wraps

def retry(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(n):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {i+1} failed: {e}")
            raise Exception(f"Function failed after {n} attempts")
        return wrapper
    return decorator


@retry(3)
def divide(a, b):
    return a / b
    