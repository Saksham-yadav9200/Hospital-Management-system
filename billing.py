from datetime import date
from database import execute_query, fetch_all, fetch_one


def create_bill():
    print("\n===== CREATE BILL =====")

    patient_id = input("Enter patient ID: ")

    patient = fetch_one(
        "SELECT name FROM patients WHERE patient_id = ?",
        (patient_id,)
    )

    if patient is None:
        print("Patient not found.")
        return

    try:
        consultation = float(
            input("Enter consultation fee: ₹")
        )

        medicine = float(
            input("Enter medicine fee: ₹")
        )

        test = float(
            input("Enter test fee: ₹")
        )

        if consultation < 0 or medicine < 0 or test < 0:
            print("Fees cannot be negative.")
            return

    except ValueError:
        print("Please enter valid numbers.")
        return

    total = consultation + medicine + test
    bill_date = date.today().strftime("%d-%m-%Y")

    query = """
        INSERT INTO bills
        (patient_id, consultation_fee, medicine_fee,
         test_fee, total_amount, bill_date)
        VALUES (?, ?, ?, ?, ?, ?)
    """

    execute_query(
        query,
        (
            patient_id,
            consultation,
            medicine,
            test,
            total,
            bill_date
        )
    )

    print("\nBill created successfully.")
    print(f"Patient       : {patient[0]}")
    print(f"Consultation  : ₹{consultation:.2f}")
    print(f"Medicine      : ₹{medicine:.2f}")
    print(f"Tests         : ₹{test:.2f}")
    print(f"Total         : ₹{total:.2f}")


def view_bills():
    print("\n===== BILL HISTORY =====")

    query = """
        SELECT
            b.bill_id,
            p.name,
            b.consultation_fee,
            b.medicine_fee,
            b.test_fee,
            b.total_amount,
            b.bill_date
        FROM bills b
        JOIN patients p
            ON b.patient_id = p.patient_id
        ORDER BY b.bill_id
    """

    bills = fetch_all(query)

    if not bills:
        print("No bills found.")
        return

    for bill in bills:
        print("-" * 60)
        print(f"Bill ID       : {bill[0]}")
        print(f"Patient       : {bill[1]}")
        print(f"Consultation  : ₹{bill[2]:.2f}")
        print(f"Medicine      : ₹{bill[3]:.2f}")
        print(f"Tests         : ₹{bill[4]:.2f}")
        print(f"Total         : ₹{bill[5]:.2f}")
        print(f"Date          : {bill[6]}")


def billing_menu():
    while True:
        print("\n")
        print("=" * 35)
        print("          BILLING")
        print("=" * 35)
        print("1. Create Bill")
        print("2. View Bills")
        print("3. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_bill()
        elif choice == "2":
            view_bills()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")