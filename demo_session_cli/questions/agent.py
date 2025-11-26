import os
from dotenv import load_dotenv
from google.adk.agents import LlmAgent
from google.adk.tools import google_search

load_dotenv()

# Create the root agent
question_answering_agent = LlmAgent(
    name="question_answering_agent",
    model=os.getenv("GOOGLE_GENAI_MODEL"),
    description="Question answering agent",
    instruction="""
    You are a helpful assistant that answers questions about the user's preferences.

    Here is some information about the user:
    Name: 
    {user_name}
    Preferences: 
    {user_preferences}
    """,
)