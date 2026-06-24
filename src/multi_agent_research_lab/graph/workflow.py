"""LangGraph workflow skeleton."""

from multi_agent_research_lab.core.errors import StudentTodoError
from multi_agent_research_lab.core.state import ResearchState


class MultiAgentWorkflow:
    """Builds and runs the multi-agent graph.

    Keep orchestration here; keep agent internals in `agents/`.
    """

    def build(self) -> object:
        """Create a LangGraph graph."""
        from langgraph.graph import StateGraph, START, END
        from multi_agent_research_lab.agents.supervisor import SupervisorAgent
        from multi_agent_research_lab.agents.researcher import ResearcherAgent
        from multi_agent_research_lab.agents.analyst import AnalystAgent
        from multi_agent_research_lab.agents.writer import WriterAgent

        workflow = StateGraph(ResearchState)
        
        # Add nodes
        workflow.add_node("supervisor", SupervisorAgent().run)
        workflow.add_node("researcher", ResearcherAgent().run)
        workflow.add_node("analyst", AnalystAgent().run)
        workflow.add_node("writer", WriterAgent().run)
        
        # Add edges
        workflow.add_edge(START, "supervisor")
        workflow.add_edge("researcher", "supervisor")
        workflow.add_edge("analyst", "supervisor")
        workflow.add_edge("writer", "supervisor")
        
        # Conditional routing from supervisor
        def router(state: ResearchState) -> str:
            if state.route_history:
                last_route = state.route_history[-1]
                if last_route == "done":
                    return END
                return last_route
            return END
            
        workflow.add_conditional_edges("supervisor", router)
        
        return workflow.compile()

    def run(self, state: ResearchState) -> ResearchState:
        """Execute the graph and return final state."""
        app = self.build()
        final_state_dict = app.invoke(state.model_dump())
        return ResearchState(**final_state_dict)
