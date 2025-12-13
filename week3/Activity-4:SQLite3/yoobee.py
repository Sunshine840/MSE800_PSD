import sqlite3  # Importring

conn = sqlite3.connect("Yoobee")  # database name
cursor = conn.cursor()  # Connecting with db


# Here is our student class
class Student:
    def __init__(self, studentId, fname, lname, email):  # Constructor
        self.studentId = studentId
        self.fname = fname
        self.lname = lname
        self.email = email

    # Method to save data to db
    def save(self):
        cursor.execute(
            """INSERT INTO STUDENT(studentId, fname, lname, email) VALUES (?,?,?,?)""",
            (self.studentId, self.fname, self.lname, self.email),
        )
        conn.commit()


class Teachers:  # Teacher Class
    def __init__(self, Teacherid, Teacher_lname, Teacher_fname, teacher_email):
        self.teacherId = Teacherid
        self.lname = Teacher_lname
        self.fname = Teacher_fname
        self.email = teacher_email

    def save(self):  # Method
        cursor.execute(
            "INSERT INTO TEACHERS(teacherId, Teacher_fname, Teacher_lname, teacher_email) VALUES (?, ?, ?, ?)",
            (self.teacherId, self.fname, self.lname, self.email),
        )

    conn.commit()  # we are also taking care of sql injection here by using ??


class Course:
    def __init__(self, courseId, course_name, course_credits, course_major, teacherid):
        self.courseId = courseId
        self.name = course_name
        self.credits = course_credits
        self.major = course_major
        self.teacher = teacherid

    def save(self):
        cursor.execute(
            "INSERT INTO COURSE(course_id, course_name, course_credits, course_major, offered_by) VALUES (?, ?, ?, ?, ?)",
            (self.courseId, self.name, self.credits, self.major, self.teacher),
        )
        conn.commit()


class EnrollsIn:
    def __init__(self, studentId, courseId):
        self.studentId = studentId
        self.courseId = courseId

    def save(self):
        cursor.execute(
            """
            INSERT INTO ENROLLS_IN (studentId, courseId)
            VALUES (?, ?)
        """,
            (self.studentId, self.courseId),
        )
        conn.commit()


# Creating student table
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS STUDENT (
    studentId INTEGER PRIMARY KEY,
    fname TEXT NOT NULL,
    lname TEXT NOT NULL,
    email TEXT UNIQUE
)
"""
)

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS TEACHERS (
    teacherId INTEGER PRIMARY KEY,
    Teacher_fname TEXT NOT NULL,
    Teacher_lname TEXT NOT NULL,
    teacher_email TEXT UNIQUE
)
"""
)

# Creating course table
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS COURSE (
    course_id INTEGER PRIMARY KEY,
    course_name TEXT NOT NULL,
    course_credits INTEGER,
    course_major TEXT,
    offered_by INTEGER,
    FOREIGN KEY (offered_by) REFERENCES TEACHERS(teacherId)
)
"""
)
# ENROLLS_IN table (many-to-many relationship)
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS ENROLLS_IN (
    studentId INTEGER,
    courseId INTEGER,
    PRIMARY KEY (studentId, courseId),
    FOREIGN KEY (studentId) REFERENCES STUDENT(studentId),
    FOREIGN KEY (courseId) REFERENCES COURSE(course_id)
)
"""
)

# Commit table creation
conn.commit()

print("All tables created successfully!")

# Adding sample data
# ---- Students ----
s1 = Student(200, "John", "Doe", "john@example.com")
s2 = Student(201, "Alice", "Smith", "alice@example.com")
s3 = Student(202, "Bob", "Johnson", "bob@example.com")

s1.save()
s2.save()
s3.save()

# ---- Teachers ----
t1 = Teachers(301, "Dr.", "Brown", "brown@yoobee.edu")
t2 = Teachers(302, "Prof.", "Green", "green@yoobee.edu")

t1.save()
t2.save()

# ---- Courses ----
c1 = Course(800, "MSE800", 3, "PSE", 301)
c2 = Course(801, "MSE801", 4, "QC", 302)
c3 = Course(802, "MSE802", 3, "RM", 301)

c1.save()
c2.save()
c3.save()

# ---- Enrollments ----
e1 = EnrollsIn(200, 800)
e2 = EnrollsIn(201, 801)
e3 = EnrollsIn(202, 802)
e4 = EnrollsIn(200, 801)

e1.save()
e2.save()
e3.save()
e4.save()

print("Sample data added successfully!")

# Number of students in MSE801
cursor.execute(
    """
SELECT COUNT(studentId)
FROM ENROLLS_IN
JOIN COURSE ON ENROLLS_IN.courseId = COURSE.course_id
WHERE COURSE.course_name = 'MSE801'
"""
)
num_students = cursor.fetchone()[0]
print(f"Number of students in MSE801: {num_students}")

# List all teachers for MSE801
cursor.execute(
    """
SELECT TEACHERS.Teacher_fname, TEACHERS.Teacher_lname
FROM COURSE
JOIN TEACHERS ON COURSE.offered_by = TEACHERS.teacherId
WHERE COURSE.course_name = 'MSE801'
"""
)
teachers = cursor.fetchall()
print("Teachers for MSE801:")
for t in teachers:  # using for loop here
    print(f"{t[0]} {t[1]}")  # index 0 (fname) and index 1(lname)

conn.close()  # connection close
