import calendar
import datetime as dt


def parse_date(text):
    """Parse DD-MM-YYYY. Raises ValueError for invalid calendar dates."""
    return dt.datetime.strptime(text.strip(), "%d-%m-%Y").date()


def calculate_age(birth, today=None):
    """Return (years, months, days) between birth and today."""
    today = today or dt.date.today()
    if birth > today:
        raise ValueError("Date of birth cannot be in the future.")

    # Whole months completed
    total_months = (today.year - birth.year) * 12 + (today.month - birth.month)
    if today.day < birth.day:
        total_months -= 1
    years, months = divmod(total_months, 12)

    # Date of the last "monthly anniversary", clamped to the month's length
    idx = birth.month - 1 + total_months
    y, m = birth.year + idx // 12, idx % 12 + 1
    last_day = calendar.monthrange(y, m)[1]
    anniversary = dt.date(y, m, min(birth.day, last_day))

    days = (today - anniversary).days
    return years, months, days


def main():
    print("=== Age Calculator ===")
    while True:
        text = input("\nEnter your date of birth (DD-MM-YYYY) or 'q' to quit: ")
        if text.strip().lower() == "q":
            print("Goodbye!")
            break
        try:
            birth = parse_date(text)
            years, months, days = calculate_age(birth)
        except ValueError as e:
            msg = str(e)
            if "future" in msg:
                print(f"Error: {msg}")
            else:
                print("Error: Invalid date. Use DD-MM-YYYY and a real calendar date.")
            continue
        print(f"Your age is: {years} years, {months} months, {days} days")


if __name__ == "__main__":
    main()