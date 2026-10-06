from database import create_tables

from patients import patient_menu
from doctors import doctor_menu
from appointments import appointment_menu
from billing import billing_menu
from reports import show_report


def display_main_menu():
    print("\n")
    print("=" * 45)
    print("       HOSPITAL MANAGEMENT SYSTEM")
    print("=" * 45)
    print("1. Patient Management")
    print("2. Doctor Management")
    print("3. Appointment Management")
    print("4. Billing")
    print("5. Hospital Report")
    print("6. Exit")
    print("=" * 45)


def main():
    create_tables()

    print("\nHospital Management System Started")
    print("Database initialized successfully.")

    while True:
        display_main_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            patient_menu()

        elif choice == "2":
            doctor_menu()

        elif choice == "3":
            appointment_menu()

        elif choice == "4":
            billing_menu()

        elif choice == "5":
            show_report()

        elif choice == "6":
            print("\nThank you for using Hospital Management System.")
            break

        else:
            print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()