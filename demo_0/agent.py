import datetime

from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm


def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city.
    Args:
        city (str): The name of the city.
    Returns:
        dict: A dictionary containing the status and current time.
    """
    time = datetime.datetime.now().strftime("%H:%M %p")
    return {"status": "success", "city": city, "time": time}


root_agent = LlmAgent(
    # model=LiteLlm(model="ollama_chat/deepseek-r1:7b"),
    model="gemini-2.5-flash-lite",
    name="root_agent",
    description="Tells the current time in a specified city.",
    instruction="""You are a helpful assistant that tells the current time in cities.
        Use the 'get_current_time' tool for this purpose. And show the time to the user""",
    tools=[get_current_time],
)
