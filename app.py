import streamlit as st

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Unemployment Analysis",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# Main Header
# --------------------------------------------------

st.title("📊 Unemployment Analysis in India")

st.subheader(
    "Understanding Unemployment Trends, Regional Patterns and COVID-19 Impact"
)

st.markdown(
    """
    This interactive application explores unemployment data in India
    using data analysis and visualization techniques.

    Explore trends, compare regions, understand labour participation,
    and examine changes during the COVID-19 period.
    """
)

st.markdown("---")

# --------------------------------------------------
# Project Objective
# --------------------------------------------------

st.header("🎯 Project Objective")

st.write(
    """
    The objective of this project is to analyze unemployment data,
    identify important patterns and trends, and present the findings
    through an interactive data visualization application.
    """
)

st.markdown("---")

# --------------------------------------------------
# Explore the Project
# --------------------------------------------------

st.header("🚀 Explore the Project")

col1, col2, col3 = st.columns(3)

with col1:
    st.info(
        """
        ### 📊 Dashboard

        View key unemployment statistics, trends,
        regional comparisons, and interactive charts.
        """
    )

with col2:
    st.info(
        """
        ### 📈 Analysis

        Explore unemployment, employment, labour
        participation, and regional patterns in detail.
        """
    )

with col3:
    st.info(
        """
        ### 🦠 COVID-19 Impact

        Compare unemployment conditions before and
        during the COVID-19 period.
        """
    )

col4, col5, col6 = st.columns(3)

with col4:
    st.info(
        """
        ### 📋 Dataset

        Explore, filter, analyze, and download
        the unemployment dataset.
        """
    )

with col5:
    st.info(
        """
        ### 💡 Insights

        Discover important findings and observations
        from the unemployment analysis.
        """
    )

with col6:
    st.info(
        """
        ### ℹ️ About

        Learn about the project, technologies,
        dataset, and learning outcomes.
        """
    )

st.markdown("---")

# --------------------------------------------------
# Key Features
# --------------------------------------------------

st.header("✨ Key Features")

feature_col1, feature_col2 = st.columns(2)

with feature_col1:
    st.markdown(
        """
        - 📈 Unemployment trend analysis
        - 🗺️ Regional comparison
        - 👥 Employment analysis
        - 📊 Labour participation analysis
        """
    )

with feature_col2:
    st.markdown(
        """
        - 🏙️ Urban vs Rural comparison
        - 🦠 COVID-19 period analysis
        - 🔎 Interactive data filtering
        - 📊 Interactive Plotly visualizations
        """
    )

st.markdown("---")

# --------------------------------------------------
# Technologies Used
# --------------------------------------------------

st.header("🛠️ Technologies Used")

# Empty columns on both sides keep the technologies centered
tech_space1, tech1, tech2, tech3, tech4, tech_space2 = st.columns(
    [1.5, 1, 1, 1, 1, 1.5]
)

with tech1:
    st.markdown("### 🐍")
    st.markdown("**Python**")

with tech2:
    st.markdown("### 🐼")
    st.markdown("**Pandas**")

with tech3:
    st.markdown("### 📊")
    st.markdown("**Plotly**")

with tech4:
    st.markdown("### 🌐")
    st.markdown("**Streamlit**")

st.markdown("---")

# --------------------------------------------------
# Getting Started
# --------------------------------------------------

st.header("📌 Getting Started")

st.write(
    """
    Use the navigation menu on the left to explore the different
    sections of the application.
    """
)

st.markdown(
    """
    **Recommended flow:**

    `Dashboard` → `Analysis` → `COVID-19 Impact` → `Dataset` → `Insights`
    """
)

st.markdown("---")

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.caption(
    "Unemployment Analysis in India | Data Analysis & Visualization Project"
)