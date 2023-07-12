# import math

# help(math)
# dir(math) -math에 담겨 있는...것들
# terminal에 less 쓰는 이유는 뭐임...->맥이라서...?

# n = int(input("enter: "))
# res = math.factorial(n)
# print(f"{n}!={res}")


from math import factorial as ft  # pandas 이용할 때 주로

n = int(input("enter: "))
res = ft(n)
print(f"{n}!={res}")
