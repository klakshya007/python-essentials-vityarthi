#Remove Key From Dictionary 

my_dict = {"a": 1, "b": 2, "c": 3}

key_to_remove = input("Enter the key to remove: ").strip()

if key_to_remove in my_dict:
    del my_dict[key_to_remove]
    print("Updated dictionary:", my_dict)
else:
    print(f"The key '{key_to_remove}' does not exist in the dictionary.")
