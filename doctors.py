from database import execute_query, fetch_all, fetch_one


def add_doctor():
    print("\n--- Add Doctor ---")

    name = input("Enter doctor name: ").strip()
    specialization = input("Enter specialization: ").strip()
    phone = input("Enter phone number: ").strip()

    if not name or not specialization or not phone:
        print("Name, specialization and phone are required.")
        return

    execute_query("""
        INSERT INTO doctors (name, specialization, phone)
        VALUES (?, ?, ?)
    """, (name, specialization, phone))

    print("Doctor added successfully.")


def view_doctors():
    print("\n--- Doctor List ---")

    doctors = fetch_all("""
        SELECT doctor_id, name, specialization, phone
        FROM doctors
        ORDER BY doctor_id
    """)

    if not doctors:
        print("No doctors found.")
        return

    for doctor in doctors:
        print("-" * 40)
        print(f"Doctor ID     : {doctor[0]}")
        print(f"Name          : {doctor[1]}")
        print(f"Specialization: {doctor[2]}")
        print(f"Phone         : {doctor[3]}")


def search_doctor():
    print("\n--- Search Doctor ---")
    keyword = input("Enter doctor name or specialization: ").strip()

    if not keyword:
        print("Search value cannot be empty.")
        return

    doctors = fetch_all("""
        SELECT doctor_id, name, specialization, phone
        FROM doctors
        WHERE name LIKE ? OR specialization LIKE ?
        ORDER BY doctor_id
    """, (f"%{keyword}%", f"%{keyword}%"))

    if not doctors:
        print("No doctor found.")
        return

    for doctor in doctors:
        print("-" * 40)
        print(f"Doctor ID     : {doctor[0]}")
        print(f"Name          : {doctor[1]}")
        print(f"Specialization: {doctor[2]}")
        print(f"Phone         : {doctor[3]}")


def doctor_menu():
    while True:
        print("\n========== DOCTOR MANAGEMENT ==========")
        print("1. Add Doctor")
        print("2. View Doctors")
        print("3. Search Doctor")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ").strip()

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
