# Enterprise AI-Powered Customer Analytics and Strategic Insight Framework

## Project Overview

This project is an Enterprise AI-Powered Customer Analytics Framework designed to help organizations understand customer behavior, predict future outcomes, and make data-driven business decisions.

The system combines Customer Churn Prediction, Revenue Forecasting, Customer Segmentation, and Customer 360 Analysis into a single analytics platform. An interactive Streamlit dashboard is used to visualize insights and support strategic decision-making.

---

## Problem Statement

Organizations collect large amounts of customer data but often struggle to convert it into actionable insights. This project addresses that challenge by developing an intelligent analytics framework capable of:

* Predicting customer churn
* Forecasting future revenue
* Segmenting customers into meaningful groups
* Providing Customer 360 insights
* Supporting business strategy through data analytics

---

## Project Objectives

* Predict customer churn using Machine Learning
* Forecast future customer revenue
* Perform customer segmentation
* Build a Customer 360 profile
* Create an interactive dashboard using Streamlit
* Generate actionable business insights

---

## Dataset Description

### Datasets Used

* fact_customers.csv
* fact_transactions.csv
* fact_usage_monthly.csv
* fact_engagement_events.csv
* dim_geography.csv
* dim_industry.csv
* dim_product.csv

### Important Features

* Customer_ID
* Health_Score
* Tenure_Months
* Daily_Active_Users
* Lifetime_Revenue_USD
* Support_Tickets
* CSAT_Score
* NPS_Score
* Churn
* Next_Quarter_Revenue_USD

---

## Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Scikit-Learn
* XGBoost
* Imbalanced-Learn (SMOTE)
* Matplotlib
* Seaborn
* Streamlit
* Joblib

---

## Machine Learning Models

### 1. Customer Churn Prediction

Algorithm Used:

* XGBoost Classifier

Target Variable:

```text
Churn
```

Purpose:

Predict customers who are likely to leave the company.

---

### 2. Revenue Forecasting

Algorithm Used:

* Gradient Boosting Regressor

Target Variable:

```text
Next_Quarter_Revenue_USD
```

Purpose:

Predict future customer revenue.

---

### 3. Customer Segmentation

Algorithm Used:

* K-Means Clustering

Features Used:

* Tenure_Months
* Lifetime_Revenue_USD
* Health_Score
* Support_Tickets
* Daily_Active_Users

Purpose:

Group customers into meaningful segments for business analysis.

---

## Project Structure

```text
enterprise-customer-analytics/
│
├── data/
│   ├── fact_customers.csv
│   ├── fact_transactions.csv
│   ├── fact_usage_monthly.csv
│   ├── fact_engagement_events.csv
│   ├── dim_geography.csv
│   ├── dim_industry.csv
│   └── dim_product.csv
│
├── models/
│   ├── churn_model.pkl
│   ├── revenue_model.pkl
│   └── clustering_model.pkl
│
├── train_models.py
├── dataset_check.py
├── eda.py
├── app.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone Repository

```bash
git clone https://github.com/Vamsee7555/enterprise-customer-analytics.git
```

Navigate to Project Folder

```bash
cd enterprise-customer-analytics
```

Install Required Packages

```bash
pip install -r requirements.txt
```

---

## Running the Project

### Dataset Validation

```bash
python dataset_check.py
```

### Exploratory Data Analysis

```bash
python eda.py
```

### Train Models

```bash
python train_models.py
```

### Run Dashboard

```bash
streamlit run app.py
```

---

## Output

The system provides:

* Churn Risk Prediction
* Revenue Forecasting
* Customer Segmentation
* Customer 360 Profile
* Business Insights Dashboard

---

## Business Benefits

* Improved Customer Retention
* Better Revenue Planning
* Personalized Customer Engagement
* Strategic Decision Making
* Increased Customer Lifetime Value

---

## Future Enhancements

* Real-Time Prediction Engine
* Deep Learning Models
* Cloud Deployment
* Generative AI Recommendations
* Automated Reporting

---

## Conclusion

The Enterprise AI-Powered Customer Analytics and Strategic Insight Framework successfully integrates customer analytics and machine learning to provide actionable business intelligence. The system enables organizations to predict customer behavior, forecast revenue, segment customers, and improve strategic decision-making.

---

## Author

Vamsee Krishna M
