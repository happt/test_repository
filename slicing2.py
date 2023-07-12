seq1 = "ATGTTATAG"

for i in range(0, len(seq1), 3):  # 3개씩 끊어 읽기
    print(i, i + 3, seq1[i : i + 3])

# 거꾸로 읽기
##1번 방법
print(seq1[::-1])
##2번 방법
seq1_rev = ""
for i in range(len(seq1) - 1, -1, -1):
    # print(i, seq1[i])
    seq1_rev += seq1[i]

print(seq1)
print(seq1_rev)
