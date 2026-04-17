from exceptions.base import AppError

try:
    raise AppError("Something went wrong")
except AppError as e:
    print(e)
    print(e.to_dict())