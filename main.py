import re
import long_responses as long
from time import sleep
import pygame

def message_probability(user_message, recon_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_req_words = True

    for word in user_message:
        if word in recon_words:
            message_certainty += 1

    # calculate the percentage of recognized words in user message
    percentage = float(message_certainty) / float(len(recon_words))

    for word in required_words:
        if word not in user_message:
            has_req_words = False
            break

    if has_req_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # short responses
    response("Hello!", ['hello', 'hey'], single_response=True)
    response("I'm doing fine, and you?", ['how', 'are', 'you'], required_words=['how'])
    response("Have a good day! ", ['bye'], required_words=['bye'])

    # long responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_TASK, ['what', 'doing'], required_words=['what', 'doing'])
    response(long.R_STARTGAME, ['play', 'the', 'game'], required_words=['play', 'game'])
    response(long.R_CONFIRM, ['yes', 'yea'], single_response=['yes', 'yea'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)

    if highest_prob_list[best_match] >= 50:
        if best_match == long.R_CONFIRM:
            runningGame()
            return long.R_CONFIRM
        else:
            return best_match
    else:
        return long.unknown()

def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    if response == long.R_CONFIRM:
        return '', True
    else:
        return response, False

def runningGame():
    print(long.R_CONFIRM)
    sleep(2)
    print("Opening game in..")
    sleep(3)
    print("3...")
    sleep(2)
    print("2..")
    sleep(1)
    print("1.")

# pygame setup start --------------------
    pygame.init()
    window_width, window_height = 1250, 1000
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Bubble Buddies")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()

    pygame.quit()
## pygame setup end --------------------

while True:
    user_input, game_started = get_response(input('You: '))
    print('Bot: ' + user_input)
    if game_started:
        break
