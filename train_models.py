import pandas as pd
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score, r2_score
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.cluster import KMeans

from xgboost import XGBClassifier
from imblearn.over_sampling import SMOTE

# Create models folder
os.makedirs("models", exist_ok=True)

# Load dataset
df = pd.read_csv("data/fact_customers.csv")

# Convert date columns
date_cols = ["Contract_Start_Date", "Contract_End_Date"]

for col in date_cols:
    df[col] = pd.to_datetime(df[col], errors="coerce")
    df[col] = df[col].astype("int64") // 10**9

# Encode categorical columns
for col in df.select_dtypes(include="object").columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col].astype(str))

# Fill missing values
imputer = SimpleImputer(strategy="most_frequent")
df = pd.DataFrame(
    imputer.fit_transform(df),
    columns=df.columns
)

print("Missing Values Remaining:", df.isnull().sum().sum())

# -----------------------
# CHURN MODEL
# -----------------------

X = df.drop(
    ["Churn", "Next_Quarter_Revenue_USD"],
    axis=1
)

y = df["Churn"]

smote = SMOTE(random_state=42)

X_res, y_res = smote.fit_resample(X, y)

X_train, X_test, y_train, y_test = train_test_split(
    X_res,
    y_res,
    test_size=0.2,
    random_state=42
)

churn_model = XGBClassifier(
    eval_metric="logloss",
    random_state=42
)

churn_model.fit(X_train, y_train)

pred = churn_model.predict(X_test)

print("Churn Accuracy:", accuracy_score(y_test, pred))

joblib.dump(
    churn_model,
    "models/churn_model.pkl"
)

# -----------------------
# REVENUE MODEL
# -----------------------

X_rev = df.drop(
    ["Next_Quarter_Revenue_USD"],
    axis=1
)

y_rev = df["Next_Quarter_Revenue_USD"]

X_train, X_test, y_train, y_test = train_test_split(
    X_rev,
    y_rev,
    test_size=0.2,
    random_state=42
)

revenue_model = GradientBoostingRegressor()

revenue_model.fit(X_train, y_train)

pred_rev = revenue_model.predict(X_test)

print("Revenue R2 Score:", r2_score(y_test, pred_rev))

joblib.dump(
    revenue_model,
    "models/revenue_model.pkl"
)

# -----------------------
# CUSTOMER SEGMENTATION
# -----------------------

cluster_features = df[
    [
        "Tenure_Months",
        "Lifetime_Revenue_USD",
        "Health_Score",
        "Support_Tickets",
        "Daily_Active_Users"
    ]
]

kmeans = KMeans(
    n_clusters=4,
    random_state=42,
    n_init=10
)

kmeans.fit(cluster_features)

joblib.dump(
    kmeans,
    "models/clustering_model.pkl"
)

print("All Models Saved Successfully")