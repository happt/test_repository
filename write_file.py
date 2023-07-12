# >A_Strain
# ATGCGGAAG
# TCGGGATAG


filepath = "write_sample.txt"
fw = open(filepath, "w")
# fw.write(">A_Strain\n")
# fw.write("ATGCGGAAG\n")
# fw.write("TCGGGATAG")

contents = [">A_Strain", "ATGCGGAAG", "TCGGGATAG"]
fw.write("\n".join(contents))  # enter기준으로 ...file에 적어두기
fw.close()
