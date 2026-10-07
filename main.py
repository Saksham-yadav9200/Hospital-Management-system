import sqlite3

# ---------- DATABASE ----------
con = sqlite3.connect("hospital.db")
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS patients(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT, age INTEGER, disease TEXT)""")

cur.execute("""CREATE TABLE IF NOT EXISTS doctors(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT, specialization TEXT)""")

cur.execute("""CREATE TABLE IF NOT EXISTS appointments(
id INTEGER PRIMARY KEY AUTOINCREMENT,
patient TEXT, doctor TEXT, date TEXT, status TEXT)""")

cur.execute("""CREATE TABLE IF NOT EXISTS bills(
id INTEGER PRIMARY KEY AUTOINCREMENT,
patient TEXT, amount REAL, date TEXT)""")

con.commit()


# ---------- 1. PATIENT ----------
def patient():
    print("\n1. Add Patient")
    print("2. View Patients")
    ch = input("Choice: ")

    if ch == "1":
        name = input("Name: ")
        age = int(input("Age: "))
        disease = input("Disease: ")

        cur.execute(
            "INSERT INTO patients(name,age,disease) VALUES(?,?,?)",
            (name, age, disease)
        )
        con.commit()
        print("Patient added.")

    elif ch == "2":
        cur.execute("SELECT * FROM patients")

        for p in cur.fetchall():
            print(p)


# ---------- 2. DOCTOR ----------
def doctor():
    print("\n1. Add Doctor")
    print("2. View Doctors")
    ch = input("Choice: ")

    if ch == "1":
        name = input("Name: ")
        specialization = input("Specialization: ")

        cur.execute(
            "INSERT INTO doctors(name,specialization) VALUES(?,?)",
            (name, specialization)
        )
        con.commit()
        print("Doctor added.")

    elif ch == "2":
        cur.execute("SELECT * FROM doctors")

        for d in cur.fetchall():
            print(d)


# ---------- 3. APPOINTMENT ----------
def appointment():
    patient_name = input("Patient name: ")
    doctor_name = input("Doctor name: ")
    date = input("Date (YYYY-MM-DD): ")

    cur.execute(
        """INSERT INTO appointments
        (patient,doctor,date,status)
        VALUES(?,?,?,'Scheduled')""",
        (patient_name, doctor_name, date)
    )

    con.commit()
    print("Appointment booked.")


# ---------- 4. BILLING ----------
def billing():
    patient_name = input("Patient name: ")

    consultation = float(input("Consultation fee: "))
    medicine = float(input("Medicine fee: "))
    test = float(input("Test fee: "))

    total = consultation + medicine + test

    cur.execute(
        "INSERT INTO bills(patient,amount,date) VALUES(?,?,date('now'))",
        (patient_name, total)
    )

    con.commit()

    print("Total Bill =", total)


# ---------- 5. REPORT ----------
def report():
    patients = cur.execute(
        "SELECT COUNT(*) FROM patients"
    ).fetchone()[0]

    doctors = cur.execute(
        "SELECT COUNT(*) FROM doctors"
    ).fetchone()[0]

    appointments = cur.execute(
        "SELECT COUNT(*) FROM appointments"
    ).fetchone()[0]

    bills = cur.execute(
        "SELECT COALESCE(SUM(amount),0) FROM bills"
    ).fetchone()[0]

    print("\n========== HOSPITAL REPORT ==========")
    print("Total Patients     :", patients)
    print("Total Doctors      :", doctors)
    print("Total Appointments :", appointments)
    print("Total Billing      :", bills)


# ---------- MAIN MENU ----------
while True:

    print("\n================================")
    print("   HOSPITAL MANAGEMENT SYSTEM")
    print("================================")
    print("1. Patient Management")
    print("2. Doctor Management")
    print("3. Appointment Management")
    print("4. Billing")
    print("5. Hospital Report")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        patient()

    elif choice == "2":
        doctor()

    elif choice == "3":
        appointment()

    elif choice == "4":
        billing()

    elif choice == "5":
        report()

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")

con.close()