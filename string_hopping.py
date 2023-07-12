seq = "AGTTTATAG"

print(seq[0::3])

res = []
for i in range(0, 9, 3):
    res.append(seq[i])
print(res)


for i in range(0, len(seq), 3):
    print(i, seq[i])
