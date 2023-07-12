a, b = map(int, input().split())
# map으로 안받고 a=int(a),b=int(b)로 해도 ㄱㄴ

if a > b:
    print(">")
elif a < b:
    print("<")
else:
    print("==")
