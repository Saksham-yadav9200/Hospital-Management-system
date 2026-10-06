from database import execute_query, fetch_all, fetch_one


def book_appointment():
    print("\n===== BOOK APPOINTMENT =====")

    patient_id = input("Enter patient ID: ")
    doctor_id = input("Enter doctor ID: ")

    patient = fetch_one(
        "SELECT name FROM patients WHERE patient_id = ?",
        (patient_id,)
    )

    doctor = fetch_one(
        "SELECT name FROM doctors WHERE doctor_id = ?",
        (doctor_id,)
    )

    if patient is None:
        print("Patient not found.")
        return

    if doctor is None:
        print("Doctor not found.")
        return

    date = input("Enter appointment date (DD-MM-YYYY): ")
    time = input("Enter appointment time (HH:MM): ")
    reason = input("Enter reason for appointment: ")

    query = """
        INSERT INTO appointments
        (patient_id, doctor_id, appointment_date,
         appointment_time, reason, status)
        VALUES (?, ?, ?, ?, ?, ?)
    """

    execute_query(
        query,
        (
            patient_id,
            doctor_id,
            date,
            time,
            reason,
            "Scheduled"
        )
    )

    print("Appointment booked successfully.")


def view_appointments():
    print("\n===== APPOINTMENTS =====")

    query = """
        SELECT
            a.appointment_id,
            p.name,
            d.name,
            d.specialization,
            a.appointment_date,
            a.appointment_time,
            a.reason,
            a.status
        FROM appointments a
        JOIN patients p
            ON a.patient_id = p.patient_id
        JOIN doctors d
            ON a.doctor_id = d.doctor_id
        ORDER BY a.appointment_id
    """

    appointments = fetch_all(query)

    if not appointments:
        print("No appointments found.")
        return

    for appointment in appointments:
        print("-" * 70)
        print(f"Appointment ID : {appointment[0]}")
        print(f"Patient        : {appointment[1]}")
        print(f"Doctor         : {appointment[2]}")
        print(f"Specialization : {appointment[3]}")
        print(f"Date           : {appointment[4]}")
        print(f"Time           : {appointment[5]}")
        print(f"Reason         : {appointment[6]}")
        print(f"Status         : {appointment[7]}")


def cancel_appointment():
    print("\n===== CANCEL APPOINTMENT =====")

    appointment_id = input("Enter appointment ID: ")

    appointment = fetch_one(
        "SELECT * FROM appointments WHERE appointment_id = ?",
        (appointment_id,)
    )

    if appointment is None:
        print("Appointment not found.")
        return

    execute_query(
        """
        UPDATE appointments
        SET status = 'Cancelled'
        WHERE appointment_id = ?
        """,
        (appointment_id,)
    )

    print("Appointment cancelled successfully.")


def appointment_menu():
    while True:
        print("\n")
        print("=" * 35)
        print("     APPOINTMENT MANAGEMENT")
        print("=" * 35)
        print("1. Book Appointment")
        print("2. View Appointments")
        print("3. Cancel Appointment")
        print("4. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            book_appointment()
        elif choice == "2":
            view_appointments()
        elif choice == "3":
            cancel_appointment()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")