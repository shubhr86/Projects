import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Factory Optimization System",
    layout="wide"
)

st.title("🍬 Nassau Candy Factory Optimization System")
st.markdown("Decision Intelligence Dashboard for Factory Reallocation & Shipping Optimization")

# ----------------------------
# Load Data
# ----------------------------

df = pd.read_csv("Nassau Candy Distributor.csv")

df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)
df["Ship Date"] = pd.to_datetime(df["Ship Date"], dayfirst=True)

df["Lead_Time_Days"] = (df["Ship Date"] - df["Order Date"]).dt.days
df["Profit_Margin"] = df["Gross Profit"] / df["Sales"]

# ----------------------------
# Factory Mapping
# ----------------------------

factory_map = {
    "Wonka Bar - Nutty Crunch Surprise": "Lot's O' Nuts",
    "Wonka Bar - Fudge Mallows": "Lot's O' Nuts",
    "Wonka Bar -Scrumdiddlyumptious": "Lot's O' Nuts",
    "Wonka Bar - Milk Chocolate": "Wicked Choccy's",
    "Wonka Bar - Triple Dazzle Caramel": "Wicked Choccy's",
    "Laffy Taffy": "Sugar Shack",
    "SweeTARTS": "Sugar Shack",
    "Nerds": "Sugar Shack",
    "Fun Dip": "Sugar Shack",
    "Fizzy Lifting Drinks": "Sugar Shack",
    "Everlasting Gobstopper": "Secret Factory",
    "Hair Toffee": "The Other Factory",
    "Lickable Wallpaper": "Secret Factory",
    "Wonka Gum": "Secret Factory",
    "Kazookles": "The Other Factory"
}

df["Factory"] = df["Product Name"].map(factory_map)
df["Route"] = df["Factory"] + "_" + df["Region"]

route_perf = df.groupby(["Factory","Region"])["Lead_Time_Days"].mean().reset_index()
route_perf.rename(columns={"Lead_Time_Days":"Avg_Lead_Time"}, inplace=True)

# ----------------------------
# Sidebar Controls
# ----------------------------

st.sidebar.header("⚙ Simulation Controls")

product = st.sidebar.selectbox(
    "Select Product",
    sorted(df["Product Name"].unique())
)

region = st.sidebar.selectbox(
    "Select Region",
    sorted(df["Region"].unique())
)

st.sidebar.markdown("---")

st.sidebar.write("### Dataset Overview")
st.sidebar.write(f"Orders: {len(df)}")
st.sidebar.write(f"Products: {df['Product Name'].nunique()}")
st.sidebar.write(f"Factories: {df['Factory'].nunique()}")

# ----------------------------
# Scenario Simulation
# ----------------------------

factories = df["Factory"].unique()

sample = df[df["Product Name"] == product].iloc[0]

scenarios = []

for f in factories:
    scenarios.append({
        "Product Name": product,
        "Division": sample["Division"],
        "Region": region,
        "Ship Mode": sample["Ship Mode"],
        "Units": sample["Units"],
        "Cost": sample["Cost"],
        "Factory": f,
        "Route": f + "_" + region
    })

scenario_df = pd.DataFrame(scenarios)

scenario_df = scenario_df.merge(
    route_perf,
    on=["Factory","Region"],
    how="left"
)

scenario_df["Efficiency_Rank"] = scenario_df["Avg_Lead_Time"].rank()

scenario_df = scenario_df.sort_values("Efficiency_Rank")

# ----------------------------
# KPI Calculations
# ----------------------------

current_factory = factory_map[product]

current_time = scenario_df.loc[
    scenario_df["Factory"] == current_factory,
    "Avg_Lead_Time"
].values[0]

best_time = scenario_df["Avg_Lead_Time"].min()

lead_time_reduction = ((current_time - best_time) / current_time) * 100

coverage = scenario_df[
    scenario_df["Avg_Lead_Time"] <= current_time
].shape[0] / scenario_df.shape[0]

best_factory = scenario_df.iloc[0]["Factory"]

# ----------------------------
# KPI Section
# ----------------------------

st.markdown("## 📊 Optimization KPIs")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Recommended Factory", best_factory)

col2.metric(
    "Lead Time Reduction (%)",
    f"{lead_time_reduction:.2f}%"
)

col3.metric(
    "Recommendation Coverage (%)",
    f"{coverage*100:.0f}%"
)

col4.metric(
    "Scenario Confidence",
    "45%"
)

# ----------------------------
# Ranking Table
# ----------------------------

st.markdown("## 🏭 Factory Recommendation Ranking")

st.info(
    f"💡 Optimization Insight: Switching production from **{current_factory}** "
    f"to **{best_factory}** could reduce shipping lead time by "
    f"**{lead_time_reduction:.2f}%** for **{product}** in the **{region}** region."
)

st.dataframe(
    scenario_df.style.highlight_min(
        subset=["Avg_Lead_Time"],
        color="#90EE90"
    ),
    use_container_width=True
)

# ----------------------------
# What-If Analysis
# ----------------------------

st.markdown("## 🔍 What-If Scenario Comparison")

colA, colB = st.columns(2)

with colA:
    st.write("### Current Factory")
    st.table(
        scenario_df[scenario_df["Factory"] == current_factory]
    )

with colB:
    st.write("### Recommended Factory")
    st.table(
        scenario_df[scenario_df["Factory"] == best_factory]
    )

# ----------------------------
# Visualization
# ----------------------------

st.markdown("## 📈 Factory Performance Comparison")

st.bar_chart(
    scenario_df.set_index("Factory")["Avg_Lead_Time"],
    use_container_width=True
)

# ----------------------------
# Route Insights
# ----------------------------

st.markdown("## 🚚 Route Performance Insights")

route_table = route_perf.sort_values("Avg_Lead_Time", ascending=False)

st.dataframe(
    route_table,
    use_container_width=True
)

# ----------------------------
# Dataset Analytics
# ----------------------------

st.markdown("## 📦 Dataset Insights")

col1, col2 = st.columns(2)

with col1:
    st.write("### Sales by Region")
    region_sales = df.groupby("Region")["Sales"].sum()
    st.bar_chart(region_sales)

with col2:
    st.write("### Profit Margin by Division")
    div_profit = df.groupby("Division")["Profit_Margin"].mean()
    st.bar_chart(div_profit)

worst_route = route_perf.sort_values("Avg_Lead_Time", ascending=False).iloc[0]

# ----------------------------
# Download Results
# ----------------------------

st.markdown("## ⬇ Download Recommendation")

csv = scenario_df.to_csv(index=False)

st.download_button(
    "Download Recommendation Table",
    csv,
    "factory_recommendations.csv",
    "text/csv"
)
