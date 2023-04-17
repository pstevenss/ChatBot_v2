import re
import long_responses as long


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

    #short responses = ---------------------------------------------- test out other bot responses
    response("Hello!", ['hello', 'hi'], single_response=True)
    response("I'm doing fine, and you?", ['how', 'are', 'you'], required_words=['how'])
    response("Have a good day! ", ['bye'], required_words=['bye'])
    #long responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'u', 'eat'], required_words=['u', 'eat'])
    response(long.R_TASK, ['what', 'doing', ], required_words=['what', 'doing'])


    best_match = max(highest_prob_list, key=highest_prob_list.get)

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Testing the response system
while True:
    print('Bot: ' + get_response(input('You: ')))
