# Project Synapse – Agentic Last-Mile Coordinator 🚚🤖

## 📌 Overview
This is a proof-of-concept AI agent that handles last-mile delivery disruptions 
using simulated logistics tools. Built for **Grab Hackathon**.

## ⚡ Features
- Handles multiple disruption scenarios:
  - Overloaded Restaurant 🍔
  - Recipient Unavailable 📦
  - Traffic Obstruction 🚦
- Agent reasoning with step-by-step trace
- Hybrid Planner:
  - Uses OpenAI GPT (if available)
  - Falls back to RulePlanner when quota is exceeded

## 🛠️ Tech Stack
- Python 3.10+
- OpenAI API (LLM)
- LangChain-style agent loop (custom)
- PyYAML for scenario configs

## ▶️ How to Run
```bash
git clone https://github.com/<your-username>/project-synapse.git
cd project-synapse
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux
pip install -r requirements.txt

# Run a scenario
python main.py --scenario overloaded-restaurant
python main.py --scenario recipient-unavailable
python main.py --scenario traffic


project-synapse/
│── agent/
│   ├── controller.py
│   ├── llm.py
│   ├── state.py
│   ├── tools.py
│   └── __init__.py
│── scenarios/
│   └── scenarios.yaml
│── main.py
│── README.md
│── requirements.txt
│── .gitignore


---

# 🟢 Step 5: Add requirements.txt
Run this in your venv to generate dependencies:

```bash
pip freeze > requirements.txt

#It will include things like:
openai
pyyaml
python-dotenv