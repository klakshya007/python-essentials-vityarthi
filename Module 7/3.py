#Check If Key Exists In A Dictionary

my_dict = {"a": 1, "b": 2, "c": 3}

key = input("Enter the key to check: ").strip()

if key in my_dict:
    print(f"The key '{key}' exists in the dictionary.")
else:
    print(f"The key '{key}' does not exist in the dictionary.")
