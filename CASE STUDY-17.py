

name = input("Enter student name: ")
n = int(input("Enter number of examinations: "))

if n < 2:
    print("Enter at least 2 examinations to analyze the trend.")

else:
    marks = []

    for i in range(n):
        score = float(input("Enter marks for exam " + str(i + 1) + ": "))

        if score < 0 or score > 100:
            print("Invalid marks! Enter marks between 0 and 100.")
            break

        marks.append(score)

    else:
        total = sum(marks)
        average = total / n

        print("\n--- Performance Report ---")
        print("Student Name:", name)
        print("Examination Marks:", marks)
        print("Average Marks:", round(average, 2))

        if marks[-1] > marks[0]:
            print("Performance Trend: Improving")
        elif marks[-1] < marks[0]:
            print("Performance Trend: Declining")
        else:
            print("Performance Trend: Stable")

        if average >= 75:
            print("Performance Level: Excellent")
        elif average >= 50:
            print("Performance Level: Good")
        else:
            print("Performance Level: Needs Improvement")
