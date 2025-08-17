import argparse, yaml
from agent.state import AgentState
from agent.controller import run_agent
from agent.llm import OpenAIPlanner

def load_scenario(scenarios_path, scenario_id):
    data = yaml.safe_load(open(scenarios_path))
    for s in data:
        if s["id"] == scenario_id:
            return s
    raise ValueError("Scenario not found")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--scenario", required=True)
    args = parser.parse_args()

    s = load_scenario("scenarios/scenarios.yaml", args.scenario)
    state = AgentState(
        scenario_id=s["id"],
        scenario_text=s["text"],
        goal=s["goal"],
        constraints=s.get("constraints", []),
        world=s.get("world", {})
    )

    # ✅ Fixed indentation here (no extra space)
    planner = OpenAIPlanner(model="gpt-4o-mini")
    final_state = run_agent(state, planner)

    print("\n=== Final Resolution ===")
    print(final_state.resolution)
