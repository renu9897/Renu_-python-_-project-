# password_generator.py
import random
import string

length = int(input("Enter password length: "))

letters = string.ascii_letters
digits = string.digits
special = string.punctuation

all_chars = letters + digits + special
password = "".join(random.choice(all_chars) for i in range(length))

print(f"Your Strong Password: {password}")