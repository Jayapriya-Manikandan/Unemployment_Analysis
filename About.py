import streamlit as st

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("ℹ️ About This Project")

st.markdown(
    """
    ### 📊 Unemployment Analysis in India

    This project analyzes unemployment data in India to understand
    unemployment trends, regional differences, employment levels,
    labour participation, and changes during the COVID-19 period.
    """
)

st.markdown("---")

# --------------------------------------------------
# Project Objective
# --------------------------------------------------

st.subheader("🎯 Project Objective")

st.write(
    """
    The main objective of this project is to explore unemployment
    data using Python and data visualization techniques.

    The analysis focuses on identifying meaningful patterns and
    trends to provide a better understanding of unemployment
    conditions across different regions and periods.
    """
)

st.markdown("---")

# --------------------------------------------------
# What This Project Covers
# --------------------------------------------------

st.subheader("🔍 What This Project Covers")

col1, col2 = st.columns(2)

with col1:

    st.info(
        """
        **📈 Unemployment Trends**

        Analyze how unemployment rates change over time.
        """
    )

    st.info(
        """
        **🗺️ Regional Analysis**

        Compare unemployment levels across different regions.
        """
    )

    st.info(
        """
        **👥 Employment Analysis**

        Explore estimated employment levels in the dataset.
        """
    )

with col2:

    st.info(
        """
        **📊 Labour Participation**

        Study labour participation rates and their trends.
        """
    )

    st.info(
        """
        **🦠 COVID-19 Impact**

        Compare unemployment conditions before and during
        the COVID-19 period.
        """
    )

    st.info(
        """
        **💡 Data Insights**

        Identify important observations from the analysis.
        """
    )

st.markdown("---")

# --------------------------------------------------
# Technologies Used
# --------------------------------------------------

st.subheader("🛠️ Technologies Used")

tech1, tech2, tech3, tech4 = st.columns(4)

with tech1:
    st.metric(
        "🐍 Language",
        "Python"
    )

with tech2:
    st.metric(
        "🐼 Data Analysis",
        "Pandas"
    )

with tech3:
    st.metric(
        "📊 Visualization",
        "Plotly"
    )

with tech4:
    st.metric(
        "🌐 Web App",
        "Streamlit"
    )

st.markdown("---")

# --------------------------------------------------
# Python Libraries
# --------------------------------------------------

st.subheader("📚 Python Libraries")

st.markdown(
    """
    - **Pandas** — Data loading, cleaning, filtering, and analysis
    - **NumPy** — Numerical operations
    - **Plotly** — Interactive data visualizations
    - **Matplotlib** — Data visualization support
    - **Seaborn** — Statistical visualization support
    - **Streamlit** — Interactive web application development
    """
)

st.markdown("---")

# --------------------------------------------------
# Project Structure
# --------------------------------------------------

st.subheader("📁 Project Structure")

st.code(
    """
Unemployment_Analysis/
│
├── data/
│   └── Unemployment in India.csv
│
├── pages/
│   ├── About.py
│   ├── Analysis.py
│   ├── COVID-19_Impact.py
│   ├── Dashboard.py
│   ├── Dataset.py
│   └── Insights.py
│
├── app.py
├── README.md
└── requirements.txt
    """,
    language="text"
)

st.markdown("---")

# --------------------------------------------------
# Dataset
# --------------------------------------------------

st.subheader("📋 Dataset")

st.write(
    """
    The project uses the **Unemployment in India** dataset.

    The dataset contains information about:

    - Region
    - Date
    - Frequency
    - Estimated Unemployment Rate (%)
    - Estimated Employed
    - Estimated Labour Participation Rate (%)
    - Area
    """
)

st.markdown("---")

# --------------------------------------------------
# Learning Outcomes
# --------------------------------------------------

st.subheader("🎓 Learning Outcomes")

st.markdown(
    """
    Through this project, the following skills are demonstrated:

    - Data loading and preprocessing using Python
    - Exploratory Data Analysis (EDA)
    - Statistical analysis
    - Interactive data visualization
    - Regional and time-based analysis
    - COVID-19 period comparison
    - Building a multi-page Streamlit application
    """
)

st.markdown("---")

# --------------------------------------------------
# Project Highlights
# --------------------------------------------------

st.subheader("✨ Project Highlights")

st.markdown(
    """
    - Interactive dashboard with data filters
    - Time-based unemployment analysis
    - Regional unemployment comparison
    - Urban and rural analysis
    - COVID-19 impact comparison
    - Interactive Plotly visualizations
    - Dataset exploration and CSV download
    - Key insights generated from the data
    """
)