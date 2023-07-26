# --------------------------------------------------------
# Import Modules
# --------------------------------------------------------

import os
import json
import openai
from libs.descriptions import function_description

# --------------------------------------------------------
# Load Open AI API Key
# --------------------------------------------------------

openai.api_key = os.getenv("OPENAI_API_KEY")

# --------------------------------------------------------
# Run
# --------------------------------------------------------


describe = input("Describe the world? ")
charachter = input("Describe yourself? ")
print(" ")
print(" ")
print(" ")

messages=[
    {"role": "system", "content": "You are a the game controller of a text based adventure game. Never refer to yourself. Tell the story in second person from the perspective of the player."},
    {"role": "system", "content": "The world is "+describe},
    {"role": "system", "content": "The user is playing as "+charachter},
    {"role": "system", "content": "Start the adventure and ask the player what they want to do next!"}
  ]
completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    max_tokens=500,
    messages=messages,
    functions = function_description,
    function_call = {"name": "create_encounter"},
    temperature = 0.2
)
messages.append(completion.choices[0].message)

print(completion)

print(completion.choices[0].message)
print(" ")
print(" ")
print(" ")
