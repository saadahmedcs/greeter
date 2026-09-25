import datetime
import sys


def get_time_based_salutation(hour: int | None = None) -> str:
    """Returns a time-appropriate salutation based on the current hour (0-23)."""
    if hour is None:
        hour = datetime.datetime.now().hour

    if 0 <= hour < 12:
        return "Good morning"
    elif 12 <= hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"


def generate_greeting(name: str | None = None) -> str:
    """Generates a formatted greeting string."""
    salutation = get_time_based_salutation()
    clean_name = name.strip() if name and name.strip() else "Friend"
    return f"{salutation}, {clean_name}!"


def main() -> None:
    """Entry point for command-line execution."""
    if len(sys.argv) > 1:
        user_name = " ".join(sys.argv[1:])
    else:
        user_name = input("Enter your name: ")

    greeting = generate_greeting(user_name)
    print(greeting)
    print(f"Today's date is {datetime.date.today()}")


if __name__ == "__main__":
    main()