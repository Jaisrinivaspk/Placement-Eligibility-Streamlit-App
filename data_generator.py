#IMPORT LIBRARIES AND SETUP

from faker import Faker
import random
import sqlite3
import os

# Initialize Faker
fake = Faker()

# Path to database
db_path = os.path.join("data", "students.db")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

#CREATE TABLES

# Drop tables if they already exist (for reruns)
cursor.execute("DROP TABLE IF EXISTS Students")
cursor.execute("DROP TABLE IF EXISTS Programming")
cursor.execute("DROP TABLE IF EXISTS SoftSkills")
cursor.execute("DROP TABLE IF EXISTS Placements")

# Students Table
cursor.execute('''
CREATE TABLE Students (
    student_id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    gender TEXT,
    email TEXT,
    phone TEXT,
    enrollment_year INTEGER,
    course_batch TEXT,
    city TEXT,
    graduation_year INTEGER
)
''')

# Programming Table
cursor.execute('''
CREATE TABLE Programming (
    programming_id INTEGER PRIMARY KEY,
    student_id INTEGER,
    language TEXT,
    problems_solved INTEGER,
    assessments_completed INTEGER,
    mini_projects INTEGER,
    certifications_earned INTEGER,
    latest_project_score REAL,
    FOREIGN KEY(student_id) REFERENCES Students(student_id)
)
''')

# Soft Skills Table
cursor.execute('''
CREATE TABLE SoftSkills (
    soft_skill_id INTEGER PRIMARY KEY,
    student_id INTEGER,
    communication INTEGER,
    teamwork INTEGER,
    presentation INTEGER,
    leadership INTEGER,
    critical_thinking INTEGER,
    interpersonal_skills INTEGER,
    FOREIGN KEY(student_id) REFERENCES Students(student_id)
)
''')

# Placements Table
cursor.execute('''
CREATE TABLE Placements (
    placement_id INTEGER PRIMARY KEY,
    student_id INTEGER,
    mock_interview_score INTEGER,
    internships_completed INTEGER,
    placement_status TEXT,
    company_name TEXT,
    placement_package REAL,
    interview_rounds_cleared INTEGER,
    placement_date TEXT,
    FOREIGN KEY(student_id) REFERENCES Students(student_id)
)
''')


#GENERATE FAKE DATA AND INSERT INTO TABLES

genders = ['Male', 'Female', 'Other']
languages = ['Python', 'SQL', 'Java']

for i in range(100):
    # --- Students Table ---
    name = fake.name()
    age = random.randint(20, 25)
    gender = random.choice(genders)
    email = fake.email()
    phone = fake.phone_number()
    enrollment_year = random.randint(2019, 2022)
    course_batch = "DS Batch " + str(random.randint(1, 5))
    city = fake.city()
    graduation_year = enrollment_year + 3

    cursor.execute('''
        INSERT INTO Students (name, age, gender, email, phone, enrollment_year, course_batch, city, graduation_year)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (name, age, gender, email, phone, enrollment_year, course_batch, city, graduation_year))

    student_id = cursor.lastrowid

    # --- Programming Table ---
    cursor.execute('''
        INSERT INTO Programming (student_id, language, problems_solved, assessments_completed, mini_projects, certifications_earned, latest_project_score)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        student_id,
        random.choice(languages),
        random.randint(20, 100),
        random.randint(1, 10),
        random.randint(0, 5),
        random.randint(0, 3),
        round(random.uniform(50, 100), 2)
    ))

    # --- Soft Skills Table ---
    cursor.execute('''
        INSERT INTO SoftSkills (student_id, communication, teamwork, presentation, leadership, critical_thinking, interpersonal_skills)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        student_id,
        random.randint(60, 100),
        random.randint(60, 100),
        random.randint(60, 100),
        random.randint(60, 100),
        random.randint(60, 100),
        random.randint(60, 100)
    ))

    # --- Placements Table ---
    cursor.execute('''
        INSERT INTO Placements (student_id, mock_interview_score, internships_completed, placement_status, company_name, placement_package, interview_rounds_cleared, placement_date)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        student_id,
        random.randint(50, 100),
        random.randint(0, 3),
        random.choice(['Ready', 'Not Ready', 'Placed']),
        fake.company(),
        round(random.uniform(3, 12), 2),
        random.randint(1, 5),
        fake.date_between(start_date='-1y', end_date='today').strftime('%Y-%m-%d')
    ))

#SAVE AND CLOSE THE DATABASE
conn.commit()
conn.close()
print("Fake data generated and inserted successfully!")

