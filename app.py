import streamlit as st
import pandas as pd
import joblib

customers = pd.read_csv(
    "data/fact_customers.csv"
)

st.title(
    "Enterprise AI Powered Customer Analytics"
)

customer_id = st.selectbox(
    "Select Customer",
    customers["Customer_ID"]
)

customer = customers[
    customers["Customer_ID"] == customer_id
]

st.write(customer)

st.subheader("Customer Summary")

st.metric(
    "Revenue",
    customer["Lifetime_Revenue_USD"].values[0]
)

st.metric(
    "Health Score",
    customer["Health_Score"].values[0]
)

st.metric(
    "Support Tickets",
    customer["Support_Tickets"].values[0]
)

st.success(
    "AI Recommendation: Contact Customer Success Manager immediately."
)