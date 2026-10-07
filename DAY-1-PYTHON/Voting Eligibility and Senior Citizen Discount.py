age = int(input("Enter age: "))

vote = "Eligible" if age >= 18 else "Not Eligible"
discount = "Senior Citizen Discount" if age >= 60 else "No Discount"

print("Voting:", vote)
print("Discount:", discount)