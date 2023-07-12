# 들어있는 값들 찾아내기

l = [3, 1, 1, 2, 0, 0, 2, 3, 3]
s = set(l)
print(s)

# 한줄씩 뽑아내기
for elem in s:
    print(elem)

# new_list = list()
# for elem in l:
#     if elem not in new_list:
#         new_list.append(elem)  # 앞에서 차례차례 넣는데 만약 이미 들어가 있으면 pass~

# print(new_list)
