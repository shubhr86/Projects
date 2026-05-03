# 📊 Customer Data Analysis for Business Insights

## 📌 1. Project Overview

This project focuses on analyzing customer data for a mid-sized Indian retail company.
The goal is to understand customer behavior, improve marketing strategies, and identify high-value customers using data analysis techniques.

This project was completed using **Python, Pandas, and Data Visualization libraries** in Jupyter Notebook.

---

## 🎯 2. Business Problem

The company wants to:

* Improve targeted marketing campaigns
* Retain valuable customers
* Identify patterns in customer purchasing behavior

As a data analyst, my task was to clean, process, and analyze the data to generate useful business insights.

---

## 🎯 3. Objectives

* Analyze customer demographics and transaction behavior
* Clean and prepare the dataset
* Perform **RFM (Recency, Frequency, Monetary) analysis**
* Segment customers based on behavior
* Create visualizations for better understanding
* Provide business insights and recommendations

---

## 📊 4. Dataset Description

The dataset contains:

* **1000 customers**
* **23,050 transactions**

### 🧾 Customer Master Data

| Column        | Description        |
| ------------- | ------------------ |
| CustomerID    | Unique customer ID |
| Name          | Customer name      |
| Email         | Email ID           |
| Gender        | Male / Female      |
| Age           | Age of customer    |
| City          | Customer location  |
| MaritalStatus | Marital status     |
| NumChildren   | Number of children |
| JoinDate      | Registration date  |

---

### 💳 Transaction Data

| Column            | Description             |
| ----------------- | ----------------------- |
| CustomerID        | Links to customer table |
| TransactionDate   | Date of purchase        |
| TransactionAmount | Amount spent            |

---

## 🧠 5. RFM Analysis Concept

RFM is used to identify valuable customers.

| Metric    | Meaning                           |
| --------- | --------------------------------- |
| Recency   | How recently a customer purchased |
| Frequency | How often they purchase           |
| Monetary  | How much they spend               |

---

## ⚙️ 6. Steps Performed

### 🔹 Step 1: Data Loading

* Imported CSV files using Pandas
* Checked dataset shape and preview

---

### 🔹 Step 2: Data Cleaning

* Converted `JoinDate` and `TransactionDate` to datetime
* Checked missing values (no major issues found)
* Verified unique `CustomerID`
* Ensured all transaction IDs exist in master data

---

### 🔹 Step 3: RFM Calculation

* Set reference date = latest transaction date + 1 day
* Calculated:

  * Recency → Days since last purchase
  * Frequency → Number of transactions
  * Monetary → Total spend

---

### 🔹 Step 4: RFM Scoring

* Used `pd.qcut()` to assign scores (1–5)
* Rules:

  * Low Recency = High Score
  * High Frequency = High Score
  * High Monetary = High Score

---

### 🔹 Step 5: Customer Segmentation

Created segments using business rules:

* Champions
* Loyal Customers
* Potential Loyalists
* Big Spenders
* At Risk
* Lost
* Others

---

### 🔹 Step 6: Data Visualization

Created multiple charts:

* Customer distribution by segment
* Revenue contribution by segment
* Recency vs Monetary scatter plot
* Pareto analysis (80/20 rule)

---

## 📈 7. Key Insights

* Total customers: **1000**

* Total transactions: **23,050**

* **Big Spenders generate the highest revenue**

* **Champions and Loyal Customers are highly valuable segments**

* **Potential Loyalists can be converted into loyal customers**

* A large number of customers fall into the **"Others" category**

* Pareto analysis shows:

  * Around **75% customers generate 80% of revenue**
  * Revenue is distributed across many customers

* **At-risk and lost customers need re-engagement strategies**

---

## 💡 8. Business Recommendations

* Reward **Champions** with loyalty programs
* Offer discounts to **Potential Loyalists**
* Upsell to **Big Spenders**
* Re-engage **At Risk customers** with campaigns
* Analyze **Lost customers** to reduce churn

---

## 🛠️ 9. Tools & Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Jupyter Notebook

---

## 📌 10. Conclusion

This project successfully used RFM analysis to segment customers and generate actionable insights.

The results can help the company:

* Improve marketing strategies
* Increase customer retention
* Boost revenue through targeted campaigns

---

## 📎 Author

**Shubham Kumar**
Aspiring Data Analyst
GitHub: https://github.com/shubhr86
LinkedIn: https://www.linkedin.com/in/shubhr86/

---


