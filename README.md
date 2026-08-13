# 🍔 QuickBite Express: Crisis Impact & Recovery Analysis

> **A Data-Driven Strategy to measure business impact and drive recovery post-crisis.**

---

## 📌 Project Overview
QuickBite Express is a Bengaluru-based food-tech startup that faced a massive crisis in June 2025 due to a viral food safety incident and a monsoon-induced delivery outage. This project involves a comprehensive data-driven analysis to measure the true impact of the crisis on business operations and design a targeted recovery strategy for the leadership team.

---

## 📉 The Business Problem
During the June 2025 crisis, QuickBite experienced:
* A viral social media backlash regarding food safety violations.
* A severe delivery outage during the monsoon season.
* Aggressive competitor campaigns stealing market share.

**Objective:** To analyze customer segments, order patterns, and delivery performance (Pre-Crisis vs. Crisis) and build an interactive dashboard to recommend actionable recovery initiatives.

---

## 🛠️ Tech Stack & Tools
* **Language:** Python
* **Data Manipulation:** Pandas, NumPy
* **Data Visualization:** Matplotlib, Seaborn
* **Dashboard Deployment:** Streamlit, LocalTunnel
* **Environment:** Google Colab / Jupyter Notebook

---

## 📊 Key Insights & Findings
Through Exploratory Data Analysis (EDA) of over 149,000 orders and ratings, the following critical metrics were identified:
* **Severe Revenue Hemorrhage:** A **63.6% drop** in monthly revenue, leading to an estimated loss of ₹4.78M per month.
* **Logistics Breakdown:** On-time delivery (SLA compliance) plummeted from 43.6% down to a mere **12.2%**.
* **Customer Trust Decay:** Average customer ratings crashed from ~4.5 to **2.4 stars**.
* **Worst-Hit Geographies:** Chennai, Kolkata, and Bengaluru experienced the highest order volume declines (>61%).

---

## 💻 Interactive Recovery Dashboard
An interactive web application was built using **Streamlit** to allow stakeholders to dynamically track the crisis impact and review actionable insights.

*(Replace the line below with your actual dashboard screenshot link)*
`![Dashboard Screenshot](images/dashboard_screenshot.png)`

---

## 💡 Strategic Recommendations
* **Targeted Win-Back Campaigns:** Allocate maximum recovery budgets to high-drop regions like Chennai, Kolkata, and Bengaluru.
* **Delivery Infrastructure Audit:** Implement dynamic weather-based ETAs to fix the shattered SLA metrics and manage user expectations.
* **Safety Certification:** Roll out a highly visible "Safety Certified" badge on the app for partner restaurants passing rigorous health audits to combat negative sentiment (key pain points identified: 'Food', 'Quality', 'Safety').

---

## 📂 Repository Structure
```text
📁 QuickBite-Crisis-Recovery-Analysis/
│
├── 📁 data/
│   ├── fact_orders.csv
│   ├── fact_ratings.csv
│   ├── fact_delivery_performance.csv
│   ├── dim_customer.csv
│   └── dim_restaurant.csv
│
├── 📁 images/
│   ├── order_volume_trend.png
│   ├── ratings_trend.png
│   └── negative_keywords.png
│
├── QuickBite_Analysis.ipynb
├── app.py
├── Problem Statement.docx
└── README.md
