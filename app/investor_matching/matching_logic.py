# app/investor_matching/matching_logic.py
import os
import pandas as pd

def match_investors(startup_id):
    startups = pd.read_csv(os.path.join("app", "investor_matching", "data", "startups.csv"))
    investors = pd.read_csv(os.path.join("app", "investor_matching", "data", "investors.csv"))

    # Find startup details
    startup = startups.loc[startups['id'] == startup_id].iloc[0]
    category = startup["business_category"]
    stage = startup["funding_stage"]

    # Match investors based on category and funding stage
    matched_investors = investors[
        (investors["industry_focus"] == category) &
        (investors["investment_preferences"] == stage)
    ]
    return matched_investors.to_dict(orient="records")

# Example Usage
print(match_investors(1))  # Matches investors for "Tech Innovators"
