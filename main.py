import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse

def main() -> None:
    load_dotenv()
    api_key=os.environ.get("OPENROUTER_API_KEY")

    if api_key == None:
        raise RuntimeError("Api key not found")

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args= parser.parse_args()


    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )
    message = [
        {"role": "user", "content": args.user_prompt},
    ]
    
    generate_content(client, message,args.verbose)

def generate_content(client:OpenAI, messages:list,verbosed:bool) -> None:
    response = client.chat.completions.create(
            model="openrouter/free",
            messages=messages,
        )
    
    if not response.usage:
        raise RuntimeError("Failed api request")
    elif verbosed:
        print(f"User prompt: {messages[0]["content"]}")
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")


    print(f"Response: {response.choices[0].message.content}")


if __name__ == "__main__":
    main()