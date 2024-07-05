print("Welcome to the DC Character Quiz!")
print("Answer the following questions to find out which DC character you are.\n")

print("1. Do you prefer working alone or with a team?")
print("a) Alone")
print("b) With a team")
answer1 = input("Enter your choice (a/b): ").strip().lower()

print("\n2. Do you rely more on your intellect or physical strength?")
print("a) Intellect")
print("b) Physical strength")
answer2 = input("Enter your choice (a/b): ").strip().lower()

print("\n3. What motivates you more?")
print("a) Justice")
print("b) Power")
answer3 = input("Enter your choice (a/b): ").strip().lower()


if answer1 == 'a' and answer2 == 'a' and answer3 == 'a':
    character = "Batman"
elif answer1 == 'b' and answer2 == 'b' and answer3 == 'a':
    character = "Superman"
elif answer1 == 'a' and answer2 == 'b' and answer3 == 'b':
    character = "Wonder Woman"
elif answer1 == 'b' and answer2 == 'a' and answer3 == 'b':
    character = "The Flash"
else:
    character = "Unknown character"

print(f"\nBased on your answers, you are {character}!")
