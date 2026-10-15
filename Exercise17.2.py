import random
import string

def generate_otp():
    characters = string.ascii_uppercase + string.digits
    otp = ""

    for i in range(6):
        otp += random.choice(characters)

    return otp

def main():
    otp = generate_otp()
    print("Generated OTP:", otp)

if __name__ == "__main__":
    main()