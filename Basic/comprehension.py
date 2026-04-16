num = [1,2,3,4,5]

# square = [x*x for x in num]

# print(square)
# print(type(square))

ans = [x if x%2 == 0 else 0 for x in num]
print(ans)