"""Supervisor / router skeleton."""

from multi_agent_research_lab.agents.base import BaseAgent
from multi_agent_research_lab.core.errors import StudentTodoError
from multi_agent_research_lab.core.state import ResearchState


class SupervisorAgent(BaseAgent):
    """Decides which worker should run next and when to stop."""

    name = "supervisor"

    def run(self, state: ResearchState) -> ResearchState:
        """Update `state.route_history` with the next route."""
        
        # Simple state machine routing logic
        if not state.research_notes:
            next_agent = "researcher"
        elif not state.analysis_notes:
            next_agent = "analyst"
        elif not state.final_answer:
            next_agent = "writer"
        else:
            next_agent = "done"

        # Prevent infinite loops
        if state.iteration >= 5:
            next_agent = "done"

        state.record_route(next_agent)
        return state
