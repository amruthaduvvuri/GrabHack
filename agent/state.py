from dataclasses import dataclass, field
from typing import List, Dict, Any

@dataclass
class ToolEvent:
    step: int
    tool: str
    input: Dict[str, Any]
    observation: Dict[str, Any]
    rationale: str

@dataclass
class AgentState:
    scenario_id: str
    scenario_text: str
    goal: str
    constraints: List[str]
    world: Dict[str, Any]
    history: List[ToolEvent] = field(default_factory=list)
    done: bool = False
    resolution: Dict[str, Any] = field(default_factory=dict)
