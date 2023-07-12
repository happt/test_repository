def my_func_1():
    print("bio")  # return값이 없음


def my_func_2():
    return "return value from my_func_2"


def my_func_3(name):
    print(f"hello {name}")


def my_func_4(num):
    return num**2


res1 = my_func_1()
res2 = my_func_2()
my_func_3("Bio")
res4 = my_func_4(3)  # 이건 그냥 값만 넣은 것
print(res1)  # None
print(res2)  # return value from my_func_2
print(res4)
