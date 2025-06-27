# Task 1
def greet_user(name):
    print(f"Hello, {name}! Welcome aboard.", end=" ")

def add_numbers(a, b):
    return a + b

greet_user("Alice")
result = add_numbers(5, 10)
print(f"The sum of 5 and 10 is {result}.")


# Task 2
def describe_pet(pet_name, animal_type="dog"):
    print(f"I have a {animal_type} named {pet_name}.")
    
describe_pet("Buddy")
describe_pet("Whiskers", "cat")


# Task 3
def make_sandwich(*ingredients):
    print("Making a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")
        
make_sandwich("Lettuce", "Tomato", "Cheese")


# Task 4
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

fact_result = factorial(5)
fib_result = fibonacci(6)

print(f"Factorial of 5 is {fact_result}. The 6th Fibonacci number is {fib_result}.")
