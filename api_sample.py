import os
import openai

openai.api_key = os.environ.get("OPENAI_KEY")

response = openai.Completion.create(
  model="code-davinci-002",
  prompt='''
  Script python para ler uma string e retornar o valor inverso.
  ''',
  temperature=0,
  max_tokens=64,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

print(response)