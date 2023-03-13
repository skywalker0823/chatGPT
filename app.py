from flask import Flask, render_template, request, jsonify
import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("API_KEY")

app = Flask(__name__, static_folder='static', template_folder='templates', static_url_path='/static')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chatbot', methods=['POST'])
def chatbot():
    message_log = request.json['message_log']
    print(message_log)
    message_log = [{"role": "user", "content": message_log}]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # 使用的模型
        messages=message_log,   # 對話紀錄
        max_tokens=3800,        # token上限
        stop="exit",            # 結束對話的字串
        temperature=0.7,        # 越高越有創意
    )

    for choice in response.choices:
        if "text" in choice:
            return choice.text
    # retuen json
    return jsonify(response.choices[0].message.content)
    # return response.choices[0].message.content

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


# venv
# cd to root directory of this project
# python3 -m venv venv
# source venv/bin/activate(every time you open a new terminal)
# pip install -r requirements.txt

# API KEY
# Put your API KEY in .env file at root directory

# development server
# python3 app.py

# production server(waitress)
# waitress-serve --port=5000 app:app

# Docker
# docker build -t chatgpt .
# docker run -dp5000:5000 --name chatgpt chatgpt
