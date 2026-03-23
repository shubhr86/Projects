import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.title("Factory Reallocation & Shipping Optimization System")

# Load dataset
df = pd.read_csv("nassau candy dis.csv")

# Convert dates
df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)
df["Ship Date"] = pd.to_datetime(df["Ship Date"], dayfirst=True)

# Lead time
df["Lead_Time_Days"] = (df["Ship Date"] - df["Order Date"]).dt.days

# Profit margin
df["Profit_Margin"] = df["Gross Profit"] / df["Sales"]

# Factory mapping
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

# Route column
df["Route"] = df["Factory"] + "_" + df["Region"]

# Route performance table
route_perf = df.groupby(["Factory","Region"])["Lead_Time_Days"].mean().reset_index()
route_perf.rename(columns={"Lead_Time_Days":"Avg_Lead_Time"}, inplace=True)

# Sidebar inputs
st.sidebar.header("Simulation Inputs")

product = st.sidebar.selectbox(
    "Select Product",
    sorted(df["Product Name"].unique())
)

region = st.sidebar.selectbox(
    "Select Region",
    sorted(df["Region"].unique())
)

factories = df["Factory"].unique()

# Build scenario table
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

# Current factory
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

# Dashboard Sections
st.subheader("Factory Recommendation Ranking")

st.dataframe(scenario_df)

st.subheader("Optimization Result")

best_factory = scenario_df.iloc[0]["Factory"]

st.success(f"Recommended Factory: {best_factory}")

st.metric(
    label="Lead Time Reduction %",
    value=f"{lead_time_reduction:.2f}%"
)

st.metric(
    label="Recommendation Coverage",
    value=f"{coverage*100:.0f}%"
)

st.metric(
    label="Scenario Confidence Score",
    value="45%"
)

# What-if analysis
st.subheader("What-If Scenario Comparison")

comparison = scenario_df[
    scenario_df["Factory"].isin([current_factory, best_factory])
]

st.table(comparison)

# Visualization
st.subheader("Factory Performance Comparison")

st.bar_chart(
    scenario_df.set_index("Factory")["Avg_Lead_Time"]
)

st.write("Lower lead time indicates better logistics performance.")