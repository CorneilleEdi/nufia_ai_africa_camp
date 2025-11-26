from google.adk.agents import LlmAgent
from google.adk.tools import FunctionTool, ToolContext



def do_calculation(expression: str, tool_context:ToolContext) -> str:
    """Evaluates a mathematical expression and returns the result as a string.
        Args:
            expression (str): The mathematical expression to evaluate.
        Returns:
            str: The result of the evaluation.
        Example:
            >>> do_calculation("2 + 2 * 3")
            '8'
    """
    try:
        # Safely evaluate the expression
        result = eval(expression, {"__builtins__": None}, {})
        tool_context.state[expression] = result
        return str(result)
    
    except Exception as e:
        return f"Error evaluating expression: {e}"

root_agent = LlmAgent(
    model="gemini-2.5-flash-lite",
    name='root_agent',
    instruction="""You are a helpful assistant that can perform mathematical calculations.
    When given a mathematical expression, use the 'do_calculation' tool to evaluate it and provide the result.
    """,
    description="Performs mathematical calculations",
    tools=[FunctionTool(do_calculation)],     
)

# 2 + 2 * 3