l = ["AA", "AC", "AG", "AT"]

l.append("TT")
print(l)
l.insert(0, "A")
print(l)


idx = l.index("AA")
print(idx)

# l.insert(2, "AAA")
l.insert(idx + 1, "AAA")
print(l)
