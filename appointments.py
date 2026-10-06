from database import execute_query, fetch_all, fetch_one


def book_appointment():
    print("\n--- Book Appointment ---")

    try:
        patient_id = int(input("Enter patient ID: "))
        doctor_id = int(input("Enter doctor ID: "))
    except ValueError:
        print("Patient ID and Doctor ID must be numbers.")
        return

    patient = fetch_one("SELECT name FROM patients WHERE patient_id = ?", (patient_id,))
    doctor = fetch_one("SELECT name FROM doctors WHERE doctor_id = ?", (doctor_id,))

    if not patient:
        print("Patient not found.")
        return

    if not doctor:
        print("Doctor not found.")
        return

    appointment_date = input("Enter appointment date (YYYY-MM-DD): ").strip()
    appointment_time = input("Enter appointment time (HH:MM): ").strip()
    reason = input("Enter reason: ").strip()

    if not appointment_date or not appointment_time:
        print("Date and time are required.")
        return

    execute_query("""
        INSERT INTO appointments
        (patient_id, doctor_id, appointment_date, appointment_time, reason, status)
        VALUES (?, ?, ?, ?, ?, 'Scheduled')
    """, (patient_id, doctor_id, appointment_date, appointment_time, reason))

    print("Appointment booked successfully.")


def view_appointments():
    print("\n--- Appointment List ---")

    appointments = fetch_all("""
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
        JOIN patients p ON a.patient_id = p.patient_id
        JOIN doctors d ON a.doctor_id = d.doctor_id
        ORDER BY a.appointment_id
    """)

    if not appointments:
        print("No appointments found.")
        return

    for appointment in appointments:
        print("-" * 50)
        print(f"Appointment ID : {appointment[0]}")
        print(f"Patient        : {appointment[1]}")
        print(f"Doctor         : {appointment[2]}")
        print(f"Specialization : {appointment[3]}")
        print(f"Date           : {appointment[4]}")
        print(f"Time           : {appointment[5]}")
        print(f"Reason         : {appointment[6] or '-'}")
        print(f"Status         : {appointment[7]}")


def cancel_appointment():
    print("\n--- Cancel Appointment ---")

    try:
        appointment_id = int(input("Enter appointment ID: "))
    except ValueError:
        print("Appointment ID must be a number.")
        return

    appointment = fetch_one("""
        SELECT status
        FROM appointments
        WHERE appointment_id = ?
    """, (appointment_id,))

    if not appointment:
        print("Appointment not found.")
        return

    if appointment[0] == "Cancelled":
        print("Appointment is already cancelled.")
        return

    execute_query("""
        UPDATE appointments
        SET status = 'Cancelled'
        WHERE appointment_id = ?
    """, (appointment_id,))

    print("Appointment cancelled successfully.")


def appointment_menu():
    while True:
        print("\n========== APPOINTMENT MANAGEMENT ==========")
        print("1. Book Appointment")
        print("2. View Appointments")
        print("3. Cancel Appointment")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ").strip()

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

