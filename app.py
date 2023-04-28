from flask import Flask, render_template, request, jsonify, abort
import os
import openai
from dotenv import load_dotenv
from linebot.exceptions import InvalidSignatureError
from linebot import LineBotApi, WebhookHandler
from linebot.models import TextSendMessage, MessageEvent, TextMessage

load_dotenv()

openai.api_key = os.getenv("OPEN_AI_API_KEY")
line_bot_api = LineBotApi(os.getenv("LINE_CHANNEL_ACCESS_TOKEN"))
handler = WebhookHandler(os.getenv("LINE_CHANNEL_SECRET"))

app = Flask(__name__, static_folder='static', template_folder='templates', static_url_path='/static')

message_stream = []

# 測試用網頁
# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    # print(body)
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
    message_log = [{"role": "user", "content": message}]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # 使用的模型
        messages=message_log,   # 對話紀錄
        max_tokens=3800,        # token上限
        stop="exit",            # 結束對話的字串
        temperature=0.7,   
    )

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=response.choices[0].message.content)
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)






# 網頁版
# HOW TO RUN
# 1. create virtual environment: (At root dir)python3 -m venv venv
# 2. activate virtual environment: source venv/bin/activate
# 3. install packages: pip install -r requirements.txt
# 4. run app: python3 app.py

# HOW TO RUN WITH DOCKER
# 1. build image: docker build -t chatgpt .
# 2. run container: docker run -d -p 5000:5000 chatgpt
# 3. check container: docker ps
# 4. Open browser and go to http://localhost:5000/
# 5. stop container: docker stop <container id>
# 6. remove container: docker rm <container id>