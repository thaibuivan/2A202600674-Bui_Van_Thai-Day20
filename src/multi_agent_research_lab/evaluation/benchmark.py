"""Benchmark skeleton for single-agent vs multi-agent."""

from time import perf_counter
from typing import Callable

from multi_agent_research_lab.core.schemas import BenchmarkMetrics
from multi_agent_research_lab.core.state import ResearchState


Runner = Callable[[str], ResearchState]


def run_benchmark(run_name: str, query: str, runner: Runner) -> tuple[ResearchState, BenchmarkMetrics]:
    """Measure latency and return a metric object."""
    started = perf_counter()
    state = runner(query)
    latency = perf_counter() - started
    
    # Calculate simple quality surrogate: length of final answer mapped to 1-10
    word_count = len(state.final_answer.split()) if state.final_answer else 0
    quality = min(float(word_count) / 50.0, 10.0)
    # Simulate cost since Groq free tier is $0
    cost = 0.0
    
    metrics = BenchmarkMetrics(
        run_name=run_name, 
        latency_seconds=latency,
        estimated_cost_usd=cost,
        quality_score=float(quality)
    )
    return state, metrics
