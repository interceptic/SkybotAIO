import openai
import json
import asyncio

client = openai.OpenAI()


# make sure to set your API key

def openai_response(prompt, message):
    with open("ai_history.json") as history:
        history = json.load(history)
    message_history = history['ids'][f'{message.author.id}']['messages']
    message_history = message_history
    response_history = history['ids'][f'{message.author.id}']['responses']
    prompt = prompt + f'Keep in mind my previous messages: {message_history}' + f'\nkeep your messages in mind aswell: {response_history}'
    system_message = ()
    try:
        response = client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt}
        ],
        max_tokens=80, 
        temperature=0.9
        )
        message = response.choices[0].message.content
        return message
    except Exception as e:
        print(f"Error getting OpenAI response: {e}")
        return "Sorry, I couldn't process that request."
    
async def ratelimit(user): # not used
    await asyncio.sleep(60)
    user = 0
    return user
