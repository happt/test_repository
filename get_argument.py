import sys

# print(sys.argv)
# print(sys.argv[0])
# print(sys.argv[1])


# 이렇게 하고 커맨드에서 리스트 추가한다음에 위에 있는 인덱싱까지 한번에 가능


# gene = sys.argv[1]
# print(f"Gene: {gene}")

# input 상관없이 간단

a = sys.argv[1]
# a=int(sys.argv[1])도 가능
b = sys.argv[2]

print(f"analysis::{int(a)+int(b)}")
