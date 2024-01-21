# Exercise 1: Calculate the multiplication and sum of two numbers
# Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

# Given 1: number1 = 20 number2 = 30
# Expected Output: The result is 600

# Given 2: number1 = 40 number2 = 30
# Expected Output: The result is 70

# psuedocode

# Function
def product_and_sum(number_one, number_two):
    product = number_one * number_two
    if product <= 1000:
        return product
    else:
        return (number_one + number_two)

# Given 1
first_given_number_one = 20
first_given_number_two = 30

# Given 2
second_given_number_one = 40
second_given_number_two = 30

# Result to the given 1
result = product_and_sum(first_given_number_one, first_given_number_two)
print("\033[1;32;40m The product of two numbers in given 1 is", result)

# Result to the given 2
result = product_and_sum(second_given_number_one, second_given_number_two)
print("\033[1;32;40m The sum of two numbers in given 2 is", result)


