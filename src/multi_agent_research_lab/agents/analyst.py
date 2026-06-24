"""Analyst agent skeleton."""

from multi_agent_research_lab.agents.base import BaseAgent
from multi_agent_research_lab.core.errors import StudentTodoError
from multi_agent_research_lab.core.state import ResearchState


class AnalystAgent(BaseAgent):
    """Turns research notes into structured insights."""

    name = "analyst"

    def run(self, state: ResearchState) -> ResearchState:
        """Populate `state.analysis_notes`."""
        from multi_agent_research_lab.services.llm_client import LLMClient
        llm = LLMClient()
        
        system_prompt = (
            "You are a Senior Analyst. Your task is to analyze the research notes "
            "provided and extract key claims, compare viewpoints, and flag any weak evidence. "
            "Provide structured insights."
        )
        
        user_prompt = (
            f"User Query: {state.request.query}\n\n"
            f"Research Notes:\n{state.research_notes}"
        )
        
        response = llm.complete(system_prompt=system_prompt, user_prompt=user_prompt)
        state.analysis_notes = response.content
        state.add_trace_event("analyst", {"status": "success"})
        
        return state
