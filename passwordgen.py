import random
import string

def generate_password(length):
    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation


    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Invalid length. Please enter a positive integer.")
            return

        password = generate_password(length)
        print(f"Generated password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")

if __name__ == "__main__":
    main()
