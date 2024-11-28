# app/query_interface/mock_data.py
import os
import pandas as pd

def generate_kpi_data():
    # Check if 'data' folder exists, if not, create it
    if not os.path.exists('data'):
        os.makedirs('data')
        print("Data folder created!")

    kpi_data = {
        "company_name": ["Tech Innovators", "Green Energy Solutions", "FinTech Plus"],
        "revenue": [100000, 150000, 120000],
        "expenses": [50000, 60000, 55000],
        "profit_margin": [50, 60, 45],  # As percentage
        "customer_growth": [30, 40, 25],  # As percentage
    }
    df = pd.DataFrame(kpi_data)
    df.to_csv(os.path.join("data","kpi_data.csv"), index=False)
    print("KPI data saved to data/kpi_data.csv")

generate_kpi_data()
