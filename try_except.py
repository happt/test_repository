try:
    with open("noname.txt") as handle:
        # lines = handle.readline()

        print(handle.readlines())

except FileNotFoundError:
    print("Check your input file")

print("# END")
