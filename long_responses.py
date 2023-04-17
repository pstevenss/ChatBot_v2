import random

R_STARTGAME = "Are you sure you want to play the game?"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
R_TASK = "Not doing anything... sitting in limbo..."

def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Um...",
                "What does that mean?"][
        random.randrange(4)]
    return response