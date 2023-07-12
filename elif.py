num = int(input("enter: "))

# if num % 3 == 0 or num % 7 == 0:
#    print(f"{num}은 3과 7의 배수")
# elif num % 3 == 0:
#    print(f"{num}은 3의 배수")
# elif num%7==0:
#    print(f"{num}은 7의 배수")
# else:
#    print(f"{num}은 3과 7의 배수가 아님.")


if num % 3 == 0:
    if num % 7 == 0:
        print(f"{num}은 3의 배수 7의 배수")
    else:
        print(f"{num}은 3의 배수")

elif num % 7 == 0:
    print(f"{num}은 7의 배수")
else:
    print(f"{num}은 3과 7의 배수가 아님.")
