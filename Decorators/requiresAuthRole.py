from functools import wraps

def requires_auth(role):              # 1. outer function (takes role)
    def decorator(func):              # 2. actual decorator
        @wraps(func)
        def wrapper(*args, **kwargs): # 3. wrapper
            print(f"Required role: {role}")
            
            # simulate current user role
            user_role = args[0] if args else None
            
            if user_role != role:
                print("Access Denied ❌")
                return None
            
            print("Access Granted ✅")
            return func(*args, **kwargs)
        
        return wrapper
    return decorator


@requires_auth("user")
def auth(role):
    return f"Welcome {role}"

print(auth("user"))