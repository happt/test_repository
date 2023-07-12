data = [1, 2, 3, 4]

new_list = []
for i in data:
    new_list.append(i**2)  # append는 memory를 많이 잡아먹어버림

print(new_list)

# comprehension 하면 더 빠르게 ㄱㄴ
new_list_2 = [(x**2) for x in data]
print(new_list_2)

new_list_3 = [f"M{x}" for x in data]

# new_list_3=["M"+str(x) for x in data]
print(new_list_3)
