import sqlite3
import os

class DatabaseManager:
    def __init__(self, db_path='data/students.db'):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()

    def get_all_students(self):
        query = "SELECT * FROM Students"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_eligible_students(self, where_clause):
        query = f"""
        SELECT s.student_id, s.name, s.age, s.email, p.language, p.problems_solved,
               ss.communication, pl.placement_status, pl.company_name
        FROM Students s
        JOIN Programming p ON s.student_id = p.student_id
        JOIN SoftSkills ss ON s.student_id = ss.student_id
        JOIN Placements pl ON s.student_id = pl.student_id
        WHERE {where_clause}
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def run_custom_query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()

