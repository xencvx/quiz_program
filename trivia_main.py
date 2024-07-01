import random

# [COMPONENT]: PLAYED_BEFORE:
# [FUNCTION]: Asks the user if they had played the quiz before.
def played_before():
    while True:
        played_before = input("Have you played before? (yes/no): \n").lower()

        if played_before == "no":
            instructions()
            break

        elif played_before == "yes":
            print("───────────────────────────────")
            trivia_quiz()
            break

        else:
            print("ERROR: please enter either YES or NO \n")


# [COMPONENT]: INSTRUCTIONS:
# [FUNCTION]: Explains the rules of the quiz in detail.
def instructions():
    print("───────────── ⋆⋅☆⋅⋆ ─────────────")
    print("          INSTRUCTIONS:")
    print("───────────── ⋆⋅☆⋅⋆ ─────────────")
    print("""Welcome to the payout Trivia quiz!

• PAYOUT:
  Your payout depends on how many questions you get right!, each question is worth
  $1.
  EXAMPLE: I chose to answer 5 questions, I got 3 questions correct but 2 
           incorrect. My end payout would be $3

• QUESTIONS:
  Questions in this Trivia are related to our Solar System!
  MINIMUN Questions: 5
  MAXIMUN Questions: 15

• HINTS: 3 (MAX)
  If you are asked a question you dont completely know the answer to, you can type 
  "hint" and you will be given a related hint to that question.

• DOUBLE TROUBLE: 
- Double trouble is a endgame extension, where if you answer all questions 
  correctly, you will be asked if you want to enter "Double Trouble" mode. 
- In double trouble mode, you will answer the same related questions again (at 
  random) and recieve DOUBLE the amount of payout at endgame!. 

- Heres the catch, in double trouble you CANNOT use any hints. And if you answer a 
  question incorrectly, the program will end straight away - losing all of your 
  money!.""")

    print()

def trivia_quiz():
    # Questions and Answers
    questions = {
        "What planet was renamed to a dwarf planet?": "Pluto",
        "How many planets are there in the solar system?": "8",
        "What planet is known as “the blue planet”?": "Uranus",
        "What planet is known as “the ringed planet”?": "Saturn",
        "Which galaxy do we live in?": "Milky way",
        "Who was the first person to walk on the moon?": "Neil armstrong",
        "What planet is the closest to the sun?": "Mercury",
        "What planet is the farthest from the sun?": "Neptune",
        "Which planet does the moon “Triton” belong to?": "Neptune",
        "Which planet in our solar system has more than 75 moons?": "Jupiter",
        "What planet is known as Earth's “sister planet”?": "Venus",
        "Which planet is known to be the coldest planet within our solar system?": 
        "Uranus",
        "What is the second smallest planet in our solar system, after mercury?": 
        "Mars",
        "Which planet inhabits environmental life?": "Earth",
        "What is the most hottest planet within our solar system?": "Venus" .lower()}

    # User input for number of questions
    def num_questions():
        while True:
            num_questions = input("How many questions would you like to answer (5-15)? \n")
            print("───────────────────────────────")
            print("     TRIVIA QUESTIONS:")
            print("─────────────────────────────── \n")
            if num_questions.isdigit():
                num_questions = int(num_questions)
                if 5 <= num_questions <= 15:
                    return num_questions
                else:
                    print("Error: Please enter a number between 5 and 15.\n")
            else:
                print("Error: Please enter a whole number.\n")


    num_questions_value = num_questions()

    # Select random questions
    selected_questions = random.sample(list(questions.items()), num_questions_value)

    # Initialize score and payout
    score = 0
    payout = 0

    # Ask questions
    for question, answer in selected_questions:
        print(question)
        user_answer = input("Answer: ").strip().capitalize()

        if user_answer == answer:
            print("Correct! \n")
            print("───────────── ⋆⋅☆⋅⋆ ───────────── \n")
            score += 1
            payout += 1
        else:
            print(f"Incorrect! The correct answer is {answer}. \n")
            print("───────────── ⋆⋅☆⋅⋆ ───────────── \n")
    # Calculate payout
    total_payout = payout * 1  # Each question is $1

    # Display results
    print("───────────── ⋆⋅☆⋅⋆ ───────────── ")
    print("        TRIVIA COMPLETED!")
    print("──────────────────────────────────")
    print(f"SOCRE: You got: {score} / {num_questions_value} questions correct!.")
    print(f"PAYOUT: You earned: ${total_payout}.")


# MAIN CONSOLE:

# INTRODUCTION [FUNCTION]
# Welcomes user to quiz.
print("⋆⁺₊⋆ ─────────── ⋆☆⋆ ─────────── ⋆⁺₊⋆")
print(" WELCOME TO THE PAYOUT TRIVIA QUIZ!")
print("──────────────────────────────────────")

played_before()

print("───────────────────────────────")
input("Press ENTER to begin: ")

trivia_quiz()


