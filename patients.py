from database import execute_query, fetch_all, fetch_one


def add_patient():
    print("\n===== ADD PATIENT =====")

    name = input("Enter patient name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    try:
        age = int(input("Enter age: "))

        if age <= 0 or age > 120:
            print("Please enter a valid age.")
            return

    except ValueError:
        print("Age must be a number.")
        return

    gender = input("Enter gender: ").strip()
    phone = input("Enter phone number: ").strip()
    address = input("Enter address: ").strip()
    disease = input("Enter disease/problem: ").strip()

    query = """
        INSERT INTO patients
        (name, age, gender, phone, address, disease)
        VALUES (?, ?, ?, ?, ?, ?)
    """

    execute_query(
        query,
        (name, age, gender, phone, address, disease)
    )

    print("Patient added successfully.")


def view_patients():
    print("\n===== PATIENT LIST =====")

    query = """
        SELECT patient_id, name, age, gender,
               phone, address, disease
        FROM patients
        ORDER BY patient_id
    """

    patients = fetch_all(query)

    if not patients:
        print("No patients found.")
        return

    for patient in patients:
        print("-" * 60)
        print(f"Patient ID : {patient[0]}")
        print(f"Name       : {patient[1]}")
        print(f"Age        : {patient[2]}")
        print(f"Gender     : {patient[3]}")
        print(f"Phone      : {patient[4]}")
        print(f"Address    : {patient[5]}")
        print(f"Disease    : {patient[6]}")


def search_patient():
    print("\n===== SEARCH PATIENT =====")

    patient_id = input("Enter patient ID: ")

    query = """
        SELECT patient_id, name, age, gender,
               phone, address, disease
        FROM patients
        WHERE patient_id = ?
    """

    patient = fetch_one(query, (patient_id,))

    if patient is None:
        print("Patient not found.")
        return

    print("\nPatient Details")
    print("-------------------------")
    print(f"Patient ID : {patient[0]}")
    print(f"Name       : {patient[1]}")
    print(f"Age        : {patient[2]}")
    print(f"Gender     : {patient[3]}")
    print(f"Phone      : {patient[4]}")
    print(f"Address    : {patient[5]}")
    print(f"Disease    : {patient[6]}")


def update_patient():
    print("\n===== UPDATE PATIENT =====")

    patient_id = input("Enter patient ID: ")

    patient = fetch_one(
        "SELECT * FROM patients WHERE patient_id = ?",
        (patient_id,)
    )

    if patient is None:
        print("Patient not found.")
        return

    name = input("Enter new name: ").strip()
    phone = input("Enter new phone: ").strip()
    address = input("Enter new address: ").strip()
    disease = input("Enter new disease: ").strip()

    query = """
        UPDATE patients
        SET name = ?, phone = ?, address = ?, disease = ?
        WHERE patient_id = ?
    """

    execute_query(
        query,
        (name, phone, address, disease, patient_id)
    )

    print("Patient updated successfully.")


def delete_patient():
    print("\n===== DELETE PATIENT =====")

    patient_id = input("Enter patient ID: ")

    patient = fetch_one(
        "SELECT * FROM patients WHERE patient_id = ?",
        (patient_id,)
    )

    if patient is None:
        print("Patient not found.")
        return

    confirm = input(
        "Are you sure you want to delete this patient? (y/n): "
    ).lower()

    if confirm == "y":
        execute_query(
            "DELETE FROM patients WHERE patient_id = ?",
            (patient_id,)
        )

        print("Patient deleted successfully.")
    else:
        print("Delete operation cancelled.")


def patient_menu():
    while True:
        print("\n")
        print("=" * 35)
        print("       PATIENT MANAGEMENT")
        print("=" * 35)
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Search Patient")
        print("4. Update Patient")
        print("5. Delete Patient")
        print("6. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_patient()
        elif choice == "2":
            view_patients()
        elif choice == "3":
            search_patient()
        elif choice == "4":
            update_patient()
        elif choice == "5":
            delete_patient()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")