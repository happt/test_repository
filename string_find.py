seq1 = "ATGTTATAG"

# if seq1.find("C")==-1:
#     print("c 없음")

##find이용
is_c_in = seq1.find("C")

if is_c_in < 0:
    print("No C")
else:
    print("Yes C")

# print(seq1.find("A"))
# print(seq1.find("T"))
# print(seq1.find("G"))
# print(seq1.find("C")) 없으므로 -1 출력해줌

##true/false 이용
is_c_in2 = "C" in seq1
print(is_c_in2)  # False


is_c_not_in = "C" not in seq1
print(is_c_not_in)  # True

##list에서 들어있는지 확인하기
data = ["A", "C", "T"]
print("A" in data)
print("G" in data)
