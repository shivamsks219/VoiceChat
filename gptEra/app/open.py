from urllib import response
import openai

openai.api_key = "OPENAI_KEY"

def ans(prompt):
    response = openai.Completion.create(engine="text-davinci-003", prompt = prompt, max_tokens=200)
    return response["choices"][0]["text"]
