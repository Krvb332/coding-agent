import os
import argparse
import json
import sys


from dotenv import load_dotenv
from openai import OpenAI
from prompts import system_prompt
from call_function import (available_functions,call_function)


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
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": args.user_prompt},
    ]
    MAX_CALLS = 20

    for _ in range(MAX_CALLS):
        generate_content(client, message,args.verbose)
        if message=="":
            sys.exit("1")
        
def generate_content(client:OpenAI, messages:list,verbosed:bool) -> None:
    response = client.chat.completions.create(
            model="openrouter/free",
            messages=messages,
            tools=available_functions,
            temperature=0,
            
        )
    
    if not response.usage:
        raise RuntimeError("Failed api request")
    elif verbosed:
        print(f"User prompt: {messages[0]["content"]}")
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")
    message = response.choices[0].message
    result_message = {}
    messages_history = []
    messages_history.append(message)
    messages_history.append(result_message)
    if not message.tool_calls:
        print("Response:")
        print(message.content)
        return

    for tool_call in message.tool_calls:
        if tool_call.type != "function":
            continue

        function_args = json.loads(tool_call.function.arguments or "{}")
        result_message = call_function(tool_call)
        print(call_function(tool_call))


    print(f"Response: {response.choices[0].message.content}")
    if verbosed:
        print(f"-> {result_message['content']}")
    return 

if __name__ == "__main__":
    main()