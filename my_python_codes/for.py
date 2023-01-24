
sum = 0
for number in range(11):
    if number % 2 == 0:
        sum += number
print(sum)

no_of_odd_numbers = 0
number_list = [12, 32, 34, 23, 26, 37, 59, 38]
for number in number_list:
    if number % 2 != 0:
        no_of_odd_numbers += 1

print("The total number of odd numbers in the given list is " + str(no_of_odd_numbers))


temp = 0
for number in range(0, len(number_list)-1):
    for second_num in range(len(number_list)-1):
        if number_list[second_num] > number_list[second_num + 1]:
            temp = number_list[second_num]
            number_list[second_num] = number_list[second_num + 1]
            number_list[second_num + 1] = temp
print(number_list)


# translate
# vowels -> g

def translate(word):
    final_word = ""
    for letter in word:
        if letter in "AEIOUaeiou":
            if letter.isupper():
                final_word += 'G'
            else:
                final_word += 'g'
        else:
            final_word += letter
    print(final_word)


input_word = input("Enter the word to be translated: ")
translate(input_word)
