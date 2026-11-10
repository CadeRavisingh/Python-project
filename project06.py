import random
import time

def get_integer_input(prompt):
    """Safely retrieves an integer from the user with validation."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input")

def generate_question(operation):
    """Generates random numbers and calculates the correct answer based on the operation."""
    if operation == 1:  # Addition
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        return f"{num1} + {num2}", num1 + num2
    
    elif operation == 2:  # Subtraction
        num1 = random.randint(1, 100)
        num2 = random.randint(1, num1)
        return f"{num1} - {num2}", num1 - num2

    elif operation == 3:  # Multiplication
        num1 = random.randint(1, 12)
        num2 = random.randint(1, 12)
        return f"{num1} × {num2}", num1 * num2

    elif operation == 4:  # Division
        num2 = random.randint(1, 12)
        correct_ans = random.randint(1, 12)
        num1 = num2 * correct_ans  # Ensures clean integer division with no remainders
        return f"{num1} ÷ {num2}", correct_ans

def run_practice_session(operation_name, operation_code):
    """Runs a 5-question practice block for the chosen math operation."""
    score = 0
    total_question = 5
    start_time = time.time()

    for i in range(1, total_question + 1):
        question_text, correct_answer = generate_question(operation_code)
        print(f"\nQuestion {i}/{total_question}: What is {question_text}?")

        user_answer = get_integer_input("Your answer: ")

        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer was {correct_answer}")
            
    end_time = time.time()
    duration = round(end_time - start_time, 1)

    print("\n==========================")
    print(f"Score: {score}/{total_question} ({(score/total_question)*100:.0f}%)")
    print(f"Time Taken: {duration} seconds")
    print("==========================")
    input("\nPress Enter to return to the Main Menu.... ")

def main():
    """Main program loop driving the menu interface."""
    while True:
        print("\n======================")
        print("1. Addition Practice ")
        print("2. Subtraction Practice ")
        print("3. Multiplication Practice ")
        print("4. Division Practice ")
        print("5. Exit Program ")
        print("=========================")

        choice = get_integer_input("Select an option (1-5): ")
        if choice == 1:
            run_practice_session("Addition", 1)
        elif choice == 2:
            run_practice_session("Subtraction", 2)
        elif choice == 3:
            run_practice_session("Multiplication", 3)
        elif choice == 4:
            run_practice_session("Division", 4)
        elif choice == 5:
            print("\nThanks for practicing! Goodbye.")
            break
        else:
            print("Invalid option. Please choose between 1-5.")

if __name__ == "__main__":
    main()