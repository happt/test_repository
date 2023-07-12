import sys

print(sys.argv)

if len(sys.argv) != 3:
    print(f"#usage: python {sys.argv[0]} [num1] [num2]")
    # 만약 사용법을 몰라 오류가 났다면 나중에 왜 오류인지 알아볼 수 있음=manual
    sys.exit()

a = sys.argv[1]
# a=int(sys.argv[1])도 가능
b = sys.argv[2]

print(f"analysis::{int(a)+int(b)}")
