# Student grade calculator with input validation. Deliverable:
def get_valid_score(assignment_name):
    """Prompts the user for a score and validates that it is a number between 0 and 100."""
    while True:
        user_input = input(f"Enter the score for {assignment_name} (0-100): ").strip()
        
        # Check if input is empty
        if not user_input:
            print("Input cannot be empty. Please enter a number.")
            continue
            
        try:
            score = float(user_input)
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid score! The number must be between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a valid numerical score.")

def calculate_letter_grade(average):
    """Returns the corresponding letter grade based on the average score."""
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

def main():
    print("=== Student Grade Calculator ===")
    
    # 1. Collect validated inputs using a loop
    assignments = ["Assignments", "Midterm Exam", "Final Exam"]
    scores = []
    
    for idx, assignment in enumerate(assignments, 1):
        score = get_valid_score(f"{idx}. {assignment}")
        scores.append(score)
    
    # 2. Calculate the weighted average (e.g., 30% Assignments, 30% Midterm, 40% Final)
    weighted_average = (scores[0] * 0.30) + (scores[1] * 0.30) + (scores[2] * 0.40)
    
    # 3. Determine the final letter grade
    letter_grade = calculate_letter_grade(weighted_average)
    
    # 4. Display the performance summary
    print("\n" + "="*30)
    print("        GRADE SUMMARY        ")
    print("="*30)
    print(f"Assignments Score : {scores[0]:.2f}%")
    print(f"Midterm Exam Score: {scores[1]:.2f}%")
    print(f"Final Exam Score  : {scores[2]:.2f}%")
    print("-"*30)
    print(f"Weighted Average  : {weighted_average:.2f}%")
    print(f"Final Letter Grade: {letter_grade}")
    print("="*30)

if __name__ == "__main__":
    main()
