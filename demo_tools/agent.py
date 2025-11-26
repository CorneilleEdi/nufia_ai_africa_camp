from google.adk.models.lite_llm import LiteLlm
from google.adk.agents import LlmAgent
import datetime
from google.adk.code_executors import BuiltInCodeExecutor
from google.adk.tools import google_search
import requests

def get_current_weather(city: str) -> dict:
    """Returns the current weather in a specified city.
        Args:
            city (str): The name of the city. Supported cities: Lille, New York, Tokyo, Paris, Lome.
        Returns:
            dict: A dictionary containing the status and current weather.
    """
    cities_coordinates = {
        "Lille": (50.6292, 3.0573),
        "New York": (40.7128, -74.0060),
        "Tokyo": (35.6895, 139.6917),
        "Paris": (48.8566, 2.3522),
        "Lome": (6.1725, 1.2314),
    }
    if city not in cities_coordinates:
        return {"status": "error", "message": f"City '{city}' not found."}
    lat, lon = cities_coordinates[city]
    
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    response = requests.get(url)
    if response.status_code != 200:
        return {"status": "error", "message": "Failed to fetch weather data."}
    data = response.json()
    current_weather = data.get("current_weather", {})
    temperature = current_weather.get("temperature")
    windspeed = current_weather.get("windspeed")
    return {"status": "success", "city": city, "temperature": temperature, "windspeed": windspeed}




root_agent = LlmAgent(
    model="gemini-2.5-flash-lite",
    name='root_agent',
    code_executor=BuiltInCodeExecutor(),
    instruction="""You are a calculator & research agent.
    When given a mathematical expression, write and execute Python code to calculate the result.
    Return only the final numerical result as plain text, without markdown or code blocks.
    When given a research question, use the 'google_search' tool to find relevant information.
    """,
    description="Executes Python code to perform calculations or do research using Google Search",
    tools=[google_search],
)

# root_agent = LlmAgent(
#     model="gemini-2.5-flash-lite",
#     name='root_agent',
#     instruction="""You are a helpful assistant that provides the current weather in cities.
#     When asked about the weather in a city, use the 'get_current_weather' tool to provide the information.
#     """,
#     description="Give the current weather in a city",
#     tools=[get_current_weather],     
# )


# Calculation
# Calculate the value of (5 + 7) * 3
# What is 10 factorial?


# Research 
# Can you search what is loopbin.dev for me ?

# Weather
# I want the weather in lille