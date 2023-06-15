import random

START_GAME = "Are you ready to start the game and embark on an exciting journey? Please confirm by saying 'Yes' and let the adventure begin!"
INFO_FOREST = "Ah, the forest holds countless mysteries waiting to be unraveled."
BECOME_ADVENT = "Becoming an adventurer is no small feat, but fear not! Seek out the wise sages, train under skilled mentors, and prove your mettle in daring quests.\nOnly then will you earn the title of a true adventurer."
ENEMY_INFO = "From fearsome beasts to cunning bandits, you will encounter a variety of challenges. Be prepared to battle creatures of myth and legends!"
UNLOCK_FOREST = "To unlock the forest's secrets, you must heed the whispers of the wind, follow the guidance of wise novels, and delve into forgotten tombs. \nEmbrace the spirit of adventure, and the forest will reveal its hidden truths."

def unknownRandomRep():
    response = ["Your words bewilder this ancient machine. Speak in simpler terms, that I may understand.",
                "Oh, the mysteries of your query! Simplify, so I may comprehend.",
                "Alas, your words elude this contraption. Speak plainly, that I may assist.",
                "Oh, the riddles within your words! Speak in simpler ways, that I may grasp your intent."][
        random.randrange(4)]
    return response