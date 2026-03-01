# 📊 Workforce & Sales Intelligence Dashboard – Insights

## 📌 Project Overview

This project presents a dynamic **Workforce & Sales Intelligence Dashboard** built using Microsoft Excel.  
The objective was to transform raw Amazon retail sales data into an interactive reporting solution to support business decision-making.

The dashboard analyzes revenue trends, regional performance, cancellation behavior, delivery efficiency, and customer contribution using Pivot Tables, XLOOKUP, KPI cards, and slicers.

---

## 📂 Dataset Description

The dataset contains 100 sales transactions with the following key fields:

- Order ID
- Order Date
- Delivery Date
- Cancel Date
- Customer ID
- Customer Name
- Customer Type
- Product ID
- Product Name
- Category
- Region
- Sale Price per Unit
- Quantity
- Total Amount
- Payment Method
- Delivery Status
- Fulfillment Partner
- Order Flag
- Delivery Performance
- Delivery Days
- Target Sales (Region-level target)

Additional reference sheets:
- `ProductMaster`
- `CustomerMaster`
- `RegionGoals`

---

## 🧹 Data Cleaning & Preparation

Key preprocessing steps:

- Standardized date formats
- Created **Delivery Days** column (Delivery Date – Order Date)
- Built **Delivery Performance logic**:
  - Fast (≤ 2 days)
  - Slow (> 2 days)
  - Not Delivered
- Created **Order Flag** to distinguish Cancelled vs Active orders
- Used **XLOOKUP** to merge:
  - Customer details
  - Product categories
  - Regional sales targets

---

## 🛠 Excel Features Used

- Pivot Tables
- XLOOKUP
- IF, IFERROR, AVERAGEIFS, COUNTIFS
- Date calculations
- Pivot Charts (Bar, Pie, Donut)
- Slicers for dynamic filtering
- Conditional formatting
- KPI Cards linked to pivot totals

---

## 📊 Dashboard Structure

### 🔹 Left Panel – Interactive Filters
- Month (Order Date grouping)
- Region
- Payment Method
- Delivery Status
- Category

### 🔹 Center Panel – Visual Insights
- Sales by Region & Category
- Category-wise Revenue Distribution
- Sales by Payment Method
- Delivery Status Breakdown
- Target vs Actual Sales by Region
- Fulfillment Partner Performance
- Customer Type Contribution

### 🔹 Right Panel – KPI Cards
- Total Revenue
- Total Quantity
- Cancellation Rate (dynamic)
- % of Fast Deliveries
- Average Delivery Days
- Highest Revenue Product

All KPIs are fully slicer-responsive.

---

## 📈 Key Business Insights

- Electronics is the highest revenue-generating category.
- North region has the highest cancellation rate.
- Fast deliveries represent a limited percentage of total deliveries.
- Certain fulfillment partners perform better in delivery timelines.
- Regional targets reveal performance gaps.

---

## 📐 Cancellation Rate Logic


The KPI updates dynamically based on slicer selections and avoids division errors.

---

## 🔎 How XLOOKUP Improved Analysis

XLOOKUP enabled seamless integration of:

- Customer details
- Product data
- Regional targets

This reduced manual matching and ensured accurate cross-sheet reporting.

---

## 💡 Recommendations

- Improve logistics coordination in high-cancellation regions
- Increase fast-delivery rate through operational improvements
- Monitor target vs actual sales monthly
- Optimize fulfillment partner allocation

---

## 🎥 Dashboard Walkthrough Video

[![Watch the Dashboard Demo](https://github.com/shubhr86/Projects/blob/main/Excel/dashboard.png)](https://youtu.be/IB-NOuTtyGo)


---

## 👨‍💻 Author

**Shubham Kumar**   
GitHub: https://github.com/shubhr86  
LinkedIn: https://www.linkedin.com/in/shubhr86/

---
