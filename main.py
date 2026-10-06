from database import create_tables
from patients import patient_menu
from doctors import doctor_menu
from appointments import appointment_menu
from billing import billing_menu
from reports import show_report


def main():
    create_tables()

    while True:
        print("\n" + "=" * 45)
        print("       HOSPITAL MANAGEMENT SYSTEM")
        print("=" * 45)
        print("1. Patient Management")
        print("2. Doctor Management")
        print("3. Appointment Management")
        print("4. Billing")
        print("5. Hospital Report")
        print("6. Exit")
        print("=" * 45)

        choice = input("Enter your choice: ").strip()

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
            print("Thank you for using the Hospital Management System.")
            break
        else:
            print("Invalid choice. Please enter 1-6.")


if __name__ == "__main__":
    main()
