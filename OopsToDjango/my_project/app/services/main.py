# from services.order_service import CreateOrderService

from .user_service import CreateUserService

# create user
user = CreateUserService("alice").run()
print(user)

# create order
# order = CreateOrderService("laptop", 2).run()
# print(order)
