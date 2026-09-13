import requests

def call_mcp_tool(record_id):
    url = "http://127.0.0.1:8000/mcp/check_support_ticket_status_tool"
    payload = {"record_id": record_id}
    response = requests.post(url, json=payload)
    print(f"▶ MCP Response for {record_id}:")
    print(response.json())

if __name__ == "__main__":
    call_mcp_tool("TKT001")
    call_mcp_tool("TKT002")
