# Project Synapse – Agentic Last-Mile Coordinator 🚚🤖

## 📌 Overview

Project Synapse is a **proof-of-concept AI agent** designed for the **Grab Hackathon**. It acts as an **intelligent coordinator** for last-mile delivery disruptions by simulating logistics APIs and reasoning step by step to resolve real-world issues like traffic delays, unavailable recipients, or overloaded merchants.

The agent follows a **Plan → Act → Observe → Reflect loop**, deciding which tools to use, observing results, and generating a final resolution.

* If OpenAI API is available (with quota), the agent uses an **LLM-powered planner**.
* If quota is exceeded or offline, it automatically falls back to a **Rule-based planner**.

This ensures the system is **robust and always demo-ready**.

---

## ⚡ Features

* **Handles multiple disruption scenarios**

  * 🍔 Overloaded Restaurant (GrabFood/GrabMart)
  * 📦 Recipient Unavailable (GrabExpress)
  * 🚦 Traffic Obstruction (GrabCar)
* **Step-by-step reasoning trace** printed to console
* **Hybrid Planner**: OpenAI GPT + Rule-based fallback
* **Tool simulation** (mock APIs):

  * `get_merchant_status()`
  * `notify_customer()`
  * `re_route_driver()`
  * `check_traffic()`
  * `calculate_alternative_route()`
  * `notify_passenger_and_driver()`
  * `contact_recipient_via_chat()`
  * `find_nearby_locker()`

---

## 🛠️ Tech Stack

* Python 3.10+
* [OpenAI API](https://platform.openai.com/) (LLM)
* [PyYAML](https://pyyaml.org/) (scenario configs)
* [python-dotenv](https://github.com/theskumar/python-dotenv) (API key management)

---

## 🗂️ Project Structure

```
project-synapse/
│── agent/
│   ├── controller.py   # agent loop (Plan → Act → Observe)
│   ├── llm.py          # OpenAI planner + Rule-based fallback
│   ├── state.py        # Agent state + ToolEvent dataclass
│   ├── tools.py        # Simulated logistics tools
│   └── __init__.py
│
│── scenarios/
│   └── scenarios.yaml  # Scenario definitions (restaurant, traffic, etc.)
│
│── main.py             # CLI entry point
│── README.md           # Documentation
│── requirements.txt    # Python dependencies
│── .gitignore          # Ignore venv, __pycache__, .env
```

---

## ▶️ How to Run

### 1. Clone Repo

```bash
git clone https://github.com/<your-username>/project-synapse.git
cd project-synapse
```

### 2. Setup Virtual Environment

```bash
python -m venv venv
# Activate venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add API Key (optional)

Create a `.env` file:

```
OPENAI_API_KEY=sk-xxxxxxx
```

If no quota → system automatically falls back to RulePlanner.

### 5. Run Scenarios

```bash
python main.py --scenario overloaded-restaurant
python main.py --scenario recipient-unavailable
python main.py --scenario traffic
```

---

## 🧪 Example Outputs

### 🍔 Overloaded Restaurant

```
[STEP 1] Check restaurant status.
→ Action: get_merchant_status({'merchant_id': 'M45'})
← Observation: {"merchant_id": "M45", "prep_time_min": 40, "status": "overloaded"}

[FINAL] Resolved by notifying customer and re-routing driver.

=== Final Resolution ===
{"customer": "Notified of delay", "driver": "Re-routed"}
```

### 📦 Recipient Unavailable

```
[FINAL] Recipient unavailable, placed in locker.

=== Final Resolution ===
{"package": "Stored in nearby locker"}
```

### 🚦 Traffic Obstruction

```
[STEP 1] Check traffic conditions on current route.
→ Action: check_traffic({'route_id': 'R1'})
← Observation: {"route_id": "R1", "status": "blocked", "delay_min": 25}

[FINAL] Traffic obstruction resolved with alternative route and passenger update.

=== Final Resolution ===
{"passenger": "Notified of new ETA", "driver": "Given alternative route"}
```

---

## 📖 Scenario Definitions

Stored in `scenarios/scenarios.yaml`:

```yaml
- id: "overloaded-restaurant"
  text: "Order delayed because restaurant is overloaded"
  goal: "Reduce driver wait and inform customer"
  constraints:
    - "Always notify customer"
  world:
    merchant: { id: "M45" }
    order: { id: "A123" }

- id: "recipient-unavailable"
  text: "Recipient not available to collect package"
  goal: "Deliver securely without doorstep drop"
  constraints:
    - "High-value parcel"
  world:
    package: { id: "PX9" }

- id: "traffic"
  text: "Passenger on urgent trip to airport, but traffic accident blocks route."
  goal: "Get passenger to airport on time."
  constraints:
    - "Minimize delay"
    - "Keep passenger informed"
  world:
    driver: { id: "D10" }
    passenger: { id: "P77" }
    route: { blocked: true }
```

---

## 📜 Future Extensions

* Add **Damaged Packaging Dispute** scenario with real-time mediation.
* Integrate **LangGraph** for more robust agent orchestration.
* Add **policy memory** (refund rules, SLA) from vector DB.
* Provide **web-based demo** with Streamlit.

---

## 👨‍💻 Authors

* **Giriraj Parsewar** – GrabHack: Campus Edition Participant

---

## 📄 License

MIT License
