import streamlit as st
import pandas as pd
from openai import OpenAI

# --- UI Setup ---
st.set_page_config(page_title="Inventory AI", page_icon="📦")
st.title("📦 AI Inventory Risk Summarizer")
st.write("Bristlecone Supply Chain MVP (OpenAI SDK + Groq)")

# Secure API Key Input
api_key = st.text_input("Enter your Free Groq API Key to continue:", type="password")

# --- Step 1: The Data (Pandas) ---
data = {
    'Item_Name': ['Microchips', 'Cooling Fans', 'Power Supplies', 'Motherboards'],
    'Current_Stock': [45, 120, 800, 30],
    'Reorder_Level': [500, 150, 400, 100],
    'Supplier': ['Global Tech', 'AeroCool', 'VoltCorp', 'Global Tech']
}
df = pd.DataFrame(data)

st.subheader("1. Current Global Inventory")
st.dataframe(df, use_container_width=True)

# --- Step 2: The Logic ---
if st.button("Run AI Risk Analysis", type="primary"):
    if not api_key:
        st.error("Please enter your Groq API Key at the top!")
    else:
        # Filter the dataframe for only low-stock items
        low_stock_df = df[df['Current_Stock'] < df['Reorder_Level']]
        
        st.warning(f"⚠️ Detected {len(low_stock_df)} items currently below minimum reorder levels.")
        st.dataframe(low_stock_df, use_container_width=True)

        # --- Step 3: The AI Integration (The Developer Loophole) ---
        st.subheader("2. AI Executive Summary")
        
        # We use the official OpenAI tool, but point it to Groq's free servers!
        client = OpenAI(
            base_url="https://api.groq.com/openai/v1",
            api_key=api_key
        )
        
        data_string = low_stock_df.to_string(index=False)
        prompt = f"Act as a strict supply chain analyst. Here is a list of critical inventory items below reorder levels:\n\n{data_string}\n\nWrite a brief, 3-bullet-point executive summary highlighting the immediate risks to production."

        with st.spinner("Generating insights at lightning speed..."):
            # Groq runs the open-source LLaMA-3 model incredibly fast
            response = client.chat.completions.create(
                model="openai/gpt-oss-120b",
                messages=[
                    {"role": "system", "content": "You are a supply chain expert."},
                    {"role": "user", "content": prompt}
                ]
            )
            
            st.success("Analysis Complete")
            st.write(response.choices[0].message.content)