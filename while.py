# while문 사용해서 팩토리얼...

n = 5
res = 1

# while n > 0:
#     res *= n
#     n -= 1
#     print(f"res: {res},n: {n}")
# print(res)

# print(res)


while True:  # true라는 컨디션이 항상 있어야 함
    if n == 0:
        break

    res *= n
    n -= 1

print(res)
