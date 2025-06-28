# 🎓 Placement Eligibility Streamlit App

This is a simple web application created using **Streamlit** that allows placement teams to filter students based on eligibility criteria and view insights using SQL. It simulates student data for a Data Science course using the Faker library.

---

## 📌 Features

- Generate fake student data using the **Faker** library
- Store and manage data in a **SQLite** database
- Use **OOP (Object-Oriented Programming)** in Python for clean structure
- Build a real-time, interactive web app using **Streamlit**
- Display SQL insights with **10 custom queries**

---

## 🧰 Tools and Technologies Used

- Python 3.12
- Streamlit
- SQLite
- Faker
- SQL
- SQLAlchemy (optional)

---

## 📁 Project Folder Structure

```Placement_Eligibility_App/
│
├── data/
│ └── students.db # SQLite database
│
├── app.py # Streamlit web app code
├── data_generator.py # Generates fake data and creates tables
├── database.py # OOP class for database interaction
├── queries.py # Contains 10 SQL insight queries
├── README.md # Project description (this file)
```

---

## 🚀 How to Run This Project

### 1. Install Required Libraries

Open your terminal or command prompt and run:
```pip install streamlit faker sqlalchemy
```

---

### 2. Generate Fake Student Data

This will create the `students.db` database with 4 tables and fake records:
 ```python data_generator.py
 ```
---

### 3. Run the Streamlit App

This command will launch the web app in your default browser:
 ```python -m streamlit run app.py
 ```


---

## 📊 SQL Insights Included

The application includes the following SQL insights:

1. Average Problems Solved by All Students
2. Top 5 Students by Mock Interview Score
3. Communication Skill Score Distribution
4. Count of Students Ready for Placement
5. City-wise Average Soft Skills Scores
6. Company-wise Placement Count
7. Students with More Than 1 Internship
8. Students with Multiple Programming Certifications
9. Batch-wise Programming Problem Averages
10. Students Who Cleared More Than 3 Interview Rounds



## 🙋‍♂️ Developer

**Jaisrinivas P K**  
Project Submitted to: **GUVI - EdTech Capstone Submission**  
Domain: **Data Science**
---
