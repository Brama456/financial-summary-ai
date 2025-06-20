import streamlit as st
import json
import openai
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Streamlit page setup
st.set_page_config(page_title="📊 Financial Summary Generator", layout="centered")
st.title("📊 Financial Summary Generator")
st.markdown("Upload your monthly P&L JSON file to generate a CFO-ready executive summary.")

# File uploader
uploaded_file = st.file_uploader("Upload P&L JSON File", type=["json"])

# Template with placeholders
def build_prompt(pnl_data, month, year):
    return f"""
Subject: Monthly Financial Report – {month} {year}

You are a financial analyst tasked with summarizing a company's monthly performance.

Given the following Profit & Loss (P&L) data in JSON format, write a 200–250 word executive summary that includes:

- Total revenue and major cost components (COGS, operating expenses)
- Gross profit and net income
- Overall financial health and performance highlights
- Any anomalies, risks, or positive highlights worth noting

Present the summary professionally, as if for a CFO’s monthly review.

P&L Data:
{pnl_data}

Thnaks&regards,  
Bramarambika  
Financial Analyst
"""

# Generate summary using OpenAI
if uploaded_file is not None:
    try:
        pnl_data = json.load(uploaded_file)

        # Extract month/year if available
        month = pnl_data.get("month", "Unknown")
        year = pnl_data.get("year", "Unknown")

        prompt = build_prompt(json.dumps(pnl_data), month, year)

        with st.spinner("Generating executive summary..."):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a financial analyst."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=500
            )

        summary = response["choices"][0]["message"]["content"]
        st.success("✅ Summary Generated!")
        st.markdown("### 📄 Executive Summary")
        st.text(summary)


    except Exception as e:
        st.error(f"❌ Error: {e}")

