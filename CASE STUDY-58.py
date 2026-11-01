
student_name = input("Enter student name: ")
book_name = input("Enter book name: ")
borrow_days = int(input("Enter number of days borrowed: "))

allowed_days = 14
fine_per_day = 5

if borrow_days < 0:
    print("Invalid number of days!")

else:
    overdue_days = max(0, borrow_days - allowed_days)
    fine = overdue_days * fine_per_day

    print("\n--- Library Borrowing Report ---")
    print("Student Name:", student_name)
    print("Book Name:", book_name)
    print("Days Borrowed:", borrow_days)
    print("Allowed Days:", allowed_days)
    print("Overdue Days:", overdue_days)
    print("Fine Amount: Rs.", fine)

    amount_paid = float(input("Enter fine amount paid: "))

    if amount_paid < 0:
        print("Invalid payment amount!")

    else:
        balance = fine - amount_paid

        print("\n--- Fine Reconciliation ---")

        if balance > 0:
            print("Pending Fine: Rs.", balance)
        elif balance < 0:
            print("Extra Payment: Rs.", abs(balance))
        else:
            print("Fine fully paid.")

        print("Total Fine: Rs.", fine)
        print("Amount Paid: Rs.", amount_paid)
