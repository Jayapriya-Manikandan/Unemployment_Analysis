import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="COVID-19 Impact",
    page_icon="🦠",
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

st.title("🦠 COVID-19 Impact on Unemployment")

st.markdown(
    """
    ### Understanding the Impact of COVID-19 on Employment

    This page compares unemployment conditions before and during
    the COVID-19 period to identify changes in unemployment,
    employment, and labour participation.
    """
)

st.markdown("---")

# --------------------------------------------------
# Define COVID Period
# --------------------------------------------------

# March 2020 is used as the beginning of the COVID-19 period
covid_start = pd.Timestamp("2020-03-01")

df["Period"] = df["Date"].apply(
    lambda x: "COVID-19 Period"
    if pd.notna(x) and x >= covid_start
    else "Pre-COVID Period"
)

# --------------------------------------------------
# Sidebar Filter
# --------------------------------------------------

st.sidebar.header("🔎 COVID-19 Analysis")

regions = ["All Regions"] + sorted(
    df["Region"].dropna().unique().tolist()
)

selected_region = st.sidebar.selectbox(
    "Select Region",
    regions
)

if selected_region == "All Regions":
    filtered_df = df.copy()
else:
    filtered_df = df[
        df["Region"] == selected_region
    ].copy()

# --------------------------------------------------
# Period Data
# --------------------------------------------------

pre_covid = filtered_df[
    filtered_df["Period"] == "Pre-COVID Period"
]

covid_period = filtered_df[
    filtered_df["Period"] == "COVID-19 Period"
]

# --------------------------------------------------
# Key Statistics
# --------------------------------------------------

st.subheader("📊 COVID-19 Impact Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    pre_avg = pre_covid[
        "Estimated Unemployment Rate (%)"
    ].mean()

    st.metric(
        "Pre-COVID Unemployment",
        f"{pre_avg:.2f}%"
    )

with col2:
    covid_avg = covid_period[
        "Estimated Unemployment Rate (%)"
    ].mean()

    st.metric(
        "COVID-19 Unemployment",
        f"{covid_avg:.2f}%"
    )

with col3:
    change = covid_avg - pre_avg

    st.metric(
        "Unemployment Change",
        f"{change:+.2f}%"
    )

with col4:
    employment_change = (
        covid_period["Estimated Employed"].mean()
        - pre_covid["Estimated Employed"].mean()
    )

    st.metric(
        "Employment Change",
        f"{employment_change:+,.0f}"
    )

st.markdown("---")

# --------------------------------------------------
# Unemployment Trend During COVID
# --------------------------------------------------

st.subheader("📈 Unemployment Rate Before and During COVID-19")

trend_df = (
    filtered_df
    .groupby(["Date", "Period"], as_index=False)[
        "Estimated Unemployment Rate (%)"
    ]
    .mean()
    .sort_values("Date")
)

