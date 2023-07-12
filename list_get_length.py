l = ["AA", "AC", "AG", "AT"]
print(len(l))

# for elem in l:
#     print(elem)  # 요소들 하나씩

for idx, elem in enumerate(l):
    print(idx, elem)

for i in range(len(l)):
    print(i, l[i])
