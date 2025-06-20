import pandas as pd
import numpy as np
import random

# Function to generate synthetic P&L data
def generate_pnl_data(n=1000):
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    
    data = []
    for _ in range(n):
        month = random.choice(months)
        year = random.choice([2022, 2023, 2024])
        
        revenue = random.randint(100000, 500000)
        cogs = int(revenue * random.uniform(0.4, 0.7))
        operating_expenses = int(revenue * random.uniform(0.2, 0.3))
        gross_profit = revenue - cogs
        net_income = gross_profit - operating_expenses

        marketing_expense = int(operating_expenses * random.uniform(0.2, 0.4))
        r_and_d_expense = int(operating_expenses * random.uniform(0.1, 0.3))
        admin_expense = operating_expenses - (marketing_expense + r_and_d_expense)

        data.append({
            "month": month,
            "year": year,
            "revenue": revenue,
            "COGS": cogs,
            "operating_expenses": operating_expenses,
            "gross_profit": gross_profit,
            "net_income": net_income,
            "marketing_expense": marketing_expense,
            "r_and_d_expense": r_and_d_expense,
            "admin_expense": admin_expense
        })

    return pd.DataFrame(data)

# Generate and save to Excel
df = generate_pnl_data()
df.to_excel("synthetic_pnl_data.xlsx", index=False)
print("✅ Data saved to 'synthetic_pnl_data.xlsx'")
