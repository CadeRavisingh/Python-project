def get_positive_float(prompt):
    """Helper function to ensure valid numeric inputs."""
    while True:
        try:
            val = float(input(prompt))
            if val < 0:
                print("Value cannot be negative. Try again.")
                continue
            return val
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def calculate_grade(percentage):
    """Determines the grade based on standard percentage thresholds."""
    if percentage >= 90: return "A+"
    elif percentage >= 80: return "A"
    elif percentage >= 70: return "B"
    elif percentage >= 60: return "C"
    elif percentage >= 50: return "D"
    else: return "F (Fail)"

def main():
    print("=" * 45)
    print("     MARKS & PERCENTAGE CALCULATOR PROJECT    ")
    print("=" * 45)
    
    # 1. Gather basic config setup
    num_subjects = int(get_positive_float("Enter the number of subjects: "))
    max_marks_per_subject = get_positive_float("Enter the Maximum Marks possible per subject (e.g. 100): ")
    
    report_card = {}
    total_obtained = 0
    
    # 2. Input marks loop
    for i in range(int(num_subjects)):
        print(f"\n  Subject {i + 1}  ")
        sub_name = input("Enter Subject Name: ").strip()
        if not sub_name:
            sub_name = f"Subject {i + 1}"
            
        while True:
            marks = get_positive_float(f"Enter marks obtained in {sub_name}: ")
            if marks <= max_marks_per_subject:
                break
            print(f" Obtained marks cannot exceed maximum possible marks ({max_marks_per_subject})!")
            
        # Store individual percentage
        sub_percentage = (marks / max_marks_per_subject) * 100
        report_card[sub_name] = {"marks": marks, "pct": sub_percentage}
        total_obtained += marks

    # 3. Complete Final Summary Metrics
    total_possible_marks = num_subjects * max_marks_per_subject
    final_percentage = (total_obtained / total_possible_marks) * 100
    final_grade = calculate_grade(final_percentage)
    
    # 4. Print Clean Formatted Report Summary
    print("\n" + "=" * 45)
    print("                 FINAL REPORT CARD             ")
    print("=" * 45)
    print(f"{'Subject':<20} | {'Marks Obtained':<15} | {'Percentage':<10}")
    print("-" * 45)
    
    for subject, data in report_card.items():
        print(f"{subject:<20} | {data['marks']:<15g} | {data['pct']:.2f}%")
        
    print("=" * 45)
    print(f"Grand Total Obtained : {total_obtained:g} / {total_possible_marks:g}")
    print(f"Aggregate Percentage : {final_percentage:.2f}%")
    print(f"Final Assigned Grade : {final_grade}")
    print("=" * 45)

if __name__ == "__main__":
    main()
