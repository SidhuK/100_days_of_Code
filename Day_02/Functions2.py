
def greet(name):
    print(f"Hello {name}")
    print(f"Hi {name}")
    print(f"Whats up, {name}?")

greet("Karat")


# fuction with more than one input

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")
greet_with(name="Karat",location="Bathinda") # can be used without name and lcation here if needed


# check for prime numbers

def prime_checker(number):
    is_prime = True
    for i in range(2,number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("The number is prime number")
    else:
        print("Is not a prime number")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)