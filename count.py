# filepath = "write_sample2.txt"

# seq = ""
# # sequence만 가져오고 싶음
# with open(filepath) as handle: #handle은 그냥 변수
#     handle.readline()  # 제목 날림
#     # _=handle.readline() ->사용하지 않는 값 담아두는 곳
#     for line in handle:
#         seq += line.strip()  # 오른쪽에 있는 \n 날려버리기

# print(seq)
# print(seq.count("A"))  # A의 개수 찾기
# print(seq.count("T"))
# print(seq.count("G"))
# print(seq.count("C"))


# 선생님 코드....

seq = ""
with open("write_sample.txt") as fo:
    _ = fo.readline()
    for line in fo:
        seq += line.strip()

with open("write_result.txt", "w") as fw:
    fw.write(f"A: {seq.count('A')}\n")
    fw.write(f"C: {seq.count('C')}\n")
    fw.write(f"G: {seq.count('G')}\n")
    fw.write(f"T: {seq.count('T')}\n")
