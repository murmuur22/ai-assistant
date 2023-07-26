function_description = [
    {
        "name": "create_encounter",
        "description": "Creates the next scene of the game. Uses the arguments provided to determine what the scene should look like.",
        "parameters": {
            "type": "object",
            "properties": {
                "scene_text": {
                    "type": "string",
                    "description": "The text describing what is happening in the scene."
                },
                "choices": {
                    "type": "object",
                    "properties": {
                        "choice1": {
                            "type": "object",
                            "properties" : {
                                "choice_text" : {
                                    "type" : "string",
                                    "description": "A choice for the player to make in the scenario"
                                },
                                "choice_type" : {
                                    "type" : "string",
                                    "enum" : ["dialogue", "combat", "trap", "item", "action"],
                                    "description" : "Choose which kind of encounter this choice will trigger."
                                }
                            }
                        }
                    }
                }
            }
        }
    }
]
