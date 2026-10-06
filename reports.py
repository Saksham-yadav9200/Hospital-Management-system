from database import fetch_one


def show_report():
    print("\n========== HOSPITAL SUMMARY REPORT ==========")

    total_patients = fetch_one(
        "SELECT COUNT(*) FROM patients"
    )[0]

    total_doctors = fetch_one(
        "SELECT COUNT(*) FROM doctors"
    )[0]

    total_appointments = fetch_one(
        "SELECT COUNT(*) FROM appointments"
    )[0]

    scheduled_appointments = fetch_one("""
        SELECT COUNT(*)
        FROM appointments
        WHERE status = 'Scheduled'
    """)[0]

    cancelled_appointments = fetch_one("""
        SELECT COUNT(*)
        FROM appointments
        WHERE status = 'Cancelled'
    """)[0]

    total_billing = fetch_one("""
        SELECT COALESCE(SUM(total_amount), 0)
        FROM bills
    """)[0]

    print(f"Total Patients          : {total_patients}")
    print(f"Total Doctors           : {total_doctors}")
    print(f"Total Appointments      : {total_appointments}")
    print(f"Scheduled Appointments  : {scheduled_appointments}")
    print(f"Cancelled Appointments  : {cancelled_appointments}")
    print(f"Total Billing           : ₹{total_billing:.2f}")
    print("=" * 46)
