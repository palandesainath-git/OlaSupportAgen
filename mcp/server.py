from fastmcp import FastMCP
from agent.tools import check_support_ticket_status

app = FastMCP()

@app.tool()
def check_support_ticket_status_tool(record_id: str):
    """
    Retrieve support ticket status and escalation score.
    Args:
        record_id (str): Ticket ID (e.g., TKT001)
    Returns:
        dict: status, resolution_time_hours, escalation_score
    """
    return check_support_ticket_status(record_id)

if __name__ == "__main__":
    # Launch MCP server locally
    app.run(host="127.0.0.1", port=8000)

