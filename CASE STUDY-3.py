print("HOSPITAL BILLING SYSTEM")

name = input("Enter patient name: ")
consultation = float(input("Enter consultation fee: "))
medicine = float(input("Enter medicine charges: "))
room = float(input("Enter room charges: "))

total = consultation + medicine + room

if total < 2000:
    category = "Low"
elif total < 5000:
    category = "Medium"
else:
    category = "High"

print("\n--- Patient Bill ---")
print("Patient Name:", name)
print("Total Bill: Rs.", total)
print("Classification:", category)