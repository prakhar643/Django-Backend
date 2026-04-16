import csv
from pathlib import Path


csv_file = Path(__file__).with_name("random.csv")

with csv_file.open("r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        name = row.get("name")
        age = row.get("age")
        email = row.get("email")

        if not name or not age or not email:
            print("Missing data in row:", row)
        else:        
            print(f"Name: {name}, Age: {age}, Email: {email}")
            

