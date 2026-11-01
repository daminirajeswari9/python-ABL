
name = input("Enter student name: ")
marks = float(input("Enter average marks out of 100: "))
attendance = float(input("Enter attendance percentage: "))

# Validate input
if marks < 0 or marks > 100 or attendance < 0 or attendance > 100:
    print("Invalid input! Enter values between 0 and 100.")

else:
    # Classify academic risk
    if marks < 40 or attendance < 65:
        risk = "High Risk"
    elif marks < 60 or attendance < 75:
        risk = "Medium Risk"
    else:
        risk = "Low Risk"

    # Display report
    print("\n--- Academic Risk Report ---")
    print("Student Name:", name)
    print("Average Marks:", marks)
    print("Attendance:", attendance, "%")
    print("Academic Risk:", risk)

    if risk == "High Risk":
        print("Recommendation: Provide academic support.")
    elif risk == "Medium Risk":
        print("Recommendation: Monitor progress regularly.")
    else:
        print("Recommendation: Continue current study habits.")
