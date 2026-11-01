
customer_name = input("Enter customer name: ")
units = float(input("Enter electricity units consumed: "))

if units < 0:
    print("Invalid units! Units cannot be negative.")

else:
    # Calculate bill using progressive tariff slabs
    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = (100 * 2) + (units - 100) * 3
    elif units <= 300:
        bill = (100 * 2) + (100 * 3) + (units - 200) * 5
    else:
        bill = (100 * 2) + (100 * 3) + (100 * 5) + (units - 300) * 7

    fixed_charge = 50
    total_bill = bill + fixed_charge

    print("\n--- Electricity Bill ---")
    print("Customer Name:", customer_name)
    print("Units Consumed:", units)
    print("Energy Charge: Rs.", round(bill, 2))
    print("Fixed Charge: Rs.", fixed_charge)
    print("Total Electricity Bill: Rs.", round(total_bill, 2))
