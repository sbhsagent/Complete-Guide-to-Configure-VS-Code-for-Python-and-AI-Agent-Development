import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

# Updated for LangChain 0.3.x compatibility
# Ensure you have installed: pip install langchain-openai==0.3.28


def run_agent():
    load_dotenv()
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Error: OPENAI_API_KEY not found in .env file.")
        return

    # Updated import and initialization for v0.3.x
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)
    question = "What is the main benefit of using a virtual environment in Python?"
    print(f"🤖 Asking AI: '{question}'")

    try:
        # Updated message format for v0.3.x
        messages = [HumanMessage(content=question)]
        response = llm.invoke(messages)
        print(f"✅ AI Response: {response.content}")
    except Exception as e:
        print(f"❌ An error occurred: {e}")


if __name__ == "__main__":
    run_agent()
