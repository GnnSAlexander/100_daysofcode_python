# Start the quiz
print("Welcome to the Dragon Ball Fan Quiz!")
print("Answer the following questions to find out if you're a true Dragon Ball fan.\n")

# Question 1
print("1. Who is the main protagonist of Dragon Ball?")
print("a) Naruto Uzumaki")
print("b) Monkey D. Luffy")
print("c) Goku")
answer1 = input("Enter your choice (a/b/c): ").strip().lower()

# Question 2
print("\n2. What is the name of the planet Goku is from?")
print("a) Namek")
print("b) Earth")
print("c) Planet Vegeta")
answer2 = input("Enter your choice (a/b/c): ").strip().lower()

# Question 3
print("\n3. Which technique is used by Goku to create a powerful energy ball?")
print("a) Kamehameha")
print("b) Rasengan")
print("c) Spirit Bomb")
answer3 = input("Enter your choice (a/b/c): ").strip().lower()

# Question 4
print("\n4. Who is Goku's rival and fellow Saiyan prince?")
print("a) Piccolo")
print("b) Frieza")
print("c) Vegeta")
answer4 = input("Enter your choice (a/b/c): ").strip().lower()

# Question 5
print("\n5. What are the seven magical orbs called?")
print("a) Dragon Balls")
print("b) Infinity Stones")
print("c) Sacred Jewels")
answer5 = input("Enter your choice (a/b/c): ").strip().lower()

# Determine if the user is a fan using nested if statements
if answer1 == 'c':
    if answer2 == 'c':
        if answer3 == 'c':
            if answer4 == 'c':
                if answer5 == 'a':
                    result = "a true Dragon Ball fan!"
                else:
                    result = "a casual Dragon Ball fan."
            else:
                result = "a casual Dragon Ball fan."
        else:
            result = "a casual Dragon Ball fan."
    else:
        result = "a casual Dragon Ball fan."
else:
    result = "not a Dragon Ball fan."

# Output the result
print(f"\nBased on your answers, you are {result}")
