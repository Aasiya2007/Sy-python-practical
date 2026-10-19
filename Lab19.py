import hashlib

USER_FILE = "users.txt"
MAX_ATTEMPTS = 3
SPECIAL_CHARACTERS = "!@#$%^&*"


def load_users():
    """Load users from file."""
    users = {}
    try:
        file = open(USER_FILE, "r")
        lines = file.readlines()
        file.close()

        for line in lines:
            line = line.strip()
            if line == "":
                continue

            parts = line.split(",")
            users[parts[0]] = parts[1]

    except FileNotFoundError:
        pass

    return users


def save_user(username, hashed_password):
    """Save a new user to file."""
    file = open(USER_FILE, "a")
    file.write(username + "," + hashed_password + "\n")
    file.close()


def hash_password(password):
    """Convert password into SHA-256 hash."""
    hashed = hashlib.sha256(password.encode()).hexdigest()
    return hashed

def validate_username(username, users):
    """Check username rules."""
    if username == "":
        raise ValueError("Username cannot be empty.")

    if len(username) < 4:
        raise ValueError("Username must be at least 4 characters long.")

    if not username.isalnum():
        raise ValueError("Username can contain only letters and digits.")

    if username in users:
        raise ValueError("This username is already taken.")


def validate_password(password):
    """Check password rules."""
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif ch in SPECIAL_CHARACTERS:
            has_special = True

    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long.")

    if " " in password:
        raise ValueError("Password cannot contain spaces.")

    if not has_upper:
        raise ValueError("Password needs at least one UPPERCASE letter.")

    if not has_lower:
        raise ValueError("Password needs at least one lowercase letter.")

    if not has_digit:
        raise ValueError("Password needs at least one digit.")

    if not has_special:
        raise ValueError(
            "Password needs at least one special character (!@#$%^&*)."
        )


def get_menu_choice():
    """Get menu choice."""
    try:
        choice = int(input("Enter your choice (1-3): "))
        return choice
    except ValueError:
        print("Invalid input! Please enter a NUMBER (1, 2 or 3).")
        return None


def register_user(users):
    """Register a new user."""
    try:
        username = input("Choose a username: ").strip()
        validate_username(username, users)

        password = input("Choose a password: ")
        validate_password(password)

        confirm_password = input("Confirm your password: ")

        if password != confirm_password:
            raise ValueError("Passwords do not match.")

    except ValueError as error:
        print("Registration failed:", error)

    else:
        hashed = hash_password(password)
        users[username] = hashed
        save_user(username, hashed)
        print(f"User '{username}' registered successfully!")

    finally:
        print("-- Registration process finished --")


def login_user(users, locked_users):
    """Login with limited attempts."""
    if len(users) == 0:
        print("No users registered yet. Please register first.")
        return

    username = input("Enter username: ").strip()

    if username in locked_users:
        print("This account is LOCKED due to too many failed attempts.")
        return

    attempts = 0
    logged_in = False

    while attempts < MAX_ATTEMPTS:
        password = input("Enter password: ")

        try:
            stored_hash = users[username]

            if hash_password(password) != stored_hash:
                raise ValueError("Wrong password")

        except KeyError:
            attempts = attempts + 1
            print( f"Invalid username or password. "
                   f"Attempts left: {MAX_ATTEMPTS - attempts}")

        except ValueError:
            attempts = attempts + 1
            print(f"Invalid username or password. "
                  f"Attempts left: {MAX_ATTEMPTS - attempts}" )

        else:
            logged_in = True
            break

    if logged_in:
        print(f"\nLogin successful! Welcome, {username}!")
    else:
        if username in users:
            locked_users.append(username)

        print("Too many failed attempts. Login blocked.")


def main():
    users = load_users()
    locked_users = []

    print("=" * 45)
    print("          SECURE LOGIN SYSTEM")
    print("=" * 45)
    print(f"{len(users)} registered user(s) loaded from file.")

    while True:
        print("\n1. Register New User")
        print("2. Login")
        print("3. Exit")

        choice = get_menu_choice()

        if choice is None:
            continue
        elif choice == 1:
            register_user(users)
        elif choice == 2:
            login_user(users, locked_users)
        elif choice == 3:
            print("Exiting Secure Login System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2 or 3.")

main()
