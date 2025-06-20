import pandas as pd
import os
import json

# Load the Excel file
df = pd.read_excel("synthetic_pnl_data.xlsx")

# Create output folder if it doesn't exist
output_folder = "monthly_jsons"
os.makedirs(output_folder, exist_ok=True)

# Loop through each row and save as a JSON file
for idx, row in df.iterrows():
    record = row.to_dict()
    file_name = f"{record['month']}_{record['year']}_{idx+1}.json"
    with open(os.path.join(output_folder, file_name), "w") as f:
        json.dump(record, f, indent=4)

print(f"✅ Created {len(df)} JSON files in the '{output_folder}' folder.")
