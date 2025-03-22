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
        return "Invalid"

subjects = ["Bangla", "English", "Math", "Science"]
grades = {}

for subject in subjects:
    while True:
        try:
            marks = int(input(f"Enter marks for {subject} (0-100): "))
            if 0 <= marks <= 100:
                grades[subject] = get_grade(marks)
                break
            else:
                print("Please enter a valid mark between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a number.")

print("\nGrade Report:")
for subject, grade in grades.items():
    print(f"{subject}: {grade}")
