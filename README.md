# GPT Terminal Chatbot

This is a simple command-line tool that uses OpenAI's [chat completion API](https://platform.openai.com/docs/guides/chat) to generate responses to user input. The tool is designed to be used in the terminal and can be easily customized to fit your needs.

## Installation

1. Clone this repository:
2. Install the required Python packages:

    - `pip install openai`
    - `pip install python-dotenv`

3. Set up your OpenAI API key:

    - Go to [platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)
    - Follow the instructions to get an API key
    - Copy the API key to your clipboard

4. Create a `.env` file in the project directory:

5. Add the following line to the `.env` file, replacing `YOUR_API_KEY` with your actual API key:

    - `OPENAI_API_KEY="YOUR_API_KEY"`

## Usage

1. Start the tool by running the script: `python ask_gpt.py`.

    - Alternatively, you can run the script via an alias: `alias ask_gpt="python ask_gpt.py"`
    - If you are using Windows, you may need to run the script using `python3` instead of `python`.

2. Enter your question or message in the terminal prompt.

3. The gpt will generate a response based on your input and display it in the terminal.

4. You can continue to enter questions or messages until you are finished.

5. To exit the tool, type `quit` in the terminal prompt.

## Configuration

You can customize the behavior of the chatbot by modifying the `ask_gpt()` function in the `ask_gpt.py` script.

-   `model`: The GPT-3.5 model to use. You can find a list of available models on the [OpenAI website](https://platform.openai.com/docs/models/gpt-3-5).
-   `temperature`: The temperature parameter controls the randomness of the generated response. Lower values will result in more predictable responses, while higher values will result in more creative and unpredictable responses.
-   `max_tokens`: The maximum number of tokens (words or phrases) to generate in the response.
-   `messages`: The messages parameter is a list of dictionaries that represent the conversation between the user and the chatbot. You can add or remove messages to control the context and flow of the conversation.
-   List of request parameters: https://platform.openai.com/docs/api-reference/chat/create

## Acknowledgments

-   The [OpenAI](https://openai.com/) team for developing the GPT API.
-   The [python-dotenv](https://pypi.org/project/python-dotenv/) package for simplifying the management of environment variables.
