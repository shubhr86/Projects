# 🍬  Nassau Candy Distributor Project | Factory Reallocation & Shipping Optimization System

## 📌 Overview
This project analyzes logistics inefficiencies at Nassau Candy Distributor and builds a system to recommend better factory assignments.

The goal is to reduce shipping time and improve operational efficiency using data analysis, simulation, and optimization techniques.

---

## 🎯 Problem Statement
Nassau Candy currently assigns products to factories using fixed rules. This leads to:

- High shipping lead time  
- Poor route efficiency  
- Increased operational cost  
- No way to test better factory assignments  

---

## 💡 Solution
This project builds a decision-support system that:

- Simulates product allocation across different factories  
- Compares shipping performance  
- Recommends the best factory for each product  
- Provides an interactive dashboard for analysis  

---

## ⚙️ Technologies Used
- Python  
- Pandas & NumPy  
- Scikit-learn  
- Streamlit  
- Data Visualization  

---

## 📊 Key Features

### 1. Factory Optimization Simulator
- Select product and region  
- Get best factory recommendation  

### 2. What-If Scenario Analysis
- Compare current vs recommended factory  
- Analyze impact on delivery time  

### 3. Recommendation System
- Rank factories based on performance  
- Identify best and worst options  

### 4. Route Performance Analysis
- Detect slow and congested routes  
- Identify logistics bottlenecks  

### 5. KPI Dashboard
- Lead Time Reduction (%)  
- Recommendation Coverage (%)  
- Scenario Confidence Score  

---

## 📈 Key Results

- **Lead Time Reduction:** ~8.9%  
- **Time Saved:** ~118 days  
- **Best Factory:** The Other Factory  
- **Worst Route:** Sugar Shack → Pacific  
- **Recommendation Coverage:** 100%  

---

## 🧠 Methodology

### 1. Data Preparation
- Cleaned dataset  
- Converted date columns  
- Created Lead Time feature  
- Calculated profit margin  

### 2. Modeling
- Linear Regression  
- Random Forest  
- Model evaluation using MAE, RMSE, R²  

### 3. Scenario Simulation
- Tested each product across all factories  
- Generated multiple factory-region combinations  

### 4. Optimization Logic
- Ranked factories using lead time  
- Selected best factory based on efficiency  

### 5. Clustering
- Used KMeans to group routes  
- Identified slow and efficient routes  

---

## 🖥️ Live Dashboard

👉 **Streamlit App Link:**  
https://projects-sfqcsauqsphqyhappr2rdxh.streamlit.app/

---

## ▶️ How to Run Locally

### 1. Install dependencies
