import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(
    page_title="Employee Salary Prediction",
    page_icon="💼",
    layout="wide"
)

# -----------------------------
# Load Model
# -----------------------------
model = joblib.load("model1.pkl")

# -----------------------------
# Title
# -----------------------------
st.markdown(
    """
    <h1 style='text-align:center;color:#2E8B57;'>
    💼 Employee Salary Prediction & Analytics
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    "<h4 style='text-align:center;'>Predict Employee Salary using Machine Learning</h4>",
    unsafe_allow_html=True
)

st.divider()

# -----------------------------
# Sidebar
# -----------------------------
page = st.sidebar.selectbox(
    "Navigation",
    [
        "Salary Prediction",
        "About Project"
    ]
)

# ===================================================
# SALARY PREDICTION PAGE
# ===================================================

if page == "Salary Prediction":

    st.subheader("Employee Information")

    col1, col2 = st.columns(2)

    with col1:

        age = st.slider(
            "Age",
            18,
            65,
            25
        )

        gender = st.selectbox(
            "Gender",
            [
                "Male",
                "Female"
            ]
        )

        education = st.selectbox(
            "Education Level",
            [
                0,
                1,
                2,
                3
            ],
            format_func=lambda x: {
                0: "High School",
                1: "Bachelor",
                2: "Master",
                3: "PhD"
            }[x]
        )
    with col2:

        job_title = st.selectbox(
            "Job Title",
            [
                "Software Engineer",
                "Data Analyst",
                "Manager",
                "Sales Associate",
                "Director",
                "Marketing Analyst",
                "Product Manager",
                "HR Manager",
                "Financial Analyst",
                "Project Manager",
                "Business Analyst",
                "Data Scientist",
                "Accountant",
                "Marketing Specialist",
                "Network Engineer",
                "Web Developer",
                "IT Manager",
                "UX Designer",
                "Graphic Designer",
                "Research Scientist"
            ]
        )

        experience = st.slider(
            "Years of Experience",
            0,
            40,
            3
        )

        country = st.selectbox(
            "Country",
            [
                "India",
                "USA",
                "UK",
                "Canada",
                "Australia",
                "China"
            ]
        )

    st.divider()

    if st.button("Predict Salary", use_container_width=True):

        sample = pd.DataFrame({

            "Age":[age],

            "Gender":[gender],

            "Education Level":[education],

            "Job Title":[job_title],

            "Years of Experience":[experience],

            "Country":[country]

        })

        prediction = model.predict(sample)[0]

        st.success(
            f"🎉 Predicted Annual Salary : ₹ {prediction:,.0f}"
        )
        monthly_salary = prediction / 12

        if prediction < 500000:
            category = "🟢 Entry Level"

        elif prediction < 1200000:
            category = "🟡 Mid Level"

        elif prediction < 2500000:
            category = "🟠 Senior Level"

        else:
            category = "🔴 Executive Level"

        st.divider()

        col1,col2,col3 = st.columns(3)

        with col1:

            st.metric(
                "Annual Salary",
                f"₹ {prediction:,.0f}"
            )

        with col2:

            st.metric(
                "Monthly Salary",
                f"₹ {monthly_salary:,.0f}"
            )

        with col3:

            st.metric(
                "Salary Category",
                category
            )

        st.success("Prediction Completed Successfully")

        st.balloons()

# ==================================================
# ANALYTICS PAGE
# ==================================================

elif page=="Analytics":

    st.header("Salary Analytics Dashboard")

    st.subheader("Dataset Overview")

    st.write(df.head())

    st.divider()

    fig1=px.histogram(
        df,
        x="Salary",
        nbins=30,
        title="Salary Distribution"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    fig2=px.scatter(
        df,
        x="Years of Experience",
        y="Salary",
        color="Gender",
        title="Experience vs Salary"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    fig3=px.box(
        df,
        x="Education Level",
        y="Salary",
        color="Education Level",
        title="Education Level vs Salary"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )
# ==================================================
# DATASET PAGE
# ==================================================

elif page == "Dataset":

    st.header("Employee Salary Dataset")

    st.dataframe(df, use_container_width=True)

    st.divider()

    st.write("Dataset Shape :", df.shape)

    st.write("Columns")

    st.write(df.columns.tolist())

# ==================================================
# ABOUT PAGE
# ==================================================

elif page == "About Project":

    st.header("About Project")

    st.markdown("""
### 💼 Employee Salary Prediction & Analytics System

This project predicts the annual salary of an employee using a trained
Machine Learning model.

### Machine Learning Algorithm

✅ Random Forest Regressor

### Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Plotly
- Joblib

### Input Parameters

- Age
- Gender
- Education Level
- Job Title
- Country
- Years of Experience

### Output

- Predicted Annual Salary
- Monthly Salary
- Salary Category

---
""")

    st.info("Model Accuracy (R² Score): 97.1 %")

    st.success("Project Ready for Demonstration")

# ==================================================
# FOOTER
# ==================================================

st.divider()

st.markdown(
"""
<div style='text-align:center;'>

### 💻 Developed by

<b>Divyansh Agrawal</b>

Employee Salary Prediction & Analytics System

SSIPMT Raipur

Machine Learning Project

2026

</div>
""",
unsafe_allow_html=True
)
