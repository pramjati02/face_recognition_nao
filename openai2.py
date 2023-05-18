
import os
import openai
openai.api_key = "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"

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Tell the world about the ChatGPT API in the style of a pirate."}
  ]
)

print(completion.choices[0].message.content)
