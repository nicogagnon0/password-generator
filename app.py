# Password Generator Application

import secrets
import string


def ask_yes_no(prompt: str, default: bool = True) -> bool:
    suffix = " [Y/n]: " if default else " [y/N]: "
    while True:
        answer = input(prompt + suffix).strip().lower()
        if not answer:
            return default
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please enter 'y' or 'n'.")


# Ask the user for a password length within a safe range
def ask_length(prompt: str = "Enter password length (8-128)", default: int = 16) -> int:
    while True:
        text = input(f"{prompt} [default: {default}]: ").strip()
        if not text:
            return default
        try:
            value = int(text)
            if 8 <= value <= 128:
                return value
            print("Please enter a number between 8 and 128.")
        except ValueError:
            print("Please enter a valid integer.")


# Generate a secure random password using the given options
def generate_password(length: int,
                      use_lower: bool = True,
                      use_upper: bool = True,
                      use_digits: bool = True,
                      use_symbols: bool = True) -> str:
    
    # At least one character from each selected category is guaranteed to appear in the password
    categories = []
    if use_lower:
        categories.append(string.ascii_lowercase)
    if use_upper:
        categories.append(string.ascii_uppercase)
    if use_digits:
        categories.append(string.digits)
    if use_symbols:
        # Symbol set
        categories.append("!@#$%^&*()-_=+[]{};:,.?/")

    if not categories:
        raise ValueError("At least one character type must be enabled.")

    all_chars = "".join(categories)

    # Ensure length is enough to include one of each selected type
    if length < len(categories):
        raise ValueError(
            f"Password length must be at least {len(categories)} "
            f"for the selected character types."
        )

    # Start with 1 char from each category to guarantee each are used
    password_chars = [secrets.choice(cat) for cat in categories]

    # Fill the remaining characters
    remaining = length - len(password_chars)
    password_chars.extend(secrets.choice(all_chars) for _ in range(remaining))

    # Shuffle the result so the first characters are not predictable
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)


def main() -> None:
    print("=" * 50)
    print(" Secure Password Generator ")
    print("=" * 50)
    print("This tool generates strong, random passwords.")
    print()

    while True:
        length = ask_length()

        use_lower = ask_yes_no("Include lowercase letters (a-z)?", default=True)
        use_upper = ask_yes_no("Include uppercase letters (A-Z)?", default=True)
        use_digits = ask_yes_no("Include digits (0-9)?", default=True)
        use_symbols = ask_yes_no("Include symbols (!@#$, etc.)?", default=True)

        # If user disables everything, fall back to default lowercase + digits
        if not any([use_lower, use_upper, use_digits, use_symbols]):
            print("You disabled all character types. Using lowercase + digits instead.")
            use_lower, use_digits = True, True

        try:
            password = generate_password(
                length,
                use_lower=use_lower,
                use_upper=use_upper,
                use_digits=use_digits,
                use_symbols=use_symbols,
            )
        except ValueError as exc:
            print(f"Error: {exc}")
            print("Please try again.\n")
            continue

        print("\nYour generated password:\n")
        print(password)
        print("\n")

        if not ask_yes_no("Generate another password?", default=False):
            print("Exited successfully.")
            print()
            break


if __name__ == "__main__":
    main()