import sys

num = int(sys.argv[1])
# print(10 / num)


try:
    print(10 / num)

# except
#     print("error")


except ZeroDivisionError:
    print("zero division error")
except ValueError:
    print("value error")
print("next command")
