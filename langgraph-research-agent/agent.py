from langgraph.graph import StateGraph, END
from state import ResearchState
from nodes import decompose_node, search_node, synthesize_node

def build_agent():
    graph = StateGraph(ResearchState)

    graph.add_node("decompose", decompose_node)
    graph.add_node("search", search_node)
    graph.add_node("synthesize", synthesize_node)

    graph.set_entry_point("decompose")
    graph.add_edge("decompose", "search")
    graph.add_edge("search", "synthesize")
    graph.add_edge("synthesize", END)

    return graph.compile()