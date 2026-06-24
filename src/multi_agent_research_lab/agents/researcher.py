"""Researcher agent skeleton."""

from multi_agent_research_lab.agents.base import BaseAgent
from multi_agent_research_lab.core.errors import StudentTodoError
from multi_agent_research_lab.core.state import ResearchState


class ResearcherAgent(BaseAgent):
    """Collects sources and creates concise research notes."""

    name = "researcher"

    def run(self, state: ResearchState) -> ResearchState:
        """Populate `state.sources` and `state.research_notes`."""
        from multi_agent_research_lab.services.search_client import SearchClient
        
        search_client = SearchClient()
        # Perform mock search
        docs = search_client.search(state.request.query)
        state.sources.extend(docs)
        
        # Combine snippets into research notes
        notes = "Found the following research documents:\n\n"
        for i, doc in enumerate(docs, start=1):
            notes += f"[{i}] {doc.title} ({doc.url})\nSnippet: {doc.snippet}\n\n"
            
        state.research_notes = notes.strip()
        state.add_trace_event("researcher", {"status": "success", "docs_found": len(docs)})
        
        return state
