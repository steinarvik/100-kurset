# Get user input
numbers_input = input("Enter a series of numbers separated by spaces:\n")

# Convert the input to a list of integers
numbers_list = [int(num) for num in numbers_input.split()]

# Calculate the frequency of each number
number_frequency = {}

for number in numbers_list:
    if not number in number_frequency:
        number_frequency[number] = 1
    else:
        number_frequency[number] += 1


# Calculate statistics
total_numbers = len(numbers_list)
sum_numbers = sum(numbers_list)
most_frequent_number = max(number_frequency, key=number_frequency.get)
average_number = round(sum_numbers / total_numbers, 2)
number_range = max(numbers_list) - min(numbers_list)

# Display the results
print("\nNumber Analysis Results:")
print("-" * 24)
print(f"Total Numbers: {total_numbers}")
print(f"Sum of Numbers: {sum_numbers}")
print(f"Range of Numbers: {number_range}")
print(f"Most Frequent Number: {most_frequent_number} (appears {number_frequency[most_frequent_number]} times)")
print(f"Average Number: {average_number}")