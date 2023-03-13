import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("API_KEY")
print(openai.api_key)


def send_message(message_log):

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message_log,
        max_tokens=3800,
        stop=None,
        temperature=0.7,
    )

    for choice in response.choices:
        if "text" in choice:
            return choice.text

    return response.choices[0].message.content


print(send_message([{"role": "user", "content": "最靠近赤道的島嶼是?"}]))