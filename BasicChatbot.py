import spacy

# Load the spaCy English model
nlp = spacy.load('en_core_web_sm')

# Define a dictionary for simple pattern-response pairs
responses = {
    'greet': ['Hello!', 'Hi there!', 'Hey!'],
    'name': ['I am a chatbot created using spaCy.'],
    'how are you': ['I am doing well, how about you?', 'I am great! Thanks for asking.'],
    'goodbye': ['Goodbye! Have a nice day!']
}

# Function to process the user's input and return the appropriate response
def get_response(user_input):
    doc = nlp(user_input.lower())  # Process the user's input using spaCy's NLP model
    
    # Check for certain keywords to determine the response
    if any(token.lemma_ in ['hi', 'hello', 'hey'] for token in doc):
        return responses['greet']
    elif any(token.lemma_ in ['name'] for token in doc):
        return responses['name']
    elif 'how' in user_input.lower() and 'you' in user_input.lower():
        return responses['how are you']
    elif any(token.lemma_ in ['bye', 'goodbye'] for token in doc):
        return responses['goodbye']
    else:
        return ["I'm sorry, I didn't understand that."]

# Start the chatbot conversation
def start_chatbot():
    print("Chatbot: Hello! I am a chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye!")
            break
        
        # Get the chatbot's response
        response = get_response(user_input)
        print("Chatbot:", response[0])

# Run the chatbot
if __name__ == '__main__':
    start_chatbot()
    