"""Writer agent skeleton."""

from multi_agent_research_lab.agents.base import BaseAgent
from multi_agent_research_lab.core.errors import StudentTodoError
from multi_agent_research_lab.core.state import ResearchState


class WriterAgent(BaseAgent):
    """Produces final answer from research and analysis notes."""

    name = "writer"

    def run(self, state: ResearchState) -> ResearchState:
        """Populate `state.final_answer`."""
        from multi_agent_research_lab.services.llm_client import LLMClient
        llm = LLMClient()
        
        system_prompt = (
            "You are an Expert Writer. Your task is to produce a final answer to the user's query "
            "based on the research notes and analysis notes. Synthesize a clear response with citations."
        )
        
        user_prompt = (
            f"User Query: {state.request.query}\n\n"
            f"Research Notes:\n{state.research_notes}\n\n"
            f"Analysis Notes:\n{state.analysis_notes}"
        )
        
        response = llm.complete(system_prompt=system_prompt, user_prompt=user_prompt)
        state.final_answer = response.content
        state.add_trace_event("writer", {"status": "success"})
        
        return state
