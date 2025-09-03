from datetime import datetime

date_format = "%d-%m-%Y"
categories = {"I": "Income", "E": "Expense"}

def get_date(prompt, allow_default=False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)
    try:
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid Date Format, Please enter the date in the format DD-MM-YYYY format")
        return get_date(prompt, allow_default=allow_default)


def get_amount():
    try:
        amount = float(input("Enter The Amount: "))
        if amount <= 0:
            raise ValueError("Amount must be a non-negative number and non-zero value.")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()

def get_category():
    category = input("Enter The Category: ('I' for Income or 'E' for Expense): ").upper()
    if category in categories:
        return categories[category]
    print("Invalid Category, Please enter one of the following: 'I' for Income or 'E' for Expense.")
    return get_category()

def get_description():
    return input("Enter a Description: ")
