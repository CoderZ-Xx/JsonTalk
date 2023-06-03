import json
import random
import re

# Check if the JSON file exists
def check_json_file():
    try:
        with open('chatbot.json') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save the conversation to the JSON file
def save_conversation(data):
    with open('chatbot.json', 'w') as file:
        json.dump(data, file, indent=4)

# Perform math operation
def perform_operation(num1, operation, num2):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    else:
        return None

# Process math-related question
def process_math_question(user_prompt):
    match = re.search(r'whats? (\d+) ([+\-*/]) (\d+)', user_prompt)
    if match:
        num1 = int(match.group(1))
        operation = match.group(2)
        num2 = int(match.group(3))
        result = perform_operation(num1, operation, num2)
        if result is not None:
            return str(result)
    return None

# Load the JSON file and retrieve the bot's response
def get_bot_response(user_prompt):
    data = check_json_file()
    bot_response = data.get(user_prompt)
    if not bot_response:
        bot_response = process_math_question(user_prompt)
        if bot_response is None:
            bot_response = input("Bot: I'm sorry, I don't have a response. Could you please provide one? ")
        data[user_prompt] = bot_response
        save_conversation(data)
    elif '|' in bot_response:
        bot_response_options = bot_response.split('|')
        bot_response = random.choice(bot_response_options)
    return bot_response

print("Math format need to be written as ''Whats [num] [operation] [num]? : Use | between teaching the ChatBot to add multiple responses")

# Main loop
while True:
    user_input = input('User: ')
    user_input = user_input.lower()
    bot_response = get_bot_response(user_input)
    print('Bot:', bot_response)
    