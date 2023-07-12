"""sum = 0
n = int(input())
for i in range(n + 1):
    sum += i

print(sum)"""


# range(start, stop, step(이건 ...몇칸 띄우나)


result = 1
n = int(input())
for i in range(1, n + 1):
    result *= i
print(result)
