numbers = [3, 5, 3, 2, 5, 5, 1]
unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

for unique_number in unique_numbers:
    n = numbers.count(unique_number)
    print(unique_number,n)
