import ollama


def run_local_agent():
    question = "What is the main benefit of using a virtual environment in Python?"
    model_name = "llama3.1"
    print(f"🤖 Asking local AI ({model_name}): '{question}'")

    try:
        response = ollama.chat(
            model=model_name, messages=[{"role": "user", "content": question}]
        )
        print(f"✅ AI Response: {response['message']['content']}")
    except Exception as e:
        print(f"❌ An error occurred. Is the Ollama app running? {e}")


if __name__ == "__main__":
    run_local_agent()
