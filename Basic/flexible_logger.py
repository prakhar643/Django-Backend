# import datetime

# def flexible_logger(*args, level="INFO", **kwargs):
#     parts = []
#     timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     print(f"[{level}] {timestamp}")
#     if "attempts" in kwargs:
#         parts.append(f"attempts={kwargs['attempts']}")
#         # print(f"Attempts: {kwargs['attempts']}")
#     for msg in args:
#         parts.append(msg)      

#     for key, value in kwargs.items():
#         parts.append(f"{key}={value}")

#         # for i in range(len(parts)):
#         #     print(parts[i])
#     print(", ".join(parts))

import datetime

def flexible_logger(*args, level="INFO", **kwargs):
    parts = []
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    parts.append(f"[{level}] {timestamp}")

    # messages
    for msg in args:
        parts.append(msg)

    # metadata
    for key, value in kwargs.items():
        parts.append(f"{key}={value}")

    # SINGLE OUTPUT
    print(" | ".join(parts))

attempts = 3

flexible_logger(
    "Login failed",
    "Retry...",
    attempts = attempts,
    level="Error",
    user="Prakhar"
)