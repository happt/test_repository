# k mer
"""
for i in range(1, 5):
    for j in range(1, 5):
        print(i, j)"""

# 구구단 짝수단만 출력

"""for i in range(2, 10, 2):
    for j in range(1, 10):
        # print(i, "*", j, "=", i * j)
        print(f"{i}*{j}={i*j}")"""


"""for i in range(1, 10):
    if i % 2 == 0:
        for j in range(1, 10):
            print(f"{i}*{j}={i*j}") #deapth가 너무 길다..."""


"""for i in range(1, 10):
    if i % 2 != 0:
        pass
    else:
        for j in range(1, 10):
            print(f"{i}*{j}={i*j}")"""


for i in range(1, 10):
    print(f"######{i}")
    if i % 2 != 0:
        continue  # i를 찾는 for문을 계속 진행시키기

    for j in range(1, 10):
        print(f"{i}*{j}={i*j}")

# for i in range(1, 10):
#     print(f"######{i}")
#     if i % 2 != 0:
#         break  # 그냥 for문 자체를 종료 시켜버림..i 찾는 for문도

#     for j in range(1, 10):
#         print(f"{i}*{j}={i*j}")
