import random
import string

def generate_password(min_Length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    password = []
    has_number = False
    has_special = False

    while len(password) < min_Length:
        new_char = random.choice(characters)
        password.append(new_char)

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

    # Ensure criteria are met
    if numbers and not has_number:
        password[random.randint(0, min_Length - 1)] = random.choice(digits)
    if special_characters and not has_special:
        password[random.randint(0, min_Length - 1)] = random.choice(special)

    return ''.join(password)

# Gets user input
min_Length = int(input("Enter the minimum length: "))
has_number = input("Do you want to include numbers (Y/N)? ").upper() == "Y"
has_special = input("Do you want to add Special Characters (Y/N)? ").upper() == "Y"

# Call the function
password = generate_password(min_Length, has_number, has_special)
print("The generated password is: ", password)



