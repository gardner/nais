from typing import Optional

from app.index import get_index
from llama_index.core.agent.workflow import AgentWorkflow
from llama_index.core.settings import Settings
from langchain_google_genai import ChatGoogleGenerativeAI
from llama_index.llms.langchain import LangChainLLM
from llama_index.server.api.models import ChatRequest
from llama_index.server.tools.index import get_query_engine_tool


def create_workflow(chat_request: Optional[ChatRequest] = None) -> AgentWorkflow:
    index = get_index(chat_request=chat_request)
    if index is None:
        raise RuntimeError(
            "Index not found! Please run `uv run generate` to index the data first."
        )
    query_tool = get_query_engine_tool(index=index)
    return AgentWorkflow.from_tools_or_functions(
        tools_or_functions=[query_tool],
        llm=Settings.llm or LangChainLLM(ChatGoogleGenerativeAI(model="gemini-2.0-flash")),
        system_prompt="You are a helpful assistant.",
    )
