import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Unemployment Analysis",
    page_icon="📈",
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
# Page Title
# --------------------------------------------------

st.title("📈 Unemployment Analysis")

st.markdown(
    """
    ### Explore Unemployment Trends and Patterns

    This page provides a detailed analysis of unemployment rates,
    employment levels, labour participation, and regional differences
    in India.
    """
)

st.markdown("---")

# --------------------------------------------------
# Sidebar Filters
# --------------------------------------------------

st.sidebar.header("🔎 Analysis Filters")

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
# Key Analysis Metrics
# --------------------------------------------------

st.subheader("📊 Key Analysis Metrics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    avg_unemployment = filtered_df[
        "Estimated Unemployment Rate (%)"
    ].mean()

    st.metric(
        "Average Unemployment Rate",
        f"{avg_unemployment:.2f}%"
    )

with col2:
    max_unemployment = filtered_df[
        "Estimated Unemployment Rate (%)"
    ].max()

    st.metric(
        "Highest Unemployment Rate",
        f"{max_unemployment:.2f}%"
    )

with col3:
    min_unemployment = filtered_df[
        "Estimated Unemployment Rate (%)"
    ].min()

    st.metric(
        "Lowest Unemployment Rate",
        f"{min_unemployment:.2f}%"
    )

with col4:
    avg_labour = filtered_df[
        "Estimated Labour Participation Rate (%)"
    ].mean()

    st.metric(
        "Average Labour Participation",
        f"{avg_labour:.2f}%"
    )

st.markdown("---")

# --------------------------------------------------
# 1. Unemployment Trend
# --------------------------------------------------

st.subheader("📈 Unemployment Rate Trend")

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
    title="Unemployment Rate Over Time"
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

# --------------------------------------------------
# 2. Employment Trend
# --------------------------------------------------

st.subheader("👥 Employment Trend")

employment_df = (
    filtered_df
    .groupby("Date", as_index=False)[
        "Estimated Employed"
    ]
    .sum()
    .sort_values("Date")
)

fig2 = px.line(
    employment_df,
    x="Date",
    y="Estimated Employed",
    markers=True,
    title="Estimated Employment Over Time"
)

fig2.update_layout(
    xaxis_title="Date",
    yaxis_title="Estimated Employed",
    hovermode="x unified"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.markdown("---")

# --------------------------------------------------
# 3. Labour Participation Trend
# --------------------------------------------------

st.subheader("📊 Labour Participation Trend")

labour_df = (
    filtered_df
    .groupby("Date", as_index=False)[
        "Estimated Labour Participation Rate (%)"
    ]
    .mean()
    .sort_values("Date")
)

fig3 = px.line(
    labour_df,
    x="Date",
    y="Estimated Labour Participation Rate (%)",
    markers=True,
    title="Labour Participation Rate Over Time"
)

fig3.update_layout(
    xaxis_title="Date",
    yaxis_title="Labour Participation Rate (%)",
    hovermode="x unified"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

st.markdown("---")

# --------------------------------------------------
# 4. Regional Comparison
# --------------------------------------------------

st.subheader("🗺️ Regional Unemployment Comparison")

if selected_region == "All Regions":

    regional_df = (
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

    fig4 = px.bar(
        regional_df,
        x="Region",
        y="Estimated Unemployment Rate (%)",
        title="Average Unemployment Rate by Region",
        text_auto=".2f"
    )

    fig4.update_layout(
        xaxis_title="Region",
        yaxis_title="Average Unemployment Rate (%)",
        xaxis_tickangle=-45
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

else:

    st.info(
        f"📍 Currently analyzing **{selected_region}**."
    )

st.markdown("---")

# --------------------------------------------------
# 5. Area-wise Analysis
# --------------------------------------------------

if "Area" in filtered_df.columns:

    st.subheader("🏙️ Urban vs Rural Analysis")

    area_df = (
        filtered_df
        .groupby("Area", as_index=False)[
            "Estimated Unemployment Rate (%)"
        ]
        .mean()
        .sort_values(
            "Estimated Unemployment Rate (%)",
            ascending=False
        )
    )

    fig5 = px.bar(
        area_df,
        x="Area",
        y="Estimated Unemployment Rate (%)",
        title="Average Unemployment Rate by Area",
        text_auto=".2f"
    )

    fig5.update_layout(
        xaxis_title="Area",
        yaxis_title="Average Unemployment Rate (%)"
    )

    st.plotly_chart(
        fig5,
        use_container_width=True
    )

st.markdown("---")

# --------------------------------------------------
# 6. Unemployment vs Labour Participation
# --------------------------------------------------

st.subheader("🔍 Unemployment vs Labour Participation")

scatter_df = filtered_df.dropna(
    subset=[
        "Estimated Unemployment Rate (%)",
        "Estimated Labour Participation Rate (%)"
    ]
)

fig6 = px.scatter(
    scatter_df,
    x="Estimated Labour Participation Rate (%)",
    y="Estimated Unemployment Rate (%)",
    size="Estimated Employed",
    hover_name="Region",
    title="Unemployment Rate vs Labour Participation Rate"
)

fig6.update_layout(
    xaxis_title="Labour Participation Rate (%)",
    yaxis_title="Unemployment Rate (%)"
)

st.plotly_chart(
    fig6,
    use_container_width=True
)

st.markdown("---")

# --------------------------------------------------
# 7. Analysis Summary
# --------------------------------------------------

st.subheader("📋 Analysis Summary")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Records Analyzed",
        f"{len(filtered_df):,}"
    )

with col2:
    st.metric(
        "Regions",
        filtered_df["Region"].nunique()
    )

with col3:
    st.metric(
        "Average Employment",
        f"{filtered_df['Estimated Employed'].mean():,.0f}"
    )

st.markdown("---")

# --------------------------------------------------
# Data Preview
# --------------------------------------------------

st.subheader("📄 Filtered Data Preview")

st.dataframe(
    filtered_df.head(15),
    use_container_width=True
)

st.markdown("---")

st.caption(
    "CodeAlpha Internship | Task 2 — Unemployment Analysis"
)