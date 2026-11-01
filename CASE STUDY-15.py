

vehicle_number = input("Enter vehicle number: ")
print("1. Two-Wheeler")
print("2. Car")
print("3. Bus")

choice = int(input("Select vehicle type (1-3): "))
hours = float(input("Enter parking duration in hours: "))

if hours <= 0:
    print("Invalid parking duration!")

elif choice not in [1, 2, 3]:
    print("Invalid vehicle type!")

else:
    # Parking rates per hour
    if choice == 1:
        vehicle_type = "Two-Wheeler"
        rate = 10
    elif choice == 2:
        vehicle_type = "Car"
        rate = 30
    else:
        vehicle_type = "Bus"
        rate = 50

    # Charge for every started hour
    parking_hours = int(hours)
    if hours > parking_hours:
        parking_hours += 1

    fee = parking_hours * rate

    # Discount for parking 8 hours or more
    if parking_hours >= 8:
        discount = fee * 0.10
    else:
        discount = 0

    total_fee = fee - discount

    print("\n--- Parking Receipt ---")
    print("Vehicle Number:", vehicle_number)
    print("Vehicle Type:", vehicle_type)
    print("Parking Duration:", hours, "hours")
    print("Charged Hours:", parking_hours)
    print("Parking Fee: Rs.", fee)
    print("Discount: Rs.", round(discount, 2))
    print("Total Fee: Rs.", round(total_fee, 2))
