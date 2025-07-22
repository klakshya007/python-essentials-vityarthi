#Employee Data Update
employees = {
    "Sunny": 25000,
    "Ravi": 23000,
    "Vijay": 26000,
    "Messi": 30000,
}
name_to_remove = input("Enter the name of the employee to remove: ").strip()

if name_to_remove in employees:
    del employees[name_to_remove]
    print("Updated employee data:", employees)
else:
    print(f"Employee {name_to_remove} does not exist.")