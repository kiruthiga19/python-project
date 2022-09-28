def new_game():
    guesses = []
    correct_guesses = 0
    questions_num = 1

    for key in questions:
        print("---------------------------")
        print(key)
        for i in options[questions_num-1]:
            print(i)
        guess = input("enter (a,b,c,d) : ")
        guess = guess.lower()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        questions_num += 1

    display_score(correct_guesses, guesses)


def check_answer(answer, guess):
    if answer == guess:
        print("You are correct :)")
        return 1
    else:
        print("wrong :(")
        return 0


def display_score(correct_guesses, guesses):
    print("-----------------------------")
    print("RESULTS")
    print("-----------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()
    score = int((correct_guesses/len(questions))*100)
    print("your score id "+str(score)+"%")



def play_again():

    response = input("you want to play again?(yes or no) : ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False


questions = {
    "Who developed Python Programming Language?: ": "c",
    "Which type of Programming does Python support? : ": "d",
    " Is Python case sensitive when dealing with identifiers?": "a",
    "Which of the following is the correct extension of the Python file?": "c"

}

options = [["a) Wick van Rossum, b) Rasmus Lerdorf ,c) Guido van Rossum, d) NieneStom"],
           ["a) object-oriented programming, b) structured programming, c) functional programming, d) all of the mentioned"],
           ["a) no, b) yes, c) machine dependent, d) none of the mentioned"],
           ["a) .python, b) .pl, c) .py, d) .p"]]

new_game()

while play_again():
    new_game()
print("Byeeeeeeee")






