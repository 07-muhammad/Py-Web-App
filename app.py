import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Project Recommendation Dashboard",
    page_icon="💻",
    layout="centered"
)

# Title
st.title("Project Recommendation Dashboard")
st.write("Tell us about yourself and we'll suggest some programming projects!")

# -----------------------------
# User Information
# -----------------------------
st.header("Personal Information")

name = st.text_input("Enter your name")

age = st.number_input(
    "Enter your age",
    min_value=10,
    max_value=100,
    value=18
)

qualifications = st.text_input(
    "Enter your qualifications",
    placeholder="e.g. Bachelor's in Computer Science"
)

# -----------------------------
# Programming Expertise
# -----------------------------
st.header("Programming Expertise")

expertise = st.selectbox(
    "How would you rate your programming expertise?",
    [
        "Beginner",
        "Intermediate",
        "Advanced"
    ]
)

language = st.multiselect(
    "Which programming languages do you know?",
    [
        "Python",
        "JavaScript",
        "Java",
        "C++",
        "C",
        "PHP",
        "Go",
        "Rust"
    ]
)

# -----------------------------
# Project Suggestions
# -----------------------------
if st.button("Suggest Projects"):

    # Basic validation
    if not name or not qualifications:
        st.warning("Please enter your name and qualifications.")
    else:

        st.success(f"Welcome, {name}! Here are some projects for you.")

        st.write(f"**Age:** {age}")
        st.write(f"**Qualifications:** {qualifications}")
        st.write(f"**Expertise:** {expertise}")

        if language:
            st.write("**Programming Languages:** " + ", ".join(language))

        st.header("Recommended Projects")

        # Beginner projects
        if expertise == "Beginner":

            projects = [
                "To-Do List App",
                "Calculator",
                "Number Guessing Game",
                "Weather App",
                "Personal Expense Tracker"
            ]

        # Intermediate projects
        elif expertise == "Intermediate":

            projects = [
                "Data Analysis Dashboard",
                "Machine Learning Prediction App",
                "News Aggregator",
                "User Authentication System",
                "Online Learning Management System"
            ]

        # Advanced projects
        else:

            projects = [
                "AI Chatbot",
                "Recommendation System",
                "Computer Vision Application",
                "Cloud-Based Web Application",
                "Real-Time Data Analytics Dashboard"
            ]

        for project in projects:
            st.write(f"- {project}")

        st.info(
            "Choose a project that matches your current skill level "
            "and gradually increase its complexity."
        )
