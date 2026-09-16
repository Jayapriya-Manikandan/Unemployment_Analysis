import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Insights",
    page_icon="💡",
    layout="wide"
)

# --------------------------------------------------
# Load Dataset
# --------------------------------------------------

@st.cache_data
def load_data():
    df = pd.read_csv("data/Unemployment in India.csv")

    df.columns = df.columns.str.strip()

    if "Region" in df.columns:
        df["Region"] = df["Region"].str.strip()

    if "Area" in df.columns:
        df["Area"] = df["Area"].str.strip()

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

st.title("💡 Key Insights")

st.markdown(
    """
    ### Important Findings from the Unemployment Analysis

    This page highlights the major patterns and observations
    identified from the unemployment dataset.
    """
)

st.markdown("---")

# --------------------------------------------------
# Overall Statistics
# --------------------------------------------------

avg_unemployment = df[
    "Estimated Unemployment Rate (%)"
].mean()

highest_unemployment = df[
    "Estimated Unemployment Rate (%)"
].max()

lowest_unemployment = df[
    "Estimated Unemployment Rate (%)"
].min()

avg_labour = df[
    "Estimated Labour Participation Rate (%)"
].mean()

# Find records for highest unemployment
highest_row = df.loc[
    df["Estimated Unemployment Rate (%)"].idxmax()
]

# --------------------------------------------------
# Key Metrics
# --------------------------------------------------

st.subheader("📊 Overall Statistics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Average Unemployment",
        f"{avg_unemployment:.2f}%"
    )

with col2:
    st.metric(
        "Highest Unemployment",
        f"{highest_unemployment:.2f}%"
    )

with col3:
    st.metric(
        "Lowest Unemployment",
        f"{lowest_unemployment:.2f}%"
    )

with col4:
    st.metric(
        "Avg Labour Participation",
        f"{avg_labour:.2f}%"
    )

st.markdown("---")

# --------------------------------------------------
# Insight 1 - Highest Unemployment
# --------------------------------------------------

st.subheader("🔴 1. Highest Unemployment Observation")

st.write(
    f"""
    The highest recorded unemployment rate in the dataset is
    **{highest_unemployment:.2f}%**.
    """
)

if "Region" in highest_row.index:
    st.write(
        f"📍 Region: **{highest_row['Region']}**"
    )

if "Date" in highest_row.index:
    st.write(
        f"📅 Date: **{highest_row['Date'].strftime('%d-%m-%Y')}**"
        if pd.notna(highest_row["Date"])
        else "📅 Date: Not available"
    )

st.markdown("---")

# --------------------------------------------------
# Insight 2 - Regional Analysis
# --------------------------------------------------

st.subheader("🗺️ 2. Regional Unemployment Insights")

regional_df = (
    df.groupby("Region", as_index=False)[
        "Estimated Unemployment Rate (%)"
    ]
    .mean()
    .sort_values(
        "Estimated Unemployment Rate (%)",
        ascending=False
    )
)

fig1 = px.bar(
    regional_df,
    x="Region",
    y="Estimated Unemployment Rate (%)",
    title="Average Unemployment Rate by Region",
    text_auto=".2f"
)

