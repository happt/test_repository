# seq없이 가볍게~

A, C, G, T = 0, 0, 0, 0

with open("write_sample.txt") as fo:
    _ = fo.readline()
    for line in fo:
        A += line.count("A")
        C += line.count("C")
        G += line.count("G")
        T += line.count("T")


with open("write_result1.txt", "w") as fw:
    fw.write(f"A: {'A'}\n")
    fw.write(f"C: {'C'}\n")
    fw.write(f"G: {'G'}\n")
    fw.write(f"T: {'T'}\n")
