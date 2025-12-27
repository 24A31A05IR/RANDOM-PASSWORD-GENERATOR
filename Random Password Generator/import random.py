import random
import string

def generate_password(length=16):
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    special = string.punctuation

    all_chars = upper + lower + digits + special

    password = ''.join(random.choice(all_chars) for _ in range(length))
    
    return password

if __name__ == "__main__":
    print(generate_password())