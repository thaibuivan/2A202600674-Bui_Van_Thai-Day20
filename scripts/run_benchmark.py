"""Script to run the benchmark and generate the report."""
import os
from multi_agent_research_lab.core.state import ResearchState
from multi_agent_research_lab.core.schemas import ResearchQuery
from multi_agent_research_lab.evaluation.benchmark import run_benchmark
from multi_agent_research_lab.evaluation.report import render_markdown_report

# Setup the runners
def baseline_runner(query: str) -> ResearchState:
    from multi_agent_research_lab.services.llm_client import LLMClient
    request = ResearchQuery(query=query)
    state = ResearchState(request=request)
    llm = LLMClient()
    
    system_prompt = (
        "You are a single-agent research assistant. "
        "The user will provide a research query. You must answer it thoroughly."
    )
    response = llm.complete(system_prompt=system_prompt, user_prompt=query)
    state.final_answer = response.content
    return state

def multi_agent_runner(query: str) -> ResearchState:
    from multi_agent_research_lab.graph.workflow import MultiAgentWorkflow
    workflow = MultiAgentWorkflow()
    state = ResearchState(request=ResearchQuery(query=query))
    return workflow.run(state)

if __name__ == "__main__":
    from multi_agent_research_lab.core.config import get_settings
    from multi_agent_research_lab.observability.logging import configure_logging
    
    settings = get_settings()
    configure_logging(settings.log_level)
    
    query = "Research GraphRAG state-of-the-art and write a 500-word summary"
    
    print("Running baseline benchmark...")
    state_base, metric_base = run_benchmark("Single-Agent Baseline", query, baseline_runner)
    
    print("Running multi-agent benchmark...")
    state_multi, metric_multi = run_benchmark("Multi-Agent Workflow", query, multi_agent_runner)
    
    report_content = render_markdown_report([metric_base, metric_multi])
    
    # Save report
    os.makedirs("reports", exist_ok=True)
    with open("reports/benchmark_report.md", "w", encoding="utf-8") as f:
        f.write(report_content)
        
    print("Benchmark complete! Report saved to reports/benchmark_report.md")
