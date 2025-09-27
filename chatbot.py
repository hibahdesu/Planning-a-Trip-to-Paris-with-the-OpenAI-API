# Start your code here!
import os
from openai import OpenAI

# Define the model to use
model = "gpt-4o-mini"

# Define the client
client = OpenAI()


conversation = [
    {"role": "system", "content": "You are a helpful chatbot that answers questions from tourists visiting Paris."},
    {"role": "user", "content": "How far away is the Louvre from the Eiffel Tower (in miles) if you are driving?"},
    {"role": "assistant", "content": "The driving distance between the Eiffel Tower and the Louvre is about 3 miles (around 4.8 kilometers)."},
    {"role": "user", "content": "Where is the Arc de Triomphe?"},
    {"role": "assistant", "content": "The Arc de Triomphe is located at the western end of the Champs-Élysées, on Place Charles de Gaulle in Paris."},
    {"role": "user", "content": "What are the must-see artworks at the Louvre Museum?"},
    {"role": "assistant", "content": "Some must-see artworks at the Louvre include the Mona Lisa by Leonardo da Vinci, the Venus de Milo, the Winged Victory of Samothrace, Liberty Leading the People by Eugène Delacroix, and The Coronation of Napoleon by Jacques-Louis David."}
]

messages_list = []


for message in conversation:
    messages_list.append(message)
    if message['role'] == 'user':
    
        response = client.chat.completions.create(
            model=model,
            messages=messages_list,
            temperature=0.0,
            max_tokens=100
        )

        print(f'User: {message["content"]}')
        print(f'Answer: {response.choices[0].message.content}')