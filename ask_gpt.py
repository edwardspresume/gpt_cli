import os
from typing import Optional

import openai
from dotenv import load_dotenv


def load_api_key() -> Optional[str]:
    """
    Load the API key from the environment variable using python-dotenv.
    Returns the API key as a string, or None if not found.
    """
    load_dotenv()
    return os.environ.get("OPENAI_API_KEY")


def configure_openai(api_key: str) -> None:
    """
    Set the API key for the openai library.
    """
    openai.api_key = api_key


def ask_gpt(input_text: str) -> str:
    """
    Send a request to the OpenAI GPT-3.5 Turbo model with the given input text.
    Returns the generated response as a string.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            temperature=0.2,
            max_tokens=300,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": input_text},
            ],
        )
        return response.choices[0].message.content.strip()
    except openai.OpenAIError as error:
        print(f"Error: {error}")
        return "An error occurred while processing your request."


def print_yellow_text(text: str) -> None:
    """
    Print the given text in yellow color.
    """
    YELLOW = "\033[93m"
    RESET = "\033[0m"
    print(YELLOW + text + RESET)


def main() -> None:
    """
    Main function that runs the question-answering loop.
    """
    api_key = load_api_key()

    if not api_key:
        print("Error: API key not found. Check your .env file or environment variables.")
        return

    configure_openai(api_key)

    while True:
        input_text = input("Enter your question (or type 'quit' to exit): ")

        if input_text.lower() == "quit":
            break

        response_text = ask_gpt(input_text)
        print_yellow_text(f"\nResponse: {response_text}\n")


if __name__ == "__main__":
    main()
