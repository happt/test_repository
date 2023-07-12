filepath = "read_sample.txt"

# 파일 읽기
##1번
# fp = open("read_sample.txt", "r")
# data = fp.readlines()
# fp.close()  # open으로 해서 열었으면 반드시 닫아주기
# print(data)

# # 2번 list로 읽기
# with open(filepath, "r") as handle:
#     data2 = handle.readlines()
# print(data2)

##3번
# with open(filepath) as handle:
#     for line in handle:  # 한줄씩 읽어줌~
#         print(line)


# 4번
# seq = ""
# # sequence만 가져오고 싶음
# with open(filepath) as handle:
#     for line in handle:
#         if line.startswith(">"):
#             continue

#         seq += line.rstrip()  # 오른쪽에 있는 \n 날려버리기

# print(seq)


##5번
seq = ""
# sequence만 가져오고 싶음
with open(filepath) as handle:
    handle.readline()  # 제목 날림
    # _=handle.readline() ->사용하지 않는 값 담아두는 곳
    for line in handle:
        seq += line.strip()  # 오른쪽에 있는 \n 날려버리기

print(seq)
print(seq.count("A"))  # A의 개수 찾기