fig1.update_layout(
    xaxis_title="Region",
    yaxis_title="Average Unemployment Rate (%)",
    xaxis_tickangle=-45
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

st.info(
    """
    Regional unemployment rates vary across the dataset.
    The chart helps identify regions with relatively higher
    and lower average unemployment levels.
    """
)

st.markdown("---")

# --------------------------------------------------
# Insight 3 - Trend Over Time
# --------------------------------------------------

st.subheader("📈 3. Unemployment Trend Over Time")

trend_df = (
    df.groupby("Date", as_index=False)[
        "Estimated Unemployment Rate (%)"
    ]
    .mean()
    .sort_values("Date")
)

fig2 = px.line(
    trend_df,
    x="Date",
    y="Estimated Unemployment Rate (%)",
    markers=True,
    title="Average Unemployment Rate Over Time"
)

fig2.update_layout(
    xaxis_title="Date",
    yaxis_title="Average Unemployment Rate (%)",
    hovermode="x unified"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.markdown(
    """
    **Observation:** The time-series chart shows how unemployment
    changed across the available observation period and helps
    identify noticeable increases or decreases.
    """
)

st.markdown("---")

# --------------------------------------------------
# Insight 4 - Urban vs Rural
# --------------------------------------------------

if "Area" in df.columns:

    st.subheader("🏙️ 4. Urban vs Rural Insights")

    area_df = (
        df.groupby("Area", as_index=False)[
            "Estimated Unemployment Rate (%)"
        ]
        .mean()
        .sort_values(
            "Estimated Unemployment Rate (%)",
            ascending=False
        )
    )

    fig3 = px.bar(
        area_df,
        x="Area",
        y="Estimated Unemployment Rate (%)",
        text_auto=".2f",
        title="Average Unemployment Rate by Area"
    )

    fig3.update_layout(
        xaxis_title="Area",
        yaxis_title="Average Unemployment Rate (%)"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

    st.info(
        """
        The comparison provides an overview of differences
        between the available area categories in the dataset.
        """
    )

st.markdown("---")

# --------------------------------------------------
# Insight 5 - COVID-19
# --------------------------------------------------

st.subheader("🦠 5. COVID-19 Period Insight")

covid_start = pd.Timestamp("2020-03-01")

pre_covid = df[
    df["Date"] < covid_start
]

covid_period = df[
    df["Date"] >= covid_start
]

pre_covid_avg = pre_covid[
    "Estimated Unemployment Rate (%)"
].mean()

covid_avg = covid_period[
    "Estimated Unemployment Rate (%)"
].mean()

covid_change = covid_avg - pre_covid_avg

comparison_df = pd.DataFrame({
    "Period": [
        "Pre-COVID",
        "COVID-19"
    ],
    "Average Unemployment Rate": [
        pre_covid_avg,
        covid_avg
    ]
})

fig4 = px.bar(
    comparison_df,
    x="Period",
    y="Average Unemployment Rate",
    text_auto=".2f",
    title="Pre-COVID vs COVID-19 Unemployment"
)

fig4.update_layout(
    xaxis_title="Period",
    yaxis_title="Average Unemployment Rate (%)"
)

st.plotly_chart(
    fig4,
    use_container_width=True
)

if covid_change > 0:
    st.warning(
        f"""
        The average unemployment rate was **{covid_change:.2f}
        percentage points higher** during the COVID-19 period
        compared with the pre-COVID period.
        """
    )
elif covid_change < 0:
    st.info(
        f"""
        The average unemployment rate was **{abs(covid_change):.2f}
        percentage points lower** during the COVID-19 period
        compared with the pre-COVID period.
        """
    )
else:
    st.info(
        "The average unemployment rate was approximately unchanged."
    )

st.markdown("---")

# --------------------------------------------------
# Insight 6 - Employment
# --------------------------------------------------

st.subheader("👥 6. Employment Insight")

average_employed = df[
    "Estimated Employed"
].mean()

st.metric(
    "Average Estimated Employment",
    f"{average_employed:,.0f}"
)

st.write(
    """
    The estimated employment values provide an additional view
    of labour-market conditions alongside the unemployment rate.
    """
)

st.markdown("---")

# --------------------------------------------------
# Main Takeaways
# --------------------------------------------------

st.subheader("🎯 Main Takeaways")

st.markdown(
    f"""
    ### Key Findings

    **1. Unemployment varies across regions**  
    Different regions show different average unemployment levels.

    **2. Unemployment changes over time**  
    The time-series analysis reveals changes in unemployment
    throughout the available dataset period.

    **3. Labour participation provides additional context**  
    Labour participation helps understand how actively people
    are participating in the labour market.

    **4. COVID-19 is an important period for comparison**  
    Comparing the periods before and from March 2020 helps
    examine changes around the beginning of the pandemic period.

    **5. Employment and unemployment should be studied together**  
    Looking at estimated employment along with unemployment
    provides a broader understanding of labour-market conditions.
    """
)

st.markdown("---")

# --------------------------------------------------
# Methodology Note
# --------------------------------------------------

st.subheader("📝 Methodology Note")

st.caption(
    """
    Insights are generated from the available dataset using
    descriptive statistics and visual analysis. The COVID-19
    comparison uses March 2020 as the analytical starting point.
    """
)

st.markdown("---")

st.caption(
    "CodeAlpha Internship | Task 2 — Unemployment Analysis"
)