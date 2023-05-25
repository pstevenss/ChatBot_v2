import re
import long_responses as long
from time import sleep
import pygame as pg

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
    import pygame as pg

    # pygame setup start --------------------
    pg.init()
    screen_width = 928
    screen_height = 650
    screen = pg.display.set_mode((screen_width, screen_height))
    clock = pg.time.Clock()
    vel = 5
    x = 0
    y = 565
    width = 40
    height = 60
    pg.display.set_caption("Bubble Buddies")

    # Load sprite images
    forestBg = pg.image.load('sprite_Images/Background.png')
    forestBg = pg.transform.scale(forestBg, (screen_width, screen_height))
    adventIdle00 = pg.image.load('sprite_Images/adventurer-idle-00.png')

    adventRunSprites = []

    # Load and scale the original sprites
    adventRunSprites.append(pg.transform.scale(pg.image.load('sprite_Images/adventurer-run-00.png'), (55, 42)))
    adventRunSprites.append(pg.transform.scale(pg.image.load('sprite_Images/adventurer-run-01.png'), (55, 42)))
    adventRunSprites.append(pg.transform.scale(pg.image.load('sprite_Images/adventurer-run-02.png'), (55, 42)))
    adventRunSprites.append(pg.transform.scale(pg.image.load('sprite_Images/adventurer-run-03.png'), (55, 42)))
    adventRunSprites.append(pg.transform.scale(pg.image.load('sprite_Images/adventurer-run-04.png'), (55, 42)))
    adventRunSprites.append(pg.transform.scale(pg.image.load('sprite_Images/adventurer-run-05.png'), (55, 42)))

    # Create flipped versions of the sprites
    adventRunSpritesFlipped = [pg.transform.flip(sprite, True, False) for sprite in adventRunSprites]

    isJump = False
    jumpCount = 5
    left = False
    right = False
    walkCount = 0

    def redrawGameWindow():
        global walkCount

        # Blit the background image
        screen.blit(forestBg, (0, 0))

        if left:
            sprite_index = walkCount // 3
            if sprite_index < len(adventRunSpritesFlipped):
                screen.blit(adventRunSpritesFlipped[sprite_index], (x, y))
            else:
                walkCount = 0
                sprite_index = walkCount // 3
                screen.blit(adventRunSpritesFlipped[sprite_index], (x, y))
            walkCount += 1
        elif right:
            sprite_index = walkCount // 3
            if sprite_index < len(adventRunSprites):
                screen.blit(adventRunSprites[sprite_index], (x, y))
            else:
                walkCount = 0
                sprite_index = walkCount // 3
                screen.blit(adventRunSprites[sprite_index], (x, y))
            walkCount += 1
        else:
            screen.blit(adventIdle00, (x, y))  # Display idle image when not moving
            walkCount = 0

        pg.display.update()

    ## main loops
    run = True

    while run:
        clock.tick(27)

        # Background sprite Forest - dark
        # screen.blit(forestBg, (0, 0))

        # # Show sprite character images
        # screen.blit(adventRun0, (0, 565))
        # screen.blit(adventRun1, (25, 565))
        # screen.blit(adventRun2, (50, 565))
        # screen.blit(adventRun3, (75, 565))
        # screen.blit(adventRun4, (100, 565))
        # screen.blit(adventRun5, (125, 565))
        #

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT] and x > vel:
            x -= vel
            left = True
            right = False

        elif keys[pg.K_RIGHT] and x < screen_width - vel - width:
            x += vel
            left = False
            right = True

        else:
            left = False
            right = False
            walkCount = 0

        if not (isJump):
            if keys[pg.K_SPACE]:
                isJump = True
                left = False
                right = False
                walkCount = 0
        else:
            if jumpCount >= -5:
                y -= (jumpCount * abs(jumpCount)) * 0.5
                jumpCount -= 1
            else:
                jumpCount = 5
                isJump = False

        redrawGameWindow()

    pg.quit()

    ## pygame setup end --------------------


while True:
    user_input, game_started = get_response(input('You: '))
    print('Bot: ' + user_input)
    if game_started:
        break
