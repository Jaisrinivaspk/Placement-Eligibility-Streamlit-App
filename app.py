import streamlit as st
from database import DatabaseManager
from queries import queries  


st.set_page_config(page_title="Placement Eligibility App", layout="wide")
st.title("🎓 Placement Eligibility Streamlit Application")
st.markdown("---")


# 🔍 Eligibility Section
st.header("🔍 Set Eligibility Criteria")

# Input fields
min_problems = st.number_input("Minimum Problems Solved", min_value=0, max_value=200, value=50)
min_communication = st.number_input("Minimum Communication Score", min_value=0, max_value=100, value=70)
placement_status = st.selectbox("Placement Status", ["Ready", "Not Ready", "Placed"])

if st.button("📊 Show Eligible Students"):
    db = DatabaseManager()

    where = f"""
        p.problems_solved >= {min_problems}
        AND ss.communication >= {min_communication}
        AND pl.placement_status = '{placement_status}'
    """

    results = db.get_eligible_students(where)

    if results:
        st.success(f"Found {len(results)} eligible students!")
        st.dataframe(results)
    else:
        st.warning("No students found matching the criteria.")

    db.close()

# 📊 SQL Insights Section
st.markdown("---")
st.header("📊 Explore SQL Insights")

selected_query = st.selectbox("Choose a query to view insights:", list(queries.keys()))

if st.button("Run Query"):
    db = DatabaseManager()
    result = db.run_custom_query(queries[selected_query])

    if result:
        st.write("### Query Result")
        st.dataframe(result)
    else:
        st.warning("No data found for this query.")
    db.close()
