from colors import greeting, helper, success, warning, danger
from constants import commands
from handlers import (
    add_contact,
    change_contact,
    show_phone,
    show_all_contacts,
    add_birthday,
    show_birthday,
    birthdays,
)
from address_book import AddressBook
from error_decorators import input_error

def parse_input(user_input):
    """Parse user input into command and arguments."""
    parts = user_input.strip().split()
    command = parts[0] if parts else None
    args = parts[1:]
    return command, args

def main():
    book = AddressBook()
    print(greeting("Welcome to the assistant bot!"))

    while True:
        user_input = input(helper("Enter a command: "))
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print(greeting("Good bye!"))
            break

        elif command == "hello":
            print(greeting("How can I help you?"))

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_contact(args, book))

        elif command == "phone":
            print(show_phone(args, book))

        elif command == "all":
            print(show_all_contacts(book))

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(args, book))

        else:
            print(danger(f"Invalid command. Choose => {greeting(commands)}"))

if __name__ == "__main__":
    main()
