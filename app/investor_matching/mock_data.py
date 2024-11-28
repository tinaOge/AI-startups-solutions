# app/investor_matching/mock_data.py
import os
import pandas as pd

def generate_mock_data():

    # Create the 'data' folder if it doesn't exist
    data_dir = "data"
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        print(f"'{data_dir}' folder created successfully.")
    else:
        print(f"'{data_dir}' folder already exists.")


    # Startup Data
    startups = {
        "id": [1, 2, 3],
        "business_name": ["Tech Innovators", "Green Energy Solutions", "FinTech Plus"],
        "business_category": ["Technology", "Energy", "Finance"],
        "business_description": [
            "AI-driven tech solutions",
            "Renewable energy projects",
            "Advanced financial platforms"
        ],
        "target_audience": ["Enterprises", "Individuals", "SMBs"],
        "funding_stage": ["Seed", "Series A", "Growth"]
    }
    startups_df = pd.DataFrame(startups)
    startups_file = os.path.join(data_dir, "startups.csv")
    startups_df.to_csv(startups_file, index=False)
    print(f"Startup data saved to {startups_file}")

    # Investor Data
    investors = {
        "id": [101, 102, 103],
        "investor_name": ["Investor Alpha", "Investor Beta", "Investor Gamma"],
        "investment_preferences": ["Seed", "Series A", "Growth"],
        "industry_focus": ["Technology", "Energy", "Finance"]
    }
    investors_df = pd.DataFrame(investors)
    investors_file = os.path.join(data_dir, "investors.csv")
    investors_df.to_csv(investors_file, index=False)
    print(f"Investor data saved to {investors_file}")
    print("Startup and investor mock data saved!")

generate_mock_data()
