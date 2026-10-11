"""Streamlit UI layer."""
import pandas as pd
import streamlit as st

import config
import database
import services


def students_to_dataframe(students: list[database.Student]) -> pd.DataFrame:
    return pd.DataFrame(
        {
            "Name": [student.name for student in students],
            "Score": [student.score for student in students],
            "Grade": [services.calculate_grade(student.score) for student in students],
        }
    )


def render_add_student_form() -> None:
    st.header("Add Student")
    with st.form("add_student_form", clear_on_submit=True):
        student_name = st.text_input("Student Name")
        student_score = st.number_input(
            "Score", min_value=config.MIN_SCORE, max_value=config.MAX_SCORE, step=1
        )
        is_submitted = st.form_submit_button("Add Student")

    if not is_submitted:
        return
    if not services.is_valid_name(student_name):
        st.error("Student name cannot be empty.")
        return
    if not services.is_valid_score(student_score):
        st.error(f"Score must be between {config.MIN_SCORE} and {config.MAX_SCORE}.")
        return

    database.add_student(student_name.strip(), int(student_score))
    st.success(f"{student_name.strip()} added.")


def render_statistics(students: list[database.Student]) -> None:
    st.header("Statistics")
    stats = services.calculate_statistics([student.score for student in students])
    columns = st.columns(4)
    columns[0].metric("Total Students", stats.total_students)
    columns[1].metric("Average Score", stats.average_score)
    columns[2].metric("Highest Score", stats.highest_score)
    columns[3].metric("Lowest Score", stats.lowest_score)


def render_student_list(students: list[database.Student]) -> None:
    st.header("Students")
    search_text = st.text_input("Search Student")
    visible_students = database.get_student(search_text) if search_text else students

    if visible_students:
        st.dataframe(students_to_dataframe(visible_students), use_container_width=True)
    else:
        st.info("No students found.")


def main() -> None:
    st.title("Student Performance Dashboard")
    render_add_student_form()
    students = database.get_students()
    render_statistics(students)
    render_student_list(students)


if __name__ == "__main__":
    main()
