from google.adk.models.lite_llm import LiteLlm
from google.adk.agents import LlmAgent
import datetime
from google.adk.code_executors import BuiltInCodeExecutor
from google.adk.tools import google_search
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters


root_agent = LlmAgent(
    model="gemini-2.5-flash-lite",
    name='root_agent',
    instruction="""You are a helpful assistant that provides information from a Redis MCP server.
    When asked about data stored in the Redis server, use the tools provided to fetch and return the information.
    """,
    description="Fetches information from a Redis MCP server",
   tools=[
        McpToolset(
            connection_params=StdioConnectionParams(
                timeout_seconds=30.0,
                server_params = StdioServerParameters(
                    command='uvx',
                           args= [
                            "--from",
                        "redis-mcp-server@latest",
                        "redis-mcp-server",
                        "--port",
                        "6379",
                        "--password",
                        "ljhfaasdb",
                        "--host",
                        "192.168.56.4"
                           ]                    
                ),
            ),
        )
    ],  
)
