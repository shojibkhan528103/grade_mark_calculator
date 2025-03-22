# Grade Calculator for 4 Subjects

# Function to determine grade based on marks
def get_grade(marks):
    if 0 <= marks <= 40:
        return "F"
    elif 41 <= marks <= 60:
        return "D"
    elif 61 <= marks <= 70:
        return "C"
    elif 71 <= marks <= 80:
        return "B"
    elif 81 <= marks <= 90:
        return "A"
    elif 91 <= marks <= 100:
        return "A+"
    else:
        return "Invalid"  # This should not happen if input is validated properly

# Function to take input and validate marks
def get_marks(subject):
    while True:
        try:
            marks = int(input(f"Enter marks for {subject} (0-100): "))  # Prompt user for input
            if 0 <= marks <= 100:
                return marks  # Return valid marks
            else:
                print("Invalid input! Marks should be between 0 and 100.")  # Error message for invalid range
        except ValueError:
            print("Invalid input! Please enter a valid number.")  # Error message for non-numeric input

# List of subjects
subjects = ["Bangla", "English", "Math", "Science"]

# Dictionary to store subject marks and grades
student_report = {}

# Loop through subjects and take user input
for subject in subjects:
    marks = get_marks(subject)  # Get marks with validation
    grade = get_grade(marks)  # Determine grade
    student_report[subject] = {"Marks": marks, "Grade": grade}  # Store in dictionary

# Print Grade Report
print("\n===== Student Grade Report =====")
print(f"{'Subject':<10} {'Marks':<5} {'Grade'}")
print("-" * 30)
for subject, details in student_report.items():
    print(f"{subject:<10} {details['Marks']:<5} {details['Grade']}")  # Print formatted result
print("=" * 30)
