# Basic clinic system

import sqlite3  # Library to interact with DB

# Database connection
conn = sqlite3.connect("middlemore")  # Creates db if does not exist
cursor = conn.cursor()


class Specialisation:
    def __init__(self, specialisation_id, specialisation_title):
        self.specialisation_id = specialisation_id
        self.specialisation_title = specialisation_title

    def save(self):
        cursor.execute(
            """INSERT INTO specialisation(specialisation_id, specialisation_title) VALUES(?,?) """,
            (self.specialisation_id, self.specialisation_title),
        )
        conn.commit()


class Patients:
    def __init__(
        self,
        Patient_id,
        Patient_fname,
        Patient_lname,
        Patient_age,
        Patient_email,
        Patient_contact,
    ):
        self.patient_id = Patient_id
        self.Patient_fname = Patient_fname
        self.Patient_lname = Patient_lname
        self.Patient_age = Patient_age
        self.Patient_email = Patient_email
        self.Patient_contact = Patient_contact

    def save(self):
        cursor.execute(
            """INSERT INTO Patients (Patient_id, Patient_fname, Patient_lname, Patient_age, Patient_email, Patient_contact) VALUES(?,?,?,?,?,?)""",
            (
                self.patient_id,
                self.Patient_fname,
                self.Patient_lname,
                self.Patient_age,
                self.Patient_email,
                self.Patient_contact,
            ),
        )
        conn.commit()


class Doctors:
    def __init__(
        self,
        Doctor_id,
        Doctor_fname,
        Doctor_lname,
        Doctor_email,
        Doctor_phone,
        Specialisation_id,
    ):
        self.Doctor_id = Doctor_id
        self.Doctor_fname = Doctor_fname
        self.Doctor_lname = Doctor_lname
        self.Doctor_email = Doctor_email
        self.Doctor_phone = Doctor_phone
        self.Specialisation_id = Specialisation_id

    def save(self):
        cursor.execute(
            """INSERT INTO Doctors(Doctor_id, Doctor_fname, Doctor_lname, Doctor_email, Doctor_phone, Specialisation_id) VALUES(?,?,?,?,?,?)""",
            (
                self.Doctor_id,
                self.Doctor_fname,
                self.Doctor_lname,
                self.Doctor_email,
                self.Doctor_phone,
                self.Specialisation_id,
            ),
        )
        conn.commit()


class Appointments:
    def __init__(self, Appointment_id, Doctor_id, Patient_id, Date, Time, Status):

        self.Appointment_id = Appointment_id
        self.Doctor_id = Doctor_id
        self.Patient_id = Patient_id
        self.Date = Date
        self.Time = Time
        self.Status = Status

    def save(self):
        cursor.execute(
            """INSERT INTO Appointments (Appointment_id, Doctor_id, Patient_id, Date, Time, Status) VALUES(?,?,?,?,?,?)""",
            (
                self.Appointment_id,
                self.Doctor_id,
                self.Patient_id,
                self.Date,
                self.Time,
                self.Status,
            ),
        )
        conn.commit()


# Creating tables if does not exisit
# Specialisation table
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS Specialisation (
    specialisation_id INTEGER PRIMARY KEY,
    specialisation_title TEXT
)
"""
)

# Patient table
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS Patients (
    Patient_id INTEGER PRIMARY KEY,
    Patient_fname TEXT,
    Patient_lname TEXT,
    Patient_age INTEGER,
    Patient_email TEXT,
    Patient_contact TEXT
)
"""
)

# Doctors table
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS Doctors (
    Doctor_id INTEGER PRIMARY KEY,
    Doctor_fname TEXT,
    Doctor_lname TEXT,
    Doctor_email TEXT,
    Doctor_phone TEXT,
    Specialisation_id INTEGER,
    FOREIGN KEY (Specialisation_id) REFERENCES Specialisation(specialisation_id)
)
"""
)

# Appointments table
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS Appointments (
    Appointment_id INTEGER PRIMARY KEY,
    Doctor_id INTEGER,
    Patient_id INTEGER,
    Date TEXT,
    Time TEXT,
    Status TEXT,
    FOREIGN KEY (Doctor_id) REFERENCES Doctors(Doctor_id),
    FOREIGN KEY (Patient_id) REFERENCES Patient(Patient_id)
)
"""
)
conn.commit()

cursor.execute("DELETE FROM Specialisation")
conn.commit()
cursor.execute("DELETE FROM Doctors")
conn.commit()
cursor.execute("DELETE FROM Patients")
conn.commit()
cursor.execute("DELETE FROM Appointments")
conn.commit()

# Inserting Sample data
# Specialisations
s1 = Specialisation(1, "Ophthalmology")
s1.save()
s2 = Specialisation(2, "Cardiology")
s2.save()

# Doctors
d1 = Doctors(1, "John", "Smith", "john@clinic.com", "12345", 1)
d1.save()
d2 = Doctors(2, "Alice", "Brown", "alice@clinic.com", "67890", 2)
d2.save()

# Patients
p1 = Patients(1, "Michael", "Johnson", 70, "michael@mail.com", "555111")
p1.save()
p2 = Patients(2, "Sara", "Williams", 60, "sara@mail.com", "555222")
p2.save()
p3 = Patients(3, "George", "Miller", 68, "george@mail.com", "555333")
p3.save()

print("Patients with age over 65:")
cursor.execute("SELECT * FROM Patients WHERE Patient_age > 65")
Aged = cursor.fetchall()
for patient in Aged:
    print(patient)

    # Count Doctors in Ophthalmology
print("Total number of Doctors specialised in Ophthalmology")
cursor.execute(
    """
SELECT COUNT(*)
FROM Doctors d
JOIN Specialisation s ON d.Specialisation_id = s.specialisation_id
WHERE s.specialisation_title = 'Ophthalmology'
"""
)
ophthalmology_count = cursor.fetchone()[0]
print("Total Ophthalmology Doctors:", ophthalmology_count)
