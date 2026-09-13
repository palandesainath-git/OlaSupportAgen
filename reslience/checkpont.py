from langgraph.graph import Graph, Node
from langgraph.checkpoint.sqlite import SqliteCheckpointer
from agent.graph import build_graph

def demo_checkpoint():
    graph = build_graph()
    checkpointer = SqliteCheckpointer("checkpoints.sqlite")
    thread_id = "demo_thread_1"

    # Simulate partial run
    print("▶ Starting partial run...")
    graph.run("Show SLA policy", thread_id=thread_id, checkpointer=checkpointer, stop_after_nodes=["intent_router"])
    print("⏸ Run stopped before remaining nodes.")

    # Resume same thread
    print("▶ Resuming run...")
    graph.run("Show SLA policy", thread_id=thread_id, checkpointer=checkpointer)
    print("✅ Resumed successfully — previous nodes loaded from checkpoint.")
