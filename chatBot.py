import random

def get_response(user_input):
    user_input = user_input.lower()

# Define some basic responses
    greetings = ['hello', 'hi', 'hey', 'howdy']

    questions = ['how are you?', 'what is your name?', 'what can you do?', 'tell me a joke', 'who created you?', 'what is the weather like today?', 'how can I contact customer support?', 'what time is it?', 'where are you located?', 'how do I reset my password?', 'what are your working hours?', 'tell me a fun fact']

    jokes = ["Why don't scientists trust atoms? Because they make up everything!", "Why did the scarecrow win an award? Because he was outstanding in his field!", "Why did the bicycle fall over? It was two-tired!"]

    weather = ["Today is sunny and warm.", "Expect a few clouds and a slight chance of rain.", "It's going to be a hot day."]

# Generate responses based on user input
    if any(greeting in user_input for greeting in greetings):
        return random.choice(['Hello!', 'Hi!', 'Hey there!', 'Hi, how can I assist you?'])

    elif any(question in user_input for question in questions):
        if 'name' in user_input:
            return "My name is Chatbot."
        elif 'do' in user_input and 'you' in user_input:
            return "I am a simple chatbot. I can respond to basic questions and tell jokes."
        elif 'joke' in user_input:
            return random.choice(jokes)
    elif 'weather' in user_input:
        return random.choice(weather)
    # Add more responses for other questions

    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase your question?"

def main():
    print("Chatbot: Hi, I'm your friendly chatbot. Ask me anything or say hello!")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
