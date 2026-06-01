from ollama import chat

print("AI Agent Started! Type 'exit' to quit.\n")


def calculator(expression):
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error: {e}"


def read_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"Error: {e}"


while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    # Calculator Tool
    if user_input.startswith("calc "):
        expression = user_input[5:]

        print("\n[Using Calculator Tool]")
        print("\nAgent:")
        print(calculator(expression))
        print()

        continue

    # File Reader Tool
    if user_input.startswith("read "):
        print("DEBUG: FILE TOOL TRIGGERED")

        filename = user_input[5:]

        print("\n[Using File Reader Tool]")
        print("\nAgent:")
        print(read_file(filename))
        print()

        continue

    # Default: Ask Qwen3
    response = chat(
        model="qwen3",
        messages=[
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    print("\nAgent:")
    print(response.message.content)
    print()