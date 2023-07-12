# 173페이지부터
# if condition == True
l = [1, 2, 3, 4]

new_list = [x for x in l if x % 2 == 0]
print(new_list)

codon = ["ATG", "GGC", "TGA", "CCT"]
# A가 안들어있는 요소들만 codon_new에 넣으세요
# codon_new=list()
# for seq in codon:
#     if "A" not in seq:
#         codon_new.append(seq)
codon_new = [x for x in codon if "A" not in x]


print(codon_new)
