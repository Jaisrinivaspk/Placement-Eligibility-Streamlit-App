# queries.py

queries = {
    "1. Average Problems Solved": """
        SELECT AVG(problems_solved) AS avg_problems
        FROM Programming;
    """,

    "2. Top 5 Students by Mock Interview Score": """
        SELECT s.name, pl.mock_interview_score
        FROM Students s
        JOIN Placements pl ON s.student_id = pl.student_id
        ORDER BY pl.mock_interview_score DESC
        LIMIT 5;
    """,

    "3. Communication Skill Score Distribution": """
        SELECT communication, COUNT(*) AS num_students
        FROM SoftSkills
        GROUP BY communication
        ORDER BY communication DESC;
    """,

    "4. Students Ready for Placement": """
        SELECT COUNT(*) AS ready_count
        FROM Placements
        WHERE placement_status = 'Ready';
    """,

    "5. Average Soft Skills per City": """
        SELECT s.city,
               AVG(ss.communication) AS avg_comm,
               AVG(ss.teamwork) AS avg_teamwork,
               AVG(ss.presentation) AS avg_presentation
        FROM Students s
        JOIN SoftSkills ss ON s.student_id = ss.student_id
        GROUP BY s.city;
    """,

    "6. Company-wise Student Placements": """
        SELECT company_name, COUNT(*) AS total_placed
        FROM Placements
        WHERE placement_status = 'Placed'
        GROUP BY company_name
        ORDER BY total_placed DESC;
    """,

    "7. Students with More Than 1 Internship": """
        SELECT s.name, pl.internships_completed
        FROM Students s
        JOIN Placements pl ON s.student_id = pl.student_id
        WHERE pl.internships_completed > 1;
    """,

    "8. Certification Leaders": """
        SELECT s.name, p.certifications_earned
        FROM Students s
        JOIN Programming p ON s.student_id = p.student_id
        WHERE p.certifications_earned >= 2
        ORDER BY p.certifications_earned DESC;
    """,

    "9. Batch-Wise Programming Averages": """
        SELECT s.course_batch, AVG(p.problems_solved) AS avg_problems
        FROM Students s
        JOIN Programming p ON s.student_id = p.student_id
        GROUP BY s.course_batch;
    """,

    "10. Students Who Cleared More Than 3 Interview Rounds": """
        SELECT s.name, pl.interview_rounds_cleared
        FROM Students s
        JOIN Placements pl ON s.student_id = pl.student_id
        WHERE pl.interview_rounds_cleared > 3;
    """
}
