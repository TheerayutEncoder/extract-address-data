# Import library
import openai
import os
from dotenv import load_dotenv

load_dotenv()

# Accessing the OPENAI KEY
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to create response from OpenAI model
def get_completion(prompt):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0,
    max_tokens=300,
    )

    return response["choices"][0]["text"]


if __name__ == "__main__":
    # Test
    prompt = """
            I will provide you a name of animal delimited by tripple backtick. 
        Your task is describe it in 3 sentences.
        Return following this format:

        Name: ```{animal}```
        Description:
         - Your description number 1
         - Your description number 2
         - Your description number 3
        """

    prompt=prompt.format(animal="Cat")
    print(prompt)