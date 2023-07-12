l = ["AA", "AC", "AG", "AT"]

l.append("CA")
print(l)

s = "ACGT"
s += "TTT"
print(s)


l = ["A", "A", "G", "T", "C"]
s = set(l)  # 중복 없애줌
print(s)

s.add("TT")
print(s)
