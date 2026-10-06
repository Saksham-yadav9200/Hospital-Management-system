from database import execute_query, fetch_all, fetch_one


def add_patient():
    print("\n--- Add Patient ---")

    name = input("Enter patient name: ").strip()
    if not name:
        print("Patient name cannot be empty.")
        return

    try:
        age = int(input("Enter patient age: "))
        if age <= 0 or age > 120:
            print("Age must be between 1 and 120.")
            return
    except ValueError:
        print("Age must be a number.")
        return

    gender = input("Enter gender: ").strip()
    phone = input("Enter phone number: ").strip()
    address = input("Enter address: ").strip()
    disease = input("Enter disease: ").strip()

    query = """
        INSERT INTO patients
        (name, age, gender, phone, address, disease)
        VALUES (?, ?, ?, ?, ?, ?)
    """

    execute_query(query, (name, age, gender, phone, address, disease))
    print("Patient added successfully.")


def view_patients():
    print("\n--- Patient List ---")

    patients = fetch_all("""
        SELECT patient_id, name, age, gender, phone, address, disease
        FROM patients
        ORDER BY patient_id
    """)

    if not patients:
        print("No patients found.")
        return

    for patient in patients:
        print("-" * 40)
        print(f"Patient ID : {patient[0]}")
        print(f"Name       : {patient[1]}")
        print(f"Age        : {patient[2]}")
        print(f"Gender     : {patient[3]}")
        print(f"Phone      : {patient[4]}")
        print(f"Address    : {patient[5] or '-'}")
        print(f"Disease    : {patient[6] or '-'}")


def search_patient():
    print("\n--- Search Patient ---")
    keyword = input("Enter patient name or ID: ").strip()

    if not keyword:
        print("Search value cannot be empty.")
        return

    if keyword.isdigit():
        patients = fetch_all("""
            SELECT patient_id, name, age, gender, phone, address, disease
            FROM patients
            WHERE patient_id = ?
        """, (int(keyword),))
    else:
        patients = fetch_all("""
            SELECT patient_id, name, age, gender, phone, address, disease
            FROM patients
            WHERE name LIKE ?
        """, (f"%{keyword}%",))

    if not patients:
        print("No patient found.")
        return

    for patient in patients:
        print("-" * 40)
        print(f"Patient ID : {patient[0]}")
        print(f"Name       : {patient[1]}")
        print(f"Age        : {patient[2]}")
        print(f"Gender     : {patient[3]}")
        print(f"Phone      : {patient[4]}")
        print(f"Address    : {patient[5] or '-'}")
        print(f"Disease    : {patient[6] or '-'}")


def update_patient():
    print("\n--- Update Patient ---")

    try:
        patient_id = int(input("Enter patient ID: "))
    except ValueError:
        print("Patient ID must be a number.")
        return

    patient = fetch_one("SELECT * FROM patients WHERE patient_id = ?", (patient_id,))
    if not patient:
        print("Patient not found.")
        return

    name = input(f"Name [{patient[1]}]: ").strip() or patient[1]
    age_input = input(f"Age [{patient[2]}]: ").strip()
    gender = input(f"Gender [{patient[3]}]: ").strip() or patient[3]
    phone = input(f"Phone [{patient[4]}]: ").strip() or patient[4]
    address = input(f"Address [{patient[5] or ''}]: ").strip() or patient[5]
    disease = input(f"Disease [{patient[6] or ''}]: ").strip() or patient[6]

    if age_input:
        try:
            age = int(age_input)
            if age <= 0 or age > 120:
                print("Age must be between 1 and 120.")
                return
        except ValueError:
            print("Age must be a number.")
            return
    else:
        age = patient[2]

    execute_query("""
        UPDATE patients
        SET name = ?, age = ?, gender = ?, phone = ?, address = ?, disease = ?
        WHERE patient_id = ?
    """, (name, age, gender, phone, address, disease, patient_id))

    print("Patient updated successfully.")


def delete_patient():
    print("\n--- Delete Patient ---")

    try:
        patient_id = int(input("Enter patient ID: "))
    except ValueError:
        print("Patient ID must be a number.")
        return

    patient = fetch_one("SELECT * FROM patients WHERE patient_id = ?", (patient_id,))
    if not patient:
        print("Patient not found.")
        return

    print(f"Patient: {patient[1]} (ID {patient[0]})")
    confirmation = input("Are you sure? (y/n): ").strip().lower()

    if confirmation != "y":
        print("Delete cancelled.")
        return

    try:
        execute_query("DELETE FROM patients WHERE patient_id = ?", (patient_id,))
        print("Patient deleted successfully.")
    except Exception as error:
        print("Patient could not be deleted.")
        print("Reason:", error)


def patient_menu():
    while True:
        print("\n========== PATIENT MANAGEMENT ==========")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Search Patient")
        print("4. Update Patient")
        print("5. Delete Patient")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ").strip()

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
