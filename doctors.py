from database import execute_query, fetch_all, fetch_one


def add_doctor():
    print("\n===== ADD DOCTOR =====")

    name = input("Enter doctor name: ").strip()
    specialization = input("Enter specialization: ").strip()
    phone = input("Enter phone number: ").strip()

    if not name or not specialization or not phone:
        print("All fields are required.")
        return

    query = """
        INSERT INTO doctors
        (name, specialization, phone)
        VALUES (?, ?, ?)
    """

    execute_query(
        query,
        (name, specialization, phone)
    )

    print("Doctor added successfully.")


def view_doctors():
    print("\n===== DOCTOR LIST =====")

    doctors = fetch_all("""
        SELECT doctor_id, name, specialization, phone
        FROM doctors
        ORDER BY doctor_id
    """)

    if not doctors:
        print("No doctors found.")
        return

    for doctor in doctors:
        print("-" * 50)
        print(f"Doctor ID     : {doctor[0]}")
        print(f"Name          : {doctor[1]}")
        print(f"Specialization: {doctor[2]}")
        print(f"Phone         : {doctor[3]}")


def search_doctor():
    print("\n===== SEARCH DOCTOR =====")

    doctor_id = input("Enter doctor ID: ")

    doctor = fetch_one("""
        SELECT doctor_id, name, specialization, phone
        FROM doctors
        WHERE doctor_id = ?
    """, (doctor_id,))

    if doctor is None:
        print("Doctor not found.")
        return

    print(f"\nDoctor ID     : {doctor[0]}")
    print(f"Name          : {doctor[1]}")
    print(f"Specialization: {doctor[2]}")
    print(f"Phone         : {doctor[3]}")


def doctor_menu():
    while True:
        print("\n")
        print("=" * 35)
        print("        DOCTOR MANAGEMENT")
        print("=" * 35)
        print("1. Add Doctor")
        print("2. View Doctors")
        print("3. Search Doctor")
        print("4. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_doctor()
        elif choice == "2":
            view_doctors()
        elif choice == "3":
            search_doctor()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")