c = input()
b = c.isalpha()  # true false를 알려줌
# print(c.isalpha())

print(type(b))
if c.isalpha():  # true 값이 나오면
    print(f"{b}, {c}, alphabet")
else:
    print(f"{b}, {c}, not alphabet")
