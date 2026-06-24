"""LLM client abstraction.

Production note: agents should depend on this interface instead of importing an SDK directly.
"""

import os
from dataclasses import dataclass
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage

from multi_agent_research_lab.core.errors import StudentTodoError

@dataclass(frozen=True)
class LLMResponse:
    content: str
    input_tokens: int | None = None
    output_tokens: int | None = None
    cost_usd: float | None = None

class LLMClient:
    """Provider-agnostic LLM client skeleton."""
    
    def __init__(self):
        from dotenv import load_dotenv
        load_dotenv()
        # Mặc định sử dụng model của Groq
        model_name = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")
        api_key = os.getenv("GROQ_API_KEY")
        self.llm = ChatGroq(model=model_name, api_key=api_key)

    def complete(self, system_prompt: str, user_prompt: str) -> LLMResponse:
        """Return a model completion."""
        
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_prompt)
        ]
        
        response = self.llm.invoke(messages)
        
        usage = response.response_metadata.get("token_usage", {})
        
        return LLMResponse(
            content=str(response.content),
            input_tokens=usage.get("prompt_tokens"),
            output_tokens=usage.get("completion_tokens"),
            cost_usd=0.0
        )
