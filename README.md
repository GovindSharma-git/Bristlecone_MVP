# Bristlecone_MVP
A collection of AI-powered supply chain and procurement MVPs. Built with Python, Pandas, and Streamlit, leveraging the OpenAI SDK and Groq's high-speed inference engine to automate enterprise workflows.
# 🚀 Enterprise Supply Chain AI Solutions (MVPs)

This repository contains two Minimum Viable Products (MVPs) designed to automate and optimize standard supply chain and procurement workflows. Both applications are built using a modern Python data stack and leverage Generative AI for real-time decision support and workflow automation.

## 🏗️ Technical Architecture & The "Groq Loophole"
To ensure enterprise-grade reliability while maintaining a zero-cost development environment, these applications utilize a custom API routing strategy:
* **The Interface:** Streamlit (for rapid, interactive web app deployment)
* **The Data Engine:** Pandas (for deterministic data filtering and manipulation)
* **The AI Integration:** The official `openai` Python SDK, dynamically routed through **Groq's** inference servers via a custom `base_url`. This allows the application to run massive open-weight models (like LLaMA-3 and GPT-OSS-120B) at ultra-low latency without incurring standard paid API costs.

---

## Project 1: 📦 AI Inventory Risk Summarizer

### Overview
A risk-analysis dashboard that prevents supply chain managers from manually hunting for inventory shortages. The tool ingests global inventory data, deterministically isolates critical shortages, and generates an executive-level risk report.

### How It Works
1. **Data Ingestion:** Reads inventory levels across multiple suppliers.
2. **Pandas Filtering:** Applies deterministic math (`Current_Stock < Reorder_Level`) to isolate only the items posing an immediate threat to production.
3. **AI Summarization:** Passes the filtered subset to a high-reasoning LLM to generate a strict, 3-bullet-point professional summary of the business risks.

# ✉️ Automated Supplier Email Copilot

An enterprise-grade Minimum Viable Product (MVP) designed to automate procurement and supply chain communication. This application instantly ingests delayed shipment data and utilizes Generative AI to draft highly customized, context-aware follow-up emails for suppliers.

## 🚀 The Business Problem
Procurement teams waste countless hours manually drafting repetitive follow-up emails for delayed inventory. This Copilot turns a multi-hour administrative bottleneck into a single-click automated workflow, allowing supply chain managers to focus on strategic negotiations rather than manual data entry.

## 🏗️ Technical Architecture
This application is built with a lightweight Python data stack and utilizes a custom API routing strategy to achieve enterprise-level reasoning at zero development cost.

* **Frontend:** Streamlit (Provides a clean, interactive UI for immediate deployment)
* **Data Engine:** Pandas (Handles data ingestion and iteration)
* **LLM Integration:** Built using the official `openai` Python SDK to maintain enterprise compliance, but dynamically routed through **Groq's** high-speed inference servers via a custom `base_url`. 
* **Model Used:** Configured to run OpenAI's massive `gpt-oss-120b` open-weight model to ensure top-tier reasoning and professional tone, while leveraging Groq's hardware for ultra-low latency.

## ⚙️ How It Works
1. **Data Iteration:** The script reads a Pandas DataFrame of active delayed shipments and iterates through the dataset row by row.
2. **Dynamic Prompt Injection:** For every delayed item, the application constructs a highly specific prompt injecting the exact `Supplier Name`, `Item`, `Days Late`, and `Business Impact Level`.
3. **Mass Generation:** The 120B model processes these specific parameters to instantly generate customized, professional email drafts, rendering them in an interactive dropdown UI.

## 🛠️ Local Setup Instructions

**1. Clone the repository and navigate to the directory:**
`git clone https://github.com/yourusername/email-copilot-mvp.git`
`cd email-copilot-mvp`

**2. Install the required dependencies:**
`pip install streamlit pandas openai`

**3. API Key Configuration:**
To run the AI features, you will need a free API key from [Groq](https://console.groq.com). The application will securely prompt you for this key via the Streamlit interface upon launch.

**4. Run the Application:**
`streamlit run copilot.py`
