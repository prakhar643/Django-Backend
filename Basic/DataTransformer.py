def transformer(users):
    ls = list(
        map(
            lambda user: user["name"],
            filter(lambda user: user["age"] >= 18, users)
        )
    )

    print(ls)


users = [
    {"name": "Aman", "age": 22, "active_status": "Online"},
    {"name": "Ravi", "age": 18, "active_status": "Online"},
    {"name": "Neha", "age": 25, "active_status": "Online"}
]

transformer(users)