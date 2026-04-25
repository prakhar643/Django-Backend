products = [
    {"name": "Laptop", "price": 75000, "category": "Electronics", "rating": 4.5, "in_stock": True},
    {"name": "Phone", "price": 30000, "category": "Electronics", "rating": 4.2, "in_stock": True},
    {"name": "Shoes", "price": 2000, "category": "Fashion", "rating": 3.8, "in_stock": False},
    {"name": "Watch", "price": 5000, "category": "Accessories", "rating": 4.0, "in_stock": True},
    {"name": "Headphones", "price": 1500, "category": "Electronics", "rating": 4.3, "in_stock": True},
]

filter_products = filter(
    lambda p: p["in_stock"] and p["category"] == "Electronics",products
)

mapped_products = map(
    lambda p : {
        "name" : p["name"],
        "discounted_price" : round(p["price"]*0.9,2)

    },filter_products
)

sorted_products = sorted(
    mapped_products,
    key=lambda p: p["discounted_price"]
)

for product in sorted_products:
    print(product)