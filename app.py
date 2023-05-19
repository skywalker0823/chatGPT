from flask import Flask, render_template, request, jsonify, abort
import os, openai
from dotenv import load_dotenv
from linebot.exceptions import InvalidSignatureError
from linebot import LineBotApi, WebhookHandler
from linebot.models import TextSendMessage, MessageEvent, TextMessage

load_dotenv()

openai.api_key = os.getenv("OPEN_AI_API_KEY")
line_bot_api = LineBotApi(os.getenv("LINE_CHANNEL_ACCESS_TOKEN"))
handler = WebhookHandler(os.getenv("LINE_CHANNEL_SECRET"))

app = Flask(__name__, static_folder='static', template_folder='templates', static_url_path='/static')

user_list_in_memory = []
conversation_history = {}

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    # get user id
    user_id = request.json['events'][0]['source']['userId']
    if user_id not in user_list_in_memory:
        user_list_in_memory.append(user_id)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
    return 'OK'

# Line chatGPT
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = event.message.text
    user_id = event.source.user_id
    try:
        if message == "clear" or message == "清除" or message == "清空" or message == "清除歷史" or message == "清空歷史":
            conversation_history[user_id] = []
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="已清除歷史訊息")
            )
        elif message == "get_list":
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=str(user_list_in_memory))
            )
        elif message == "get_history":
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=str(conversation_history))
            )
        else:
                if user_id not in conversation_history:
                    conversation_history[user_id] = []
                conversation_history[user_id].append({"role": "user", "content": message})
                message_log = conversation_history[user_id]
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",  # 使用的模型
                    messages=message_log,   # 對話紀錄
                    max_tokens=4097,        # token上限
                    stop="exit",            # 結束對話的字串
                    temperature=0.7,   
                )
                conversation_history[user_id].append({"role": "assistant", "content": response.choices[0].message.content})
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=response.choices[0].message.content)
                )
    except Exception as e:
        print(e)
        # clear conversation history
        conversation_history[user_id] = []
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Oops! 發生了一點問題，已為您清除歷史訊息，請重新嘗試")
        )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)







# HOW TO RUN WITH DOCKER
# 1. build image: docker build -t chatgpt .
# 2. run container: docker run -d -p 5000:5000 chatgpt
# 3. check container: docker ps
# 4. Open browser and go to http://localhost:5000/
# 5. stop container: docker stop <container id>
# 6. remove container: docker rm <container id>