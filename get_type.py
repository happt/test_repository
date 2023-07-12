def print_type(obj):
    print(obj, type(obj))


a = "this is a string."

# print(a, type(a))
print_type(a)


b = -2

# print(b, type(b))
print_type(b)

c = 3.14
# print(c, type(c))
print_type(c)

d = ["abc", 123]
print_type(d)

e = (1, 2, "ab")
print_type(e)

f = range(4)
print_type(f)

g = {"A": 10, "B": 7}
print_type(g)

h = {1, 2, "ab"}
print_type(h)

i = True
print_type(i)

j = b"Byte string"
print_type(j)

k = None
print_type(k)
