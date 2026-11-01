
total_rooms = int(input("Enter total number of rooms: "))
students = int(input("Enter number of students: "))

if total_rooms <= 0 or students <= 0:
    print("Invalid input! Enter positive numbers.")

else:
    allocated_rooms = []
    available_rooms = total_rooms

    for i in range(students):
        name = input("\nEnter student name: ")
        year = int(input("Enter study year (1-4): "))

        if year < 1 or year > 4:
            print("Invalid study year! Student not allocated.")
            continue

        if available_rooms > 0:
            room_number = total_rooms - available_rooms + 1
            allocated_rooms.append((name, year, room_number))
            available_rooms -= 1

            print("Room allocated successfully!")
            print("Room Number:", room_number)
        else:
            print("Sorry! No rooms available for", name)

    print("\n--- Hostel Allocation Report ---")

    if allocated_rooms:
        for student in allocated_rooms:
            print("Student:", student[0],
                  "| Year:", student[1],
                  "| Room:", student[2])
    else:
        print("No rooms were allocated.")

    print("\nTotal Rooms:", total_rooms)
    print("Allocated Rooms:", len(allocated_rooms))
    print("Available Rooms:", available_rooms)
