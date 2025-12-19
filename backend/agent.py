from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from tools import get_weather
from config import OPENROUTER_API_KEY
from langchain_core.messages import SystemMessage, HumanMessage


SYSTEM_PROMPT = """
You are an AI weather assistant.

STRICT RULES:
- Do NOT use markdown.
- Do NOT use **, ###, bullets, or emojis.
- Use plain text only.
- Use short lines with labels.

ALWAYS respond in this format:

City: <city name>
Temperature: <value in °C>
Wind Speed: <value in km/h>
Conditions: <short description>
Advice: <1 short sentence>
Forecast: <optional, 1 line>
"""


# LLM via OpenRouter
llm = ChatOpenAI(
    model="mistralai/devstral-2512:free",
    openai_api_key=OPENROUTER_API_KEY,
    openai_api_base="https://openrouter.ai/api/v1",
    temperature=0
)

# Bind tool to LLM (THIS IS KEY)
llm_with_tools = llm.bind_tools([get_weather])

def ask_agent(query: str) -> str:
    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=query)
    ]

    response = llm_with_tools.invoke(messages)

    # If LLM decides to call the weather tool
    if response.tool_calls:
        tool_call = response.tool_calls[0]
        tool_result = get_weather.invoke(tool_call["args"])

        final_response = llm.invoke([
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(content=query),
            tool_result
        ])

        return final_response.content

    # If no tool was needed
    return response.content

