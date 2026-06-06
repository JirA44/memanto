from langgraph.graph import START, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_openai import ChatOpenAI
from langgraph.graph.message import add_messages
from typing import Annotated

class State(TypedDict):
    messages: Annotated[list, add_messages]

def build_graph(tools: list[callable]):
    """
    Builds the LangGraph state graph for the agent.
    """
    llm = ChatOpenAI(
        model=os.environ.get("LLM_MODEL", "openai/gpt-4o-mini"),
        temperature=0,
        api_key=os.environ.get("OPENROUTER_API_KEY"),
        base_url=os.environ.get("OPENAI_API_BASE", "https://openrouter.ai/api/v1"),
    )
    llm_with_tools = llm.bind_tools(tools)

    def chatbot(state: State):
        sys_msg = SystemMessage(
            content=(
                "You are an intelligent personal assistant equipped with a persistent memory. "
                "You have two special tools: memanto_remember and memanto_recall. "
                "1. When the user tells you pers