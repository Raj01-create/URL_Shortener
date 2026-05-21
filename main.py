#URL Shortner 
import random
import string

urls = {}

def generate_code(length=5):

    characters = string.ascii_letters + string.digits

    short_code = ""

    for _ in range(length):
        short_code += random.choice(characters)

    return short_code

def shorten_url():

    original_url = input("Enter URL: ")

    short_code = generate_code()

    urls[short_code] = original_url

    print(f"Short URL: short.ly/{short_code}")

def open_url():

    code = input("Enter short code: ")

    if code in urls:
        print("Original URL:", urls[code])

    else:
        print("URL not found")

while True:

    print("\n1. Shorten URL")
    print("2. Open URL")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        shorten_url()

    elif choice == "2":
        open_url()

    elif choice == "3":
        break

    else:
        print("Invalid choice")
