from Bio.Seq import Seq  # 바이오 파이썬 이용

seq1 = "ATGTTATAG"
seq_obj = Seq(seq1)
print(seq1)
print(seq_obj.complement())  # 상보적인 서열 만들어버림
