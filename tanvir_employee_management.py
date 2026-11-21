"""Employee Salary Management System - Module 3 assignment."""

from pathlib import Path


EMPLOYEE_FILE = Path(__file__).with_name("employees.txt")


def add_employee(name, employee_id, salary):
    """Append one employee record and return True when it is saved."""
    try:
        with EMPLOYEE_FILE.open("a", encoding="utf-8") as file:
            file.write(f"{name} | {employee_id} | {salary}\n")
        return True
    except OSError as error:
        print(f"Could not save employee: {error}")
        return False


def get_employees():
    """Read and return employee records as a list of strings."""
    try:
        with EMPLOYEE_FILE.open("r", encoding="utf-8") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        return []
    except OSError as error:
        print(f"Could not read employee records: {error}")
        return []


def view_employees():
    """Display every employee record stored in the file."""
    employees = get_employees()

    if not employees:
        print("No employee records found.")
        return

    print("\nEmployee Records")
    print("-" * 40)
    for number, employee in enumerate(employees, start=1):
        print(f"{number}. {employee}")
    print("-" * 40)


def add_employee_from_input():
    """Collect, validate, and save information for one employee."""
    name = input("Enter Name: ").strip()
    employee_id = input("Enter ID: ").strip()
    salary = input("Enter Salary: ").strip()

    if not name or not employee_id or not salary:
        print("Name, ID, and Salary cannot be empty.")
        return

    if any("|" in value for value in (name, employee_id, salary)):
        print("Please do not use the '|' character in the information.")
        return

    try:
        if float(salary) <= 0:
            print("Salary must be greater than zero.")
            return
    except ValueError:
        print("Salary must be a number.")
        return

    if add_employee(name, employee_id, salary):
        print("Employee Added Successfully")


def main():
    """Run the employee management menu until the user exits."""
    while True:
        print("\n1. Add Employee")
        print("2. View Employees")
        print("3. Exit")
        choice = input("Choose Option: ").strip()

        if choice == "1":
            add_employee_from_input()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()