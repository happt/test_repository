n = int(input())

for i in range(n, 0, -1):
    print(i * "*")

for i in range(1, n + 1):
    print((n - i) * " " + i * "*")  # 공백 생각하면서 하기

for i in range(n, 0, -1):
    print((n - i) * " " + i * "*")

# for i in range(1, n + 1):
#    print((n - i) * " " + (i - 1) * "*" + "*" + (i - 1) * "*" + (n - i) * " ")


for i in range(1, n + 1):  # 등차수열 이용
    print((n - i) * " " + (2 * i - 1) * "*")

# 완전이상하게 생긴 별임-for문 두번 이용
for i in range(1, n + 1):  # 등차수열 이용
    print((n - i) * " " + (2 * i - 1) * "*")

for i in range(n - 1, 0, -1):
    print((n - i) * " " + (2 * i - 1) * "*")


for i in range(n, 0, -1):
    print((n - i) * " " + (2 * i - 1) * "*")
for i in range(2, n + 1):  # 등차수열 이용
    print((n - i) * " " + (2 * i - 1) * "*")
