"""Search client abstraction for ResearcherAgent."""

from multi_agent_research_lab.core.schemas import SourceDocument


class SearchClient:
    """Mock search client returning dummy data."""

    def search(self, query: str) -> list[SourceDocument]:
        """Return mock search results to fulfill the requirement without external API keys."""
        
        # Trả về các document giả định để Agent có dữ liệu phân tích
        return [
            SourceDocument(
                url="https://mock-domain.com/article1",
                title="Introduction to GraphRAG",
                snippet=f"GraphRAG is a state-of-the-art technique combining graph databases with LLMs. Found results for query: {query}"
            ),
            SourceDocument(
                url="https://mock-domain.com/article2",
                title="Multi-Agent Systems vs Single-Agent",
                snippet="Multi-agent systems offer better separation of concerns, higher quality analysis, and robustness compared to single-agent baselines."
            )
        ]
