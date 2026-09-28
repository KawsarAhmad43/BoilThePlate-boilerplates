from typing import Annotated, Sequence, TypedDict
from langchain_core.messages import BaseMessage
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from app.llm.factory import get_llm
from app.core.telemetry import AnalyticsCallback

# tracking conversation state for the graph
class ChatState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]

def chat_node(state: ChatState):
    llm = get_llm()
    analytics = AnalyticsCallback() # for tracking time/tokens
    response = llm.invoke(state["messages"], config={"callbacks": [analytics]})
    return {"messages": [response]}

# setting up the langgraph flow
graph_builder = StateGraph(ChatState)
graph_builder.add_node("chat", chat_node)
graph_builder.add_edge(START, "chat")
graph_builder.add_edge("chat", END)

memory_graph = graph_builder.compile()
