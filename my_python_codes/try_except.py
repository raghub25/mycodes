try:
    num_list = [1, 2, 3, 4, 5]
    for number in num_list + 1:
        print(number)
    print(num_list[5])
except IndexError as err:
    print(err)
except TypeError as err:
    print(err)
