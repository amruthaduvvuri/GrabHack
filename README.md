# Project Synapse – Agentic Last-Mile Coordinator 🚚🤖

## 📌 Overview

Project Synapse is a proof-of-concept AI agent designed for the Grab Hackathon. It acts as an intelligent coordinator for last-mile delivery disruptions by simulating logistics APIs and reasoning step by step to resolve real-world issues like traffic delays, unavailable recipients, or overloaded merchants.

The agent follows a **Plan → Act → Observe → Reflect** loop, deciding which tools to use, observing results, and generating a final resolution.

* If OpenAI API is available (with quota), the agent uses an **LLM-powered planner**.
* If quota is exceeded or offline, it automatically falls back to a **Rule-based planner**.
* This ensures the system is robust and always demo-ready.

---

## ⚡ Features (Round 1)

* Handles multiple disruption scenarios:

  * 🍔 Overloaded Restaurant (GrabFood/GrabMart)
  * 📦 Recipient Unavailable (GrabExpress)
  * 🚦 Traffic Obstruction (GrabCar)
* Step-by-step reasoning trace printed to console
* Hybrid Planner: OpenAI GPT + Rule-based fallback
* Tool simulation (mock APIs):

  * `get_merchant_status()`
  * `notify_customer()`
  * `re_route_driver()`
  * `check_traffic()`
  * `calculate_alternative_route()`
  * `notify_passenger_and_driver()`
  * `contact_recipient_via_chat()`
  * `find_nearby_locker()`

---

## 🆕 Round 2 Enhancements

For the **Detailed Submission Round**, we extended the system with a **working frontend demo** and API-based backend integration:

* **FastAPI Backend Layer**

  * Added `api.py` exposing endpoints:

    * `POST /simulate/traffic`
    * `POST /simulate/restaurant`
    * `POST /simulate/recipient`
  * Backend wraps the agent logic and returns structured JSON responses with `decision`, `notification`, `steps`, `timestamp`, and `severity`.

* **React + Vite + Tailwind Frontend**

  * Interactive dashboard (single page app) built in `App.tsx`.
  * Features:

    * Sidebar with simulation controls (trigger disruptions).
    * Event log with recent actions.
    * AI decision steps panel with severity levels.
    * Customer Notification & Driver Update panels.
    * Map placeholder for driver route visualization.
  * API integrated: frontend buttons call backend endpoints in real time.

* **Updated Demo Flow**

  * User clicks disruption button in UI.
  * Backend agent processes scenario.
  * UI displays:

    * Real-time steps taken by agent.
    * Final decision + notification.
    * Customer & driver updates.

---

## 🛠️ Tech Stack

* **Backend**: Python 3.10+, FastAPI, Uvicorn, PyYAML, OpenAI API (optional), dotenv
* **Frontend**: React 18, TypeScript, Vite, Tailwind CSS, lucide-react (icons)

---

## 🗂️ Project Structure

```
project-synapse/
│
├── backend/
│   ├── agent/
│   │   ├── controller.py       # agent loop (Plan → Act → Observe)
│   │   ├── llm.py              # OpenAI planner + Rule-based fallback
│   │   ├── state.py            # Agent state + ToolEvent dataclass
│   │   ├── tools.py            # Simulated logistics tools
│   │   └── __init__.py
│   │
│   ├── scenarios/
│   │   └── scenarios.yaml      # Scenario definitions
│   │
│   ├── runner.py               # Wrapper for running scenarios
│   ├── api.py                  # FastAPI server
│   ├── main.py                 # CLI entry point
│   └── requirements.txt        # Python dependencies
│
├── frontend/
│   ├── src/
│   │   ├── App.tsx             # Dashboard UI (single-page app)
│   │   ├── main.tsx            # React root
│   │   ├── index.css           # Tailwind base styles
│   │   └── vite-env.d.ts
│   │
│   ├── index.html
│   ├── package.json
│   ├── tailwind.config.js
│   ├── postcss.config.js
│   └── vite.config.ts
│
├── README.md
└── .gitignore
```

---

## ▶️ How to Run

### 1. Clone Repo

```bash
git clone https://github.com/<your-username>/project-synapse.git
cd project-synapse
```

### 2. Setup Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

Start API:

```bash
uvicorn api:app --reload --port 8000
```

### 3. Setup Frontend

```bash
cd frontend
npm install
npm run dev
```

Open browser → `http://localhost:5173`

---

## 🧪 Example Demo Flow

* User clicks **Simulate Traffic Obstruction** → API returns reroute decision.
* Event log shows step-by-step reasoning.
* Notifications show updated ETA for customer + reroute for driver.
* Map panel highlights disruption (static placeholder for now).

---

## 📖 Scenario Definitions

(unchanged from Round 1, stored in `scenarios/scenarios.yaml`)

---

## 📜 Future Extensions

* Add Damaged Packaging Dispute scenario with real-time mediation.
* Integrate LangGraph for more robust agent orchestration.
* Add policy memory (refund rules, SLA) from vector DB.
* Expand map into live visualization with Leaflet.js or Google Maps API.
* Deploy backend on cloud (e.g., Render/Heroku) for live demo links.

---

## 👨‍💻 Authors

Giriraj Parsewar – GrabHack: Campus Edition Participant

---

## 📄 License

MIT License
