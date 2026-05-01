import operator
from operator import itemgetter


data = [
    {"name": "Aman", "age": 21},
    {"name": "Riya", "age": 22},
    {"name": "Rahul", "age": 20}
]


result =  sorted(data,key=lambda x :(x["name"],x["age"]))

print(result)