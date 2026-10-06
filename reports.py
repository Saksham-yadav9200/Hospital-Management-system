from database import fetch_one


def show_report():
    print("\n")
    print("=" * 40)
    print("       HOSPITAL SUMMARY REPORT")
    print("=" * 40)

    patient_count = fetch_one(
        "SELECT COUNT(*) FROM patients"
    )[0]

    doctor_count = fetch_one(
        "SELECT COUNT(*) FROM doctors"
    )[0]

    appointment_count = fetch_one(
        "SELECT COUNT(*) FROM appointments"
    )[0]

    scheduled_count = fetch_one(
        """
        SELECT COUNT(*)
        FROM appointments
        WHERE status = 'Scheduled'
        """
    )[0]

    cancelled_count = fetch_one(
        """
        SELECT COUNT(*)
        FROM appointments
        WHERE status = 'Cancelled'
        """
    )[0]

    total_revenue = fetch_one(
        "SELECT COALESCE(SUM(total_amount), 0) FROM bills"
    )[0]

    print(f"Total Patients       : {patient_count}")
    print(f"Total Doctors        : {doctor_count}")
    print(f"Total Appointments   : {appointment_count}")
    print(f"Scheduled Appointments: {scheduled_count}")
    print(f"Cancelled Appointments: {cancelled_count}")
    print(f"Total Billing        : ₹{total_revenue:.2f}")

    print("=" * 40)