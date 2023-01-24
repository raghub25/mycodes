def add(num1, num2):
    print(num1 + num2)


add(1, 2)


def calc_age(birth_year):
    return 2023 - int(birth_year)


year = input("Enter the birth year: ")
result = calc_age(year)
print(result)
