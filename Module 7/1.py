#Counting Currencies
n = int(input("Enter Number of Currencies: "))

distinct_countries = set()

for i in range(n):
    country = input(f"Enter the name of the country ({i + 1}/{n}): ").strip()
    distinct_countries.add(country)

print(f"Total number of distinct country currencies: {len(distinct_countries)}")
