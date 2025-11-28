from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters

root_agent = LlmAgent(
    model="gemini-2.5-flash-lite",
    name="root_agent",
    instruction="""
    You are a helpful assistant that provides information from a SQLite database using MCP (Multi-Connection Protocol).
    """,
    tools=[
        McpToolset(
            connection_params=StdioConnectionParams(
                timeout_seconds=30.0,
                server_params=StdioServerParameters(
                    command="uvx",
                    args=[
                        "--directory",
                        "/Users/corneilleedi/Lab/work/loopbin/tdev_ai_day/demo_mcp",
                        "mcp-server-sqlite",
                        "--db-path",
                        "./chinook.db",
                    ],
                ),
            ),
        )
    ],
)
