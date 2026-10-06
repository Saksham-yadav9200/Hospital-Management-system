import sqlite3

DATABASE_NAME = "hospital.db"


def get_connection():
    return sqlite3.connect(DATABASE_NAME)


def create_tables():
    connection = get_connection()
    cursor = connection.cursor()

    # Patients table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS patients (
            patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            gender TEXT NOT NULL,
            phone TEXT NOT NULL,
            address TEXT,
            disease TEXT
        )
    """)

    # Doctors table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS doctors (
            doctor_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            specialization TEXT NOT NULL,
            phone TEXT NOT NULL
        )
    """)

    # Appointments table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS appointments (
            appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER NOT NULL,
            doctor_id INTEGER NOT NULL,
            appointment_date TEXT NOT NULL,
            appointment_time TEXT NOT NULL,
            reason TEXT,
            status TEXT DEFAULT 'Scheduled',
            FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
            FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)
        )
    """)

    # Bills table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bills (
            bill_id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER NOT NULL,
            consultation_fee REAL DEFAULT 0,
            medicine_fee REAL DEFAULT 0,
            test_fee REAL DEFAULT 0,
            total_amount REAL DEFAULT 0,
            bill_date TEXT NOT NULL,
            FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
        )
    """)

    connection.commit()
    connection.close()


def execute_query(query, parameters=()):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(query, parameters)

    connection.commit()
    connection.close()


def fetch_all(query, parameters=()):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(query, parameters)
    records = cursor.fetchall()

    connection.close()

    return records


def fetch_one(query, parameters=()):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(query, parameters)
    record = cursor.fetchone()

    connection.close()

    return record