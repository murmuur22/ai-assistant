function_descriptions = [
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
            },
            "required" : ["scene_text", "choices"]
        }
    },
    {
        "name": "create_enemy",
        "description": "Creates an enemy for a turn based combat system.",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "A creative name for the enemy."
                },
                "difficulty": {
                    "type": "string",
                    "enum" : ["1", "2", "3", "4", "5"],
                    "description": "Determines the difficulty. Higher numbers mean a more difficult enemy."
                },
                "abilities": {
                    "type": "object",
                    "properties" : {
                        "ability1" : {
                            "type" : "object",
                            "properties" : {
                                "ability_name" : {
                                    "type" : "string",
                                    "description" : "The name of the ability"
                                },
                                "effect" : {
                                    "type" : "string",
                                    "enum" : ["damage", "stun", "buff_strength", "buff_defense", "damage_over_time"],
                                    "description" : "What the ability should do."
                                },
                                "power" : {
                                    "type" : "string",
                                    "enum" : ["1", "2", "3", "4", "5"],
                                    "description" : "The power level of the ability. Higher numbers mean the ability's effect is more powerful."
                                }
                            }
                        }
                    }
                }
            },
            "required" : ["name", "difficulty", "abilities"]
        }
    }
]
