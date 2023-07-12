filepath = "write_sample2.txt"
contents = [">A_Strain", "ATGCGGAAG", "TCGGGATAG"]

# 더 추천하는 방법
with open(filepath, "w") as handle:
    handle.write("\n".join(contents))
