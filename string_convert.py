# seq1.replace("A", "T")

seq1 = "ATGTTATAG"

# seq1.replace("A", "t")
# seq1.replace("T", "a")
# seq1.replace("C", "g")
# seq1.replace("G", "c")

##replace 없이 바꾸는 방법
seq1_new = ""

for s in seq1:
    if s == "A":
        seq1_new += "T"
    elif s == "T":
        seq1_new += "A"
    elif s == "G":
        seq1_new += "C"
    elif s == "C":
        seq1_new += "G"

print(seq1)
print(seq1_new)

##
