from datetime import date
from database import execute_query, fetch_all, fetch_one


def read_fee(label):
    try:
        value = float(input(label))
        if value < 0:
            print("Fee cannot be negative.")
            return None
        return value
    except ValueError:
        print("Please enter a valid amount.")
        return None


def create_bill():
    print("\n--- Create Bill ---")

    try:
        patient_id = int(input("Enter patient ID: "))
    except ValueError:
        print("Patient ID must be a number.")
        return

    patient = fetch_one("SELECT name FROM patients WHERE patient_id = ?", (patient_id,))

    if not patient:
        print("Patient not found.")
        return

    consultation_fee = read_fee("Consultation fee: ")
    if consultation_fee is None:
        return

    medicine_fee = read_fee("Medicine fee: ")
    if medicine_fee is None:
        return

    test_fee = read_fee("Test fee: ")
    if test_fee is None:
        return

    total_amount = consultation_fee + medicine_fee + test_fee
    bill_date = date.today().isoformat()

    execute_query("""
        INSERT INTO bills
        (patient_id, consultation_fee, medicine_fee, test_fee, total_amount, bill_date)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        patient_id,
        consultation_fee,
        medicine_fee,
        test_fee,
        total_amount,
        bill_date
    ))

    print(f"Bill created successfully.")
    print(f"Total amount: ₹{total_amount:.2f}")


def view_bills():
    print("\n--- Billing History ---")

    bills = fetch_all("""
        SELECT
            b.bill_id,
            p.name,
            b.consultation_fee,
            b.medicine_fee,
            b.test_fee,
            b.total_amount,
            b.bill_date
        FROM bills b
        JOIN patients p ON b.patient_id = p.patient_id
        ORDER BY b.bill_id
    """)

    if not bills:
        print("No bills found.")
        return

    for bill in bills:
        print("-" * 50)
        print(f"Bill ID          : {bill[0]}")
        print(f"Patient          : {bill[1]}")
        print(f"Consultation Fee : ₹{bill[2]:.2f}")
        print(f"Medicine Fee     : ₹{bill[3]:.2f}")
        print(f"Test Fee         : ₹{bill[4]:.2f}")
        print(f"Total Amount     : ₹{bill[5]:.2f}")
        print(f"Bill Date        : {bill[6]}")


def billing_menu():
    while True:
        print("\n========== BILLING ==========")
        print("1. Create Bill")
        print("2. View Billing History")
        print("3. Back to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            create_bill()
        elif choice == "2":
            view_bills()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")
