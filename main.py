# --------------------------------------------------------
# Import Modules
# --------------------------------------------------------

import os
import json
import openai
from libs.descriptions import function_descriptions

# --------------------------------------------------------
# Load Open AI API Key
# --------------------------------------------------------

openai.api_key = os.getenv("OPENAI_API_KEY")

# --------------------------------------------------------
# Setup
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
    functions = function_descriptions,
    function_call = {"name": "create_encounter"},
    temperature = 0.2
)
reply = completion.choices[0].message.function_call.arguments
reply = json.loads(reply)

scene_text = reply["scene_text"]

# --------------------------------------------------------
# Main Game Loop
# --------------------------------------------------------

while(True):

    print(scene_text)
    messages.append({"role": "assistant", "content": scene_text})

    for i in range(len(reply["choices"])):
        choice = reply["choices"]["choice"+str(i+1)]
        print(str(i+1)+'.', choice["choice_text"], '['+choice["choice_type"]+']')

    player_choice = input('> ')

    choice_text = reply["choices"]["choice"+player_choice]["choice_text"]
    choice_type = reply["choices"]["choice"+player_choice]["choice_type"]

    messages.append({"role": "user", "content": choice_text})

    if choice_type == 'combat':
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            max_tokens=800,
            messages=messages,
            functions = function_descriptions,
            function_call = {"name": "create_enemy"},
            temperature = 0.2
        )
        reply = completion.choices[0].message.function_call.arguments
        reply = json.loads(reply)

        print("fighting > ")
        print('name >', reply['name'])
        print('diffuclty >', reply['difficulty'])
        print('abilities >', reply['abilities'])

        break
    else:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            max_tokens=800,
            messages=messages,
            functions = function_descriptions,
            function_call = {"name": "create_encounter"},
            temperature = 0.2
        )

    reply = completion.choices[0].message.function_call.arguments
    reply = json.loads(reply)
    scene_text = reply["scene_text"]
