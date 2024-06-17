import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate, HumanMessagePromptTemplate

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")


def ask_chat(model_name, template, input_text, variables):
    question = input(input_text)
    variables['person'] = question  # Assuming 'person' is always one of the variables
    llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model_name=model_name, temperature=0.7)
    message = HumanMessagePromptTemplate.from_template(template=template)
    prompt = ChatPromptTemplate.from_messages(messages=[message])

    # Formatting the prompt with the given variables
    prompt_with_values = prompt.format_prompt(**variables)

    # Ensure the prompt_with_values is converted correctly to a list of messages
    messages = prompt_with_values.to_messages()

    # Pass the list of messages to the llm object
    answer = llm.generate(messages)

    print(answer)


# Example usage
model_name = "gpt-4"
template = "Provide information about {person}. Mention their {occupation} and {achievements}."
input_text = "Ask about the person"
variables = {
    "occupation": "scientific contributions",
    "achievements": "Nobel Prize"
}

ask_chat(model_name, template, input_text, variables)
