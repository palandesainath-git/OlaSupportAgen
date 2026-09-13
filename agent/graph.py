from langgraph.graph import Graph, Node
from tools import check_support_ticket_status
from rag_core.retrieval import retrieve_answer
from memory import MemoryManager
from guardrails import apply_guardrails
import json, jsonschema

memory = MemoryManager()

with open("agent/schema.json") as f:
    SCHEMA = jsonschema.Draft7Validator(json.load(f))

def route_query(query: str):
    if "ticket" in query.lower() or "status" in query.lower():
        return "ticket_status"
    return "rag"

def build_graph():
    g = Graph()
    g.add_node(Node("guardrails", apply_guardrails))
    g.add_node(Node("intent_router", route_query))
    g.add_node(Node("rag_tool", retrieve_answer))
    g.add_node(Node("ticket_tool", check_support_ticket_status))

    g.add_edge("guardrails", "intent_router")
    g.add_conditional_edge("intent_router", "rag_tool", "rag")
    g.add_conditional_edge("intent_router", "ticket_tool", "ticket_status")

    return g

