def hint_counter():
    # Initialize hint counter
    hint_count = 0
    max_hints = 3

    # Example question (you can replace this with your actual question)
    question = "What is the capital of France?"
    correct_answer = "Paris"

    while hint_count < max_hints:
        # Display question and ask for input
        print(question)
        user_answer = input("Your answer: ")

        # Check if the player wants a hint
        if user_answer.lower() == "hint":
            # Provide a hint (you can customize the hints based on your needs)
            hint_count += 1
            if hint_count == 1:
                print("Hint: It starts with letter 'P'.")
            elif hint_count == 2:
                print("Hint: It is known as the City of Love.")
            elif hint_count == 3:
                print("Hint: The river Seine flows through this city.")

        # Check if the answer is correct
        elif user_answer.lower() == correct_answer.lower():
            print("Congratulations! That's correct.")
            break  # Exit the loop if the answer is correct

        # If answer is incorrect and not "hint", provide feedback
        else:
            print("Incorrect.")

        # Check if the player has used all hints
        if hint_count == max_hints:
            print("You have run out of hints.")

    # After the loop ends (correct answer or out of hints), ask the question again
    hint_counter()  # This recursively restarts the game after each attempt

# Start the program
if __name__ == "__main__":
    hint_counter()
