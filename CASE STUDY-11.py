

name = input("Enter student name: ")
marks = float(input("Enter marks out of 100: "))
passing_marks = 40
grace_marks = 5

print("\n--- Examination Result ---")
print("Student Name:", name)
print("Original Marks:", marks)

if marks < 0 or marks > 100:
    print("Invalid marks! Enter marks between 0 and 100.")

elif marks >= passing_marks:
    print("Final Marks:", marks)
    print("Result: PASS")
    print("Grace Marks Awarded: 0")

elif marks + grace_marks >= passing_marks:
    final_marks = passing_marks
    print("Final Marks:", final_marks)
    print("Result: PASS")
    print("Grace Marks Awarded:", final_marks - marks)

else:
    print("Final Marks:", marks)
    print("Result: FAIL")
    print("Grace Marks Awarded: 0")
