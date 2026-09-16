import streamlit as st
import pandas as pd

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Dataset",
    page_icon="📋",
    layout="wide"
)

# --------------------------------------------------
# Load Dataset
# --------------------------------------------------

@st.cache_data
def load_data():
    df = pd.read_csv("data/Unemployment in India.csv")

    # Clean column names
    df.columns = df.columns.str.strip()

    # Clean text columns
    if "Region" in df.columns:
        df["Region"] = df["Region"].str.strip()

    if "Area" in df.columns:
        df["Area"] = df["Area"].str.strip()

    if "Frequency" in df.columns:
        df["Frequency"] = df["Frequency"].str.strip()

    # Convert Date
    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(
            df["Date"],
            dayfirst=True,
            errors="coerce"
        )

    return df


df = load_data()

# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("📋 Unemployment Dataset")

st.markdown(
    """
    ### Explore the Dataset

    This page allows you to explore, filter, and understand
    the unemployment dataset used in this project.
    """
)

st.markdown("---")

# --------------------------------------------------
# Dataset Overview
# --------------------------------------------------

st.subheader("📊 Dataset Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Records",
        f"{df.shape[0]:,}"
    )

with col2:
    st.metric(
        "Total Columns",
        df.shape[1]
    )

with col3:
    st.metric(
        "Missing Values",
        f"{df.isnull().sum().sum():,}"
    )

with col4:
    st.metric(
        "Regions",
        df["Region"].nunique()
    )

st.markdown("---")

# --------------------------------------------------
# Sidebar Filters
# --------------------------------------------------

st.sidebar.header("🔎 Dataset Filters")

# Region filter
regions = ["All Regions"] + sorted(
    df["Region"].dropna().unique().tolist()
)

selected_region = st.sidebar.selectbox(
    "Select Region",
    regions
)

# Area filter
if "Area" in df.columns:

    areas = ["All Areas"] + sorted(
        df["Area"].dropna().unique().tolist()
    )

    selected_area = st.sidebar.selectbox(
        "Select Area",
        areas
    )

else:
    selected_area = "All Areas"


# --------------------------------------------------
# Apply Filters
# --------------------------------------------------

filtered_df = df.copy()

if selected_region != "All Regions":
    filtered_df = filtered_df[
        filtered_df["Region"] == selected_region
    ]

if selected_area != "All Areas" and "Area" in filtered_df.columns:
    filtered_df = filtered_df[
        filtered_df["Area"] == selected_area
    ]

# --------------------------------------------------
# Filtered Dataset Information
# --------------------------------------------------

st.subheader("🔍 Filtered Dataset")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Records After Filtering",
        f"{len(filtered_df):,}"
    )

with col2:
    st.metric(
        "Regions Selected",
        filtered_df["Region"].nunique()
    )

with col3:
    st.metric(
        "Missing Values",
        f"{filtered_df.isnull().sum().sum():,}"
    )

# --------------------------------------------------
# Display Dataset
# --------------------------------------------------

st.dataframe(
    filtered_df,
    use_container_width=True,
    height=500
)

st.markdown("---")

# --------------------------------------------------
# Column Information
# --------------------------------------------------

st.subheader("🧾 Column Information")

column_info = pd.DataFrame({
    "Column Name": df.columns,
    "Data Type": [
        str(df[column].dtype)
        for column in df.columns
    ],
    "Non-Null Values": [
        df[column].notna().sum()
        for column in df.columns
    ],
    "Missing Values": [
        df[column].isnull().sum()
        for column in df.columns
    ]
})

st.dataframe(
    column_info,
    use_container_width=True
)

st.markdown("---")

# --------------------------------------------------
# Statistical Summary
# --------------------------------------------------

st.subheader("📈 Statistical Summary")

numeric_df = df.select_dtypes(
    include="number"
)

if not numeric_df.empty:
    st.dataframe(
        numeric_df.describe().round(2),
        use_container_width=True
    )

st.markdown("---")

# --------------------------------------------------
# Dataset Description
# --------------------------------------------------

st.subheader("📚 Dataset Description")

st.markdown(
    """
    **Important columns in the dataset:**

    - **Region** — Indian state or region represented in the data.
    - **Date** — Date of the recorded observation.
    - **Frequency** — Frequency of the observation.
    - **Estimated Unemployment Rate (%)** — Estimated percentage of unemployed people.
    - **Estimated Employed** — Estimated number of employed people.
    - **Estimated Labour Participation Rate (%)** — Percentage of the population participating in the labour market.
    - **Area** — Classification such as Urban or Rural.
    """
)

st.markdown("---")

# --------------------------------------------------
# Download Filtered Dataset
# --------------------------------------------------

st.subheader("⬇️ Download Dataset")

csv_data = filtered_df.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="📥 Download Filtered CSV",
    data=csv_data,
    file_name="filtered_unemployment_data.csv",
    mime="text/csv"
)

st.markdown("---")

st.caption(
    "CodeAlpha Internship | Task 2 — Unemployment Analysis"
)