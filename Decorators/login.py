from functools import wraps



current_user = {"is_authenticated": False}


def login(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if not current_user.get("is_authenticated"):
            raise PermissionError("User not logged in")
        return func(*args,**kwargs)

    return wrapper


@login
def dashboard():
    return "Welcome to dashboard"

current_user["is_authenticated"] = True
print(dashboard()) 
