import openai
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()

openai.api_key = os.getenv("OPEN_AI_API_KEY")

async def send_message(message_log):
    response = await manage_request(message_log)
    for choice in response.choices:
        if "text" in choice:
            return choice.text
    return response.choices[0].message.content

async def manage_request(message_log):
    response = await asyncio.to_thread(openai.ChatCompletion.create,
                                       model="gpt-3.5-turbo",
                                       messages=message_log,
                                       max_tokens=3800,
                                       stop=None,
                                       temperature=0.7)
    return response

# execute twice to test async
async def main():
    print(await send_message([{"role": "user", "content": "地球上最高的地方"}]))
    print(await send_message([{"role": "user", "content": "地球上最深的洞窟"}]))



if __name__ == '__main__':
    asyncio.run(main())

# Main response test function
# @app.route('/chatbot', methods=['POST'])
# def chatbot():
#     # display message_stream

#     print(">>>>>>>>>>",message_stream)
#     # incomming message style : {"message_log": "hi"}
#     new_log = request.json['message_log']
#     message_stream.append({'role': 'user', 'content': new_log})
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",  # 使用的模型
#         messages=message_stream,   # 對話紀錄
#         max_tokens=3800,        # token上限
#         stop="exit",            # 結束對話的字串
#         temperature=0.7,        # 越高越有創意
#     )

#     print(response)
#     for choice in response.choices:
#         if "text" in choice:
#             return choice.text
#     # retuen json
#     return jsonify(response.choices[0].message.content)
#     # return response.choices[0].message.content