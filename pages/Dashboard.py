import streamlit as st
import pandas as pd
import plotly.express as px

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Unemployment Dashboard",
    page_icon="📊",
    layout="wide"
)


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():
    df = pd.read_csv("data/Unemployment in India.csv")

    # Remove extra spaces from column names
    df.columns = df.columns.str.strip()

    # Clean Region column
    if "Region" in df.columns:
        df["Region"] = df["Region"].str.strip()

    # Convert Date column
    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(
            df["Date"],
            dayfirst=True,
            errors="coerce"
        )

    return df


df = load_data()


# ============================================================
# PAGE TITLE
# ============================================================

st.title("📊 Unemployment Dashboard")

st.markdown(
    """
    ### Overview of Unemployment in India

    Explore unemployment rates, employment levels, labour participation,
    regional differences, and trends over time.
    """
)

st.markdown("---")


# ============================================================
# SIDEBAR FILTER
# ============================================================

st.sidebar.header("🔎 Dashboard Filters")

regions = ["All Regions"] + sorted(
    df["Region"].dropna().unique().tolist()
)

selected_region = st.sidebar.selectbox(
    "Select Region",
    regions
)


# Filter dataset
if selected_region == "All Regions":
    filtered_df = df.copy()
else:
    filtered_df = df[
        df["Region"] == selected_region
    ].copy()


# ============================================================
# KPI SECTION
# ============================================================

st.subheader("📌 Key Statistics")

col1, col2, col3, col4 = st.columns(4)


# Average unemployment
with col1:

    avg_unemployment = filtered_df[
        "Estimated Unemployment Rate (%)"
    ].mean()

    st.metric(
        label="📈 Average Unemployment",
        value=f"{avg_unemployment:.2f}%"
    )


# Total employed
with col2:

    total_employed = filtered_df[
        "Estimated Employed"
    ].sum()

    st.metric(
        label="👥 Total Estimated Employed",
        value=f"{total_employed:,.0f}"
    )


# Labour participation
with col3:

    avg_labour = filtered_df[
        "Estimated Labour Participation Rate (%)"
    ].mean()

    st.metric(
        label="📊 Avg Labour Participation",
        value=f"{avg_labour:.2f}%"
    )


# Regions
with col4:

    region_count = filtered_df[
        "Region"
    ].nunique()

    st.metric(
        label="🗺️ Regions Covered",
        value=region_count
    )


st.markdown("---")


# ============================================================
# UNEMPLOYMENT TREND
# ============================================================

st.subheader("📈 Unemployment Rate Trend")

if "Date" in filtered_df.columns:

    trend_df = (
        filtered_df
        .groupby("Date", as_index=False)[
            "Estimated Unemployment Rate (%)"
        ]
        .mean()
        .sort_values("Date")
    )

    fig1 = px.line(
        trend_df,
        x="Date",
        y="Estimated Unemployment Rate (%)",
        markers=True,
        title="Average Unemployment Rate Over Time"
    )

    fig1.update_layout(
        xaxis_title="Date",
        yaxis_title="Unemployment Rate (%)",
        hovermode="x unified"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )


st.markdown("---")


# ============================================================
# REGIONAL ANALYSIS
# ============================================================

st.subheader("🗺️ Regional Unemployment Analysis")

if selected_region == "All Regions":

    region_df = (
        filtered_df
        .groupby("Region", as_index=False)[
            "Estimated Unemployment Rate (%)"
        ]
        .mean()
        .sort_values(
            "Estimated Unemployment Rate (%)",
            ascending=False
        )
    )

    fig2 = px.bar(
        region_df,
        x="Region",
        y="Estimated Unemployment Rate (%)",
        title="Average Unemployment Rate by Region",
        text_auto=".2f"
    )

    fig2.update_layout(
        xaxis_title="Region",
        yaxis_title="Average Unemployment Rate (%)",
        xaxis_tickangle=-45
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

else:

    st.info(
        f"Showing data for **{selected_region}**."
    )


st.markdown("---")


# ============================================================
# EMPLOYMENT VS LABOUR PARTICIPATION
# ============================================================

st.subheader("👥 Employment vs Labour Participation")

scatter_df = filtered_df.dropna(
    subset=[
        "Estimated Employed",
        "Estimated Labour Participation Rate (%)"
    ]
)

fig3 = px.scatter(
    scatter_df,
    x="Estimated Labour Participation Rate (%)",
    y="Estimated Employed",
    size="Estimated Employed",
    hover_name="Region",
    title="Employment vs Labour Participation Rate"
)

fig3.update_layout(
    xaxis_title="Labour Participation Rate (%)",
    yaxis_title="Estimated Employed"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)


st.markdown("---")


# ============================================================
# DATASET SUMMARY
# ============================================================

st.subheader("📋 Dataset Summary")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Records",
        f"{len(filtered_df):,}"
    )

with col2:
    st.metric(
        "Total Columns",
        len(filtered_df.columns)
    )

with col3:
    missing_values = filtered_df.isnull().sum().sum()

    st.metric(
        "Missing Values",
        f"{missing_values:,}"
    )


# ============================================================
# RECENT DATA
# ============================================================

st.markdown("---")

st.subheader("🔍 Data Preview")

st.dataframe(
    filtered_df.head(10),
    use_container_width=True
)


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "CodeAlpha Internship | Task 2 — Unemployment Analysis"
)
