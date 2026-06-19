import pandas as pd

def build_customer360(customer):

    profile = {
        "Customer_ID": customer["Customer_ID"],
        "Churn_Risk": customer["Churn_Probability"],
        "Predicted_Revenue": customer["Revenue_Forecast"],
        "Segment": customer["Segment"]
    }

    return profile