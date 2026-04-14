from functools import wraps

def decorators(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print(f"Calling {func.__name__} with args: {args} and kwargs: {kwargs}")
        result = func(*args,**kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@decorators
def add(a,b):   
    return a+b

add(5,3)