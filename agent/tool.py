from dataset import generate_tickets

DATASET = generate_tickets()

def check_support_ticket_status(record_id: str) -> dict:
    """Lookup ticket and compute escalation score."""
    record = next((r for r in DATASET if r["record_id"] == record_id), None)
    if not record:
        return {"error": "Ticket not found"}

    days = record["days_since_created"]
    escalated = record["escalated"]

    recency = days / 30
    score = 0.6 * recency + 0.4 * (1 if escalated else 0)
    escalation_score = round(score, 2)

    return {
        "record_id": record_id,
        "status": record["status"],
        "resolution_time_hours": record["resolution_time_hours"],
        "escalation_score": escalation_score
    }
