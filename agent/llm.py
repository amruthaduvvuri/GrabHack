import os, json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class OpenAIPlanner:
    def __init__(self, model="gpt-4o-mini"):
        self.model = model

    def plan(self, state):
        tools_doc = "\n".join(state.get("tools", []))
        history_text = "\n".join(
    [f"Step {h.step}: used {h.tool} → {h.observation}" for h in state["history"]]
)


        prompt = f"""
You are a logistics coordinator agent.
Scenario: {state['scenario_text']}
Goal: {state['goal']}
Constraints: {state['constraints']}
Available Tools: {tools_doc}

History so far:
{history_text}

Respond in JSON ONLY:
{{
  "rationale": "...",
  "action": {{"tool": "tool_name", "input": {{...}}}},
  "final": false
}}
OR
{{
  "rationale": "...",
  "resolution": {{...}},
  "final": true
}}
"""

        try:
            response = client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are an AI planning agent."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.2,
            )
            raw_output = response.choices[0].message.content.strip()
            return json.loads(raw_output)

        except Exception as e:
            print(f"[WARNING] OpenAI failed → falling back to RulePlanner. Error: {e}")
            return RulePlanner().plan(state)


# ---- Simple fallback planner ----
class RulePlanner:
    def plan(self, state):
        text = state["scenario_text"].lower()

        # Restaurant case
        if "restaurant" in text:
            if not state["history"]:
                return {
                    "rationale": "Check restaurant status.",
                    "action": {"tool": "get_merchant_status", "input": {"merchant_id": "M45"}},
                    "final": False
                }
            else:
                return {
                    "final": True,
                    "resolution": {"customer": "Notified of delay", "driver": "Re-routed"},
                    "rationale": "Resolved by notifying customer and re-routing driver."
                }

        # Recipient unavailable case
        elif "recipient" in text:
            return {
                "final": True,
                "resolution": {"package": "Stored in nearby locker"},
                "rationale": "Recipient unavailable, placed in locker."
            }

        # 🚦 Traffic obstruction case
        elif "traffic" in text or "accident" in text:
            if not state["history"]:
                return {
                    "rationale": "Check traffic conditions on current route.",
                    "action": {"tool": "check_traffic", "input": {"route_id": "R1"}},
                    "final": False
                }
            else:
                return {
                    "final": True,
                    "resolution": {
                        "passenger": "Notified of new ETA",
                        "driver": "Given alternative route"
                    },
                    "rationale": "Traffic obstruction resolved with alternative route and passenger update."
                }

        # Default fallback
        return {
            "final": True,
            "resolution": {"status": "No plan"},
            "rationale": "Fallback generic resolution."
        }
