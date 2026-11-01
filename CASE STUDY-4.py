
name = input("Enter employee name: ")
basic_salary = float(input("Enter basic salary: "))
allowances = float(input("Enter allowances: "))
deductions = float(input("Enter deductions: "))

if basic_salary < 0 or allowances < 0 or deductions < 0:
    print("Invalid input! Salary and amounts cannot be negative.")

else:
    gross_salary = basic_salary + allowances

    if deductions > gross_salary:
        print("Invalid deductions! Deductions cannot exceed gross salary.")

    else:
        net_salary = gross_salary - deductions

        print("\n--- Employee Payroll Report ---")
        print("Employee Name:", name)
        print("Basic Salary: Rs.", round(basic_salary, 2))
        print("Allowances: Rs.", round(allowances, 2))
        print("Gross Salary: Rs.", round(gross_salary, 2))
        print("Total Deductions: Rs.", round(deductions, 2))
        print("Net Salary: Rs.", round(net_salary, 2))

        if net_salary >= 30000:
            print("Payroll Status: High Salary")
        elif net_salary >= 15000:
            print("Payroll Status: متوسط Salary")
        else:
            print("Payroll Status: Low Salary")
