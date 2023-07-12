# n = 1
# sum = 0

# while n < 11:
#     sum += n
#     n += 1

# print(sum)


# while True:
#     if n == 11:
#         break
#     sum += n
#     n += 1

# print(sum)


res = 0
n = 10

while n > 0:
    res += n
    n -= 1
print(res)

###
res = 0
n = 10
while True:
    if n == 0:
        break
    res += n
    n -= 1
print(res)
