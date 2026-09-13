import json, statistics
from rag_core.retrieval import retrieve_answer
from rag_core.retrieval import build_collections

# Load KB docs
docs = [
    open("knowledge_base/ticket_priority.md").read(),
    open("knowledge_base/sla_policy.md").read(),
    open("knowledge_base/escalation_matrix.md").read(),
    open("knowledge_base/refund_policy.md").read(),
    open("knowledge_base/communication_channels.md").read(),
    open("knowledge_base/holiday_support.md").read(),
    open("knowledge_base/repeat_complaints.md").read(),
    open("knowledge_base/service_credit.md").read(),
    open("knowledge_base/feedback_collection.md").read(),
    open("knowledge_base/vip_handling.md").read(),
    open("knowledge_base/outage_protocol.md").read(),
    open("knowledge_base/data_retention.md").read(),
]

fixed_coll, sent_coll = build_collections(docs)

# 15 test queries (cover all topics + 2 out-of-scope)
queries = [
    "What defines ticket priority levels?",
    "Explain SLA timelines for critical issues.",
    "How does the escalation matrix work?",
    "What is the refund process for duplicate charges?",
    "Which communication channels are available?",
    "Is support available on holidays?",
    "How are repeat complaints handled?",
    "What are service credits?",
    "How is feedback collected?",
    "How are VIP customers handled?",
    "What happens during an outage?",
    "How long is ticket data retained?",
    "Tell me about driver onboarding policy.",  # out-of-scope
    "Explain Ola ride insurance policy.",        # out-of-scope
    "Describe escalation threshold for old tickets."
]

results = []
for q in queries:
    res = retrieve_answer(q, sent_coll)
    results.append({
        "query": q,
        "context_relevance": round(res["confidence"], 2),
        "groundedness": 1 if res["answer"] != "I don't know." else 0,
        "answer_relevance": round(res["confidence"], 2)
    })

# Compute averages
avg_context = statistics.mean(r["context_relevance"] for r in results)
avg_grounded = statistics.mean(r["groundedness"] for r in results)
avg_answer = statistics.mean(r["answer_relevance"] for r in results)

report = {
    "per_query_scores": results,
    "average_scores": {
        "context_relevance": round(avg_context, 2),
        "groundedness": round(avg_grounded, 2),
        "answer_relevance": round(avg_answer, 2)
    }
}

with open("tests/rag_eval_report.json", "w") as f:
    json.dump(report, f, indent=2)

print(json.dumps(report, indent=2))

