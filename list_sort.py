gene_expr = [3.14, 11.82, 7.44, 1.92]
codon = ["ATG", "GGC", "TGA", "CCT"]

##리스트 만들기-원본 유지
gene_expr_sorted = sorted(gene_expr)  # 오름차순
gene_expr_sorted_des = sorted(gene_expr, reverse=True)  # 내림차순

print(gene_expr_sorted)
print(gene_expr_sorted_des)

##그냥 하기-원본 유지 필요 없을 때 이용
print(gene_expr)
gene_expr.sort()
print(gene_expr)
gene_expr.sort(reverse=True)
print(gene_expr)

# codon_asc = sorted(codon)
# codon_des = sorted(codon, reverse=True)
# print(codon_asc)
# print(codon_des)
