from agent.tools import TOOL_REGISTRY
from agent.state import ToolEvent

def run_agent(state, planner):
    step = 1
    while not state.done and step <= 5:
        decision = planner.plan(state.__dict__)

        if decision.get("final"):
            state.done = True
            state.resolution = decision["resolution"]
            print(f"[FINAL] {decision['rationale']}")
            break

        tool_name = decision["action"]["tool"]
        tool_input = decision["action"]["input"]
        rationale = decision.get("rationale", "")

        if tool_name in TOOL_REGISTRY:
            obs = TOOL_REGISTRY[tool_name](**tool_input)
        else:
            obs = {"error": f"Unknown tool {tool_name}"}

        print(f"[STEP {step}] {rationale}")
        print(f"→ Action: {tool_name}({tool_input})")
        print(f"← Observation: {obs}\n")

        state.history.append(ToolEvent(step, tool_name, tool_input, obs, rationale))
        step += 1

    return state
