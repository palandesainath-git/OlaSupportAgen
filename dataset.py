import random, json
from collections import Counter

# Seeded deterministic generator
SEED = 99
random.seed(SEED)

CATEGORIES = ["Billing", "Technical Issue", "Account Access", "Product Defect", "General Inquiry"]
STATUSES = ["Open", "In Progress", "Escalated", "Resolved", "Closed"]

def generate_tickets(n=40):
    tickets = []
    for i in range(n):
        category = random.choice(CATEGORIES)
        status = random.choice(STATUSES)
        resolution_time = random.randint(1, 72)  # realistic: 1–72 hours
        days_since_created = random.randint(0, 30)
        escalated = random.random() < 0.2  # ~20% escalated
        tickets.append({
            "record_id": f"TKT{i+1:03d}",
            "category": category,
            "status": status,
            "resolution_time_hours": resolution_time,
            "days_since_created": days_since_created,
            "escalated": escalated
        })
    return tickets

def validate_dataset(tickets):
    cat_count = Counter(t["category"] for t in tickets)
    status_count = Counter(t["status"] for t in tickets)
    escalated_pct = sum(t["escalated"] for t in tickets) / len(tickets) * 100

    print("\n📊 Validation Summary")
    print("Category counts:", dict(cat_count))
    print("Status counts:", dict(status_count))
    print(f"Escalated %: {escalated_pct:.2f}")

    # Validation checks
    assert all(v >= 3 for v in cat_count.values()), "Each category must have ≥3 records"
    assert all(v >= 1 for v in status_count.values()), "Each status must have ≥1 record"
    assert 10 <= escalated_pct <= 30, "Escalated % must be between 10–30"

if __name__ == "__main__":
    dataset = generate_tickets()
    print(json.dumps(dataset[:5], indent=2))
    validate_dataset(dataset)

