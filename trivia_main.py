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
  You can use up to 3 hints for the ENTIRE game. 
  If you are asked a question you dont completely know the answer to, you can type 
  "hint" and you will be given a related hint to that question.""")

    print()

def trivia_quiz():
    # Questions and Answers (with hints)
    questions = {
        "What planet was renamed to a dwarf planet?":{ 
        "answer":"Pluto", "hints": ["It shares the same name as a mickey mouse clubhouse character. \n", "One of its moons is named 'Charon' \n","Pl___ \n" ]
        },
        
        "How many planets are there in the solar system?":{
        "answer":"8", "hints": ["less than 10, higher than 5 \n","only 1 digit \n", "eig__"],
        },
        
        "What planet is known as “the blue planet”?":{
        "answer":"Uranus", "hints": ["It's made of gas and ice \n","It's the seventh planet from the sun. \n", "Ura___ \n"]
        },
        
        "What planet is known as “the ringed planet”?":{
        "answer":"Saturn", "hints":["It's a gas planet \n", "SZA song \n", "SA____ \n"]
        },
        
        "Which galaxy do we live in?":{ 
        "answer":"Milky way", "hints": ["Milk____ \n","Shares it's name with a chocolate bar. \n", "It's in the shape of a swirl \n"]
        },
        
        "Who was the first person to walk on the moon?":{
        "answer":"Neil armstrong", "hints":["His intials are N.A.\n", "He was an American Astronaut \n", "The Apollo 11 Mission \n"]
        },
        
        "What planet is the closest to the sun?":{ 
        "answer":"Mercury", "hints":["It's a rocky planet","This planet has no rings or moons \n", "Unhabital for any life form \n"]
        },
        
        "What planet is the farthest from the sun?":{ 
        "answer":"Neptune", "hints":["It's a gas planet \n", "Known as 'The Big Blue' \n", "Ne_____ \n"]
        },
        
        "Which planet does the moon “Triton” belong to?":{ 
        "answer":"Neptune", "hints":["It's a gas planet \n", "It is the Bluest Planet \n", "Ne_____ \n" ]
        },
        
        "Which planet in our solar system has more than 75 moons?":{ 
        "answer":"Jupiter", "hints":["It's a gas planet \n", "It is the 5th planet away from the sun \n","It is known as a 'Gas Giant' \n" ]
        },
        
        "What planet is known as Earth's “sister planet”?":{
        "answer":"Venus", "hints":["The planet is blue and green \n", "Third planet from the sun \n", "Has 1 moon \n"]
        },
        
        "Which planet is known to be the coldest planet within our solar system?":{ 
        "answer":"Uranus", "hints":["It's a gas planet \n", "It's surface is coloured Blue \n","The third largest planet in our solar system \n"]
        },
        
        "What is the second smallest planet in our solar system, after mercury?":{ 
        "answer":"Mars", "hints":["It's a rocky planet \n", "This planet has no rings or moons \n", "Unhabital for any life form \n"]
        },
        
        "Which planet inhabits environmental life?":{
        "answer":"Earth", "hints":["It's a rocky planet \n", "Has 1 moon \n", "Third planet from the sun \n"]
        },
        
        "What is the most hottest planet within our solar system?": { 
        "answer":"Venus", "hints":["Earths sister planet \n","Second planet from the sun \n", "This planet rotates the oppisite direction of other planets \n"]}}

    
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
    hint_count = 0  # Global hint counter for the game
    
    # Ask questions
    for question, data in selected_questions:
        answer = data["answer"]
        hints = data["hints"]
        print(question)
        while True:
            user_answer = input("Answer: ").strip().capitalize()

            if user_answer.lower() == "hint":
                if hint_count < 3:
                    hint_count += 1
                    print(f"Hint: {hints}")
                else:
                    print("You have run out of hints.")
            elif user_answer == answer:
                print("Correct! \n")
                print("───────────── ⋆⋅☆⋅⋆ ───────────── \n")
                score += 1
                payout += 1
                break  # Exit the question loop if correct
            else:
                print(f"Incorrect! The correct answer is {answer}. \n")
                print("───────────── ⋆⋅☆⋅⋆ ───────────── \n")
                break  # Exit the question loop if incorrect

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