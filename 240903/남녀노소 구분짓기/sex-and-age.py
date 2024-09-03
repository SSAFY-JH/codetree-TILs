gender = input()
age = int(input())

if gender == "0" and age >= 19:
    print("MAN")
elif gender == "1" and age >= 19:
    print("WOMAN")
elif gender == "0" and age <= 19:
    print("BOY")
else:
    print("GIRL")