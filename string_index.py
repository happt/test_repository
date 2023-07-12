seq1 = "AGTTTATAG"

# TT가 출현하는 index, 필요한 motif 찾을 때 이용함

# for문 사용하기

for i in range(0, len(seq1)):
    # seq1[i:i+2]
    if seq1[i : i + 2] == "TT":
        print(i)
    # print(i, i + 1, seq1[i : i + 2])
