
students = []
n = int(input("Enter number of students: "))

if n <= 0:
    print("Invalid number of students!")

else:
    for i in range(n):
        print("\nEnter details for Student", i + 1)

        roll_no = input("Enter roll number: ").strip()
        name = input("Enter student name: ").strip()
        marks = float(input("Enter marks out of 100: "))
        attendance = float(input("Enter attendance percentage: "))

        errors = []

        # Check missing details
        if roll_no == "":
            errors.append("Missing roll number")

        if name == "":
            errors.append("Missing student name")

        # Check duplicate roll numbers
        for student in students:
            if roll_no != "" and student["roll"] == roll_no:
                errors.append("Duplicate roll number")
                break

        # Validate marks
        if marks < 0 or marks > 100:
            errors.append("Invalid marks")

        # Validate attendance
        if attendance < 0 or attendance > 100:
            errors.append("Invalid attendance")

        # Store student record
        students.append({
            "roll": roll_no,
            "name": name,
            "marks": marks,
            "attendance": attendance,
            "errors": errors
        })

    # Display consistency report
    print("\n--- STUDENT RECORD CONSISTENCY REPORT ---")

    for student in students:
        print("\nRoll Number:", student["roll"])
        print("Name:", student["name"])
        print("Marks:", student["marks"])
        print("Attendance:", student["attendance"], "%")

        if student["errors"]:
            print("Status: INCONSISTENT")
            print("Errors:", ", ".join(student["errors"]))
        else:
            print("Status: VALID")

    valid_count = sum(
        1 for student in students if not student["errors"]
    )
    invalid_count = n - valid_count

    print("\n--- SUMMARY ---")
    print("Total Records:", n)
    print("Valid Records:", valid_count)
    print("Inconsistent Records:", invalid_count)
