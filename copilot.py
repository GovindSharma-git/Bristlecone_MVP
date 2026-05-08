import streamlit as st
import pandas as pd
from openai import OpenAI

# --- UI Setup ---
st.set_page_config(page_title="Email Copilot", page_icon="✉️")
st.title("✉️ Automated Supplier Email Copilot")
st.write("Bristlecone Procurement MVP (OpenAI SDK + Groq)")

# Secure API Key Input
api_key = st.text_input("Enter your Free Groq API Key to continue:", type="password")

# --- Step 1: The Data (Pandas) ---
# Simulating a database of delayed shipments
data = {
    'Supplier': ['TechLogistics Inc.', 'Global Components Ltd.', 'Apex Shipping'],
    'Delayed_Item': ['Microchips', 'Cooling Fans', 'Optical Sensors'],
    'Days_Late': [14, 5, 2],
    'Impact_Level': ['Critical', 'Medium', 'Low']
}
df = pd.DataFrame(data)

st.subheader("1. Active Delayed Shipments")
st.dataframe(df, use_container_width=True)

# --- Step 2: The Logic & AI Integration ---
if st.button("Generate Follow-up Emails", type="primary"):
    if not api_key:
        st.error("Please enter your Groq API Key at the top!")
    else:
        st.subheader("2. AI Generated Drafts")
        
        # Initialize the AI client via Groq
        client = OpenAI(
            base_url="https://api.groq.com/openai/v1",
            api_key=api_key
        )
        
        # We loop through EVERY row in the Pandas dataframe
        for index, row in df.iterrows():
            
            # Build a highly specific, dynamic prompt for this exact supplier
            prompt = f"Write a professional but firm follow-up email to {row['Supplier']} regarding their shipment of {row['Delayed_Item']} which is {row['Days_Late']} days late. The business impact of this delay is {row['Impact_Level']}. Keep the draft under 80 words."
            
            with st.spinner(f"Drafting email to {row['Supplier']}..."):
                response = client.chat.completions.create(
                        model="meta-llama/llama-4-scout-17b-16e-instruct",
                    messages=[
                        {"role": "system", "content": "You are a highly efficient corporate procurement manager."},
                        {"role": "user", "content": prompt}
                    ]
                )
                
                # Streamlit Magic: Put each email in a clean, clickable dropdown box
                with st.expander(f"✉️ Draft for {row['Supplier']} ({row['Delayed_Item']})"):
                    st.write(response.choices[0].message.content)