fig1 = px.line(
    trend_df,
    x="Date",
    y="Estimated Unemployment Rate (%)",
    color="Period",
    markers=True,
    title="Unemployment Rate Trend"
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
# Pre-COVID vs COVID Comparison
# --------------------------------------------------

st.subheader("⚖️ Pre-COVID vs COVID-19 Comparison")

comparison_df = pd.DataFrame({
    "Period": [
        "Pre-COVID Period",
        "COVID-19 Period"
    ],
    "Average Unemployment Rate": [
        pre_avg,
        covid_avg
    ]
})

fig2 = px.bar(
    comparison_df,
    x="Period",
    y="Average Unemployment Rate",
    text_auto=".2f",
    title="Average Unemployment Rate Comparison"
)

fig2.update_layout(
    xaxis_title="Period",
    yaxis_title="Average Unemployment Rate (%)"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.markdown("---")

# --------------------------------------------------
# Employment Comparison
# --------------------------------------------------

st.subheader("👥 Employment Before and During COVID-19")

employment_comparison = pd.DataFrame({
    "Period": [
        "Pre-COVID Period",
        "COVID-19 Period"
    ],
    "Average Estimated Employed": [
        pre_covid["Estimated Employed"].mean(),
        covid_period["Estimated Employed"].mean()
    ]
})

fig3 = px.bar(
    employment_comparison,
    x="Period",
    y="Average Estimated Employed",
    text_auto=".0f",
    title="Average Estimated Employment Comparison"
)

fig3.update_layout(
    xaxis_title="Period",
    yaxis_title="Estimated Employed"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

st.markdown("---")

# --------------------------------------------------
# Labour Participation Comparison
# --------------------------------------------------

st.subheader("📊 Labour Participation Before and During COVID-19")

labour_comparison = pd.DataFrame({
    "Period": [
        "Pre-COVID Period",
        "COVID-19 Period"
    ],
    "Average Labour Participation Rate": [
        pre_covid[
            "Estimated Labour Participation Rate (%)"
        ].mean(),
        covid_period[
            "Estimated Labour Participation Rate (%)"
        ].mean()
    ]
})

fig4 = px.bar(
    labour_comparison,
    x="Period",
    y="Average Labour Participation Rate",
    text_auto=".2f",
    title="Labour Participation Rate Comparison"
)

fig4.update_layout(
    xaxis_title="Period",
    yaxis_title="Labour Participation Rate (%)"
)

st.plotly_chart(
    fig4,
    use_container_width=True
)

st.markdown("---")

# --------------------------------------------------
# Regional COVID Impact
# --------------------------------------------------

st.subheader("🗺️ Regional COVID-19 Impact")

if selected_region == "All Regions":

    regional_covid = (
        filtered_df
        .groupby(["Region", "Period"], as_index=False)[
            "Estimated Unemployment Rate (%)"
        ]
        .mean()
    )

    fig5 = px.bar(
        regional_covid,
        x="Region",
        y="Estimated Unemployment Rate (%)",
        color="Period",
        barmode="group",
        title="Regional Unemployment: Pre-COVID vs COVID-19"
    )

    fig5.update_layout(
        xaxis_title="Region",
        yaxis_title="Average Unemployment Rate (%)",
        xaxis_tickangle=-45
    )

    st.plotly_chart(
        fig5,
        use_container_width=True
    )

else:

    st.info(
        f"📍 Showing COVID-19 impact for **{selected_region}**."
    )

# --------------------------------------------------
# COVID-19 Impact Summary
# --------------------------------------------------

st.markdown("---")

st.subheader("💡 COVID-19 Impact Summary")

if change > 0:
    unemployment_message = (
        f"The average unemployment rate increased by "
        f"**{change:.2f} percentage points** during the COVID-19 period "
        f"compared with the pre-COVID period."
    )
elif change < 0:
    unemployment_message = (
        f"The average unemployment rate decreased by "
        f"**{abs(change):.2f} percentage points** during the COVID-19 period "
        f"compared with the pre-COVID period."
    )
else:
    unemployment_message = (
        "The average unemployment rate remained approximately "
        "unchanged between the two periods."
    )

st.info(unemployment_message)

if employment_change < 0:
    st.warning(
        f"Average estimated employment decreased by "
        f"**{abs(employment_change):,.0f}** during the COVID-19 period."
    )
elif employment_change > 0:
    st.info(
        f"Average estimated employment increased by "
        f"**{employment_change:,.0f}** during the COVID-19 period."
    )
else:
    st.info(
        "Average estimated employment remained approximately unchanged."
    )

# --------------------------------------------------
# Methodology
# --------------------------------------------------

st.markdown("---")

st.subheader("📝 Analysis Methodology")

st.markdown(
    """
    - **Pre-COVID Period:** Data before March 2020
    - **COVID-19 Period:** Data from March 2020 onwards
    - Unemployment rates are compared using the average values
      for each period.
    - Regional comparisons are based on the available records
      in the dataset.
    - The COVID-19 period definition is an analytical convention
      used for this project.
    """
)

st.markdown("---")

st.caption(
    "CodeAlpha Internship | Task 2 — Unemployment Analysis"
)