from Contestants import Contestants
from Questions import Questions

questions_asked = [
    "\nWhat is the name of the animal with stripes?\na.) Zebra\nb.) Lion\nc.) Cow\n\n",
    "\nWhich animal is king of the jungle?\na.) Zebra\nb.) Lion\nc.) Cow\n\n",
    "\nWhich of the following animals cannot swim?\na.) Fish\nb.) Crocodile\nc.) Cow\n\n"
]

questions = [
    Questions(questions_asked[0], "a"),
    Questions(questions_asked[1], "b"),
    Questions(questions_asked[2], "c")
]

contestant1 = Contestants("Mike", "USA", 0)
contestant2 = Contestants("Asif", "Pakistan", 0)
contestant3 = Contestants("Kohli", "India", 0)

print("Hello to one and all! Welcome to the first edition of Who is the Tarzan!!!")
print("\nMy name is Aarushi and I am glad to welcome the contestants")
print("Let's give a round of applause to " + contestant1.name + " from " + contestant1.country)
print("\n " + contestant2.name + " from " + contestant2.country)
print("\n " + contestant3.name + " from " + contestant3.country)
print("\n Let's begin the quiz with " + contestant1.name)

for question in questions:
    contest1_answer = input(question.question_prompt)
    if contest1_answer == question.answer:
        contestant1.score += 1

print("\nThank you " + contestant1.name)
print("\n Let's give it up for " + contestant2.name)

for question in questions:
    contestant2_answer = input(question.question_prompt)
    if contestant2_answer == question.answer:
        contestant2.score += 1

print("\nThank you " + contestant2.name)
print("\n Let's give it up for " + contestant3.name)

for question in questions:
    contestant3_answer = input(question.question_prompt)
    if contestant3_answer == question.answer:
        contestant3.score += 1

print("\n We have finished our quiz with all the contestants. It's time for the Tarzan reveal!!!")
print("\n And the winner is.....")
# [1,1,2] [1,1,3] [2,1,1] [2,1,2] [2,1,3] [3,1,1] [3,1,2]
# [3,1,3] [3,2,1] [3,2,2] [3,2,3] [3,3,1] [3,3,2]
if contestant1.score != contestant2.score != contestant3.score:
    if contestant1.score >= contestant2.score and contestant1.score >= contestant3.score:
        print(contestant1.name + " !!!! You got " + contestant1.score + " questions right!!!")
    elif contestant2.score >= contestant1.score and contestant2.score >= contestant3.score:
        print(contestant2.name + " !!!! You got " + contestant2.score + " questions right!!!")
    elif contestant3.score >= contestant1.score and contestant3.score >= contestant2.score:
        print(contestant3.name + " !!!! You got " + contestant3.score + " questions right!!!")

if contestant1.score == contestant2.score == contestant3.score:
    print("\nWell well well!! We have a tie here")
    print("\n It's a do or die which will decide the tarzan now")
    print("\n Whoever answers this first correctly will be crowned as the Tarzan")
    print("\n Here's the question for you")

    ques = "\nWhich of the following animals is a friend of Tarzan \na.) Tiger\nb.) Leopard\nc.) Monkey\n\n"
    special_question = Questions(ques, "c")
    contestant1_answer = input(special_question.question_prompt)
    contestant2_answer = input(special_question.question_prompt)
    contestant3.answer = input(special_question.question_prompt)

    if contestant1_answer == special_question.answer:
        print("Congratulations " + contestant1.name + " You are the Tarzan!!!!!")
    elif contestant2_answer == special_question.answer:
        print("Congratulations " + contestant2.name + " You are the Tarzan!!!!!")
    elif contestant3_answer == special_question.answer:
        print("Congratulations " + contestant3.name + " You are the Tarzan!!!!!")
