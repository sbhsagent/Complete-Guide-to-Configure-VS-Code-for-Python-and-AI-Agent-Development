import os
from dotenv import load_dotenv
from openai import OpenAI

# This code uses the modern OpenAI v1.x+ library
# Ensure you have installed: pip install openai>=1.54.0


def run_direct_agent():
    load_dotenv()
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Error: OPENAI_API_KEY not found in .env file.")
        return

    client = OpenAI()  # API key is read from OPENAI_API_KEY env var by default
    question = "What is the main benefit of using a virtual environment in Python?"
    print(f"🤖 Asking AI: '{question}'")

    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant providing concise answers.",
                },
                {"role": "user", "content": question},
            ],
        )
        response = completion.choices[0].message.content
        print(f"✅ AI Response: {response}")
    except Exception as e:
        print(f"❌ An error occurred: {e}")


if __name__ == "__main__":
    run_direct_agent()
