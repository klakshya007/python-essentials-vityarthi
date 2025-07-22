#Mean And Standard Deviation Of Quiz Marks

import statistics

marks = list(map(int, input("Enter 7 integers with spaces: ").split()))

if len(marks) >= 7:
    mean = statistics.mean(marks)
    std_dev = statistics.stdev(marks)
    print(f"Mean is: {mean}")
    print(f"Standard Deviation is: {std_dev}")
else:
    print("Please enter at least 7 integers.")
