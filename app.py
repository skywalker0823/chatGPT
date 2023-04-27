from flask import Flask, render_template, request, jsonify
import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("API_KEY")

app = Flask(__name__, static_folder='static', template_folder='templates', static_url_path='/static')

prev_message = ""
prev_answer = ""

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

    print(response)
    for choice in response.choices:
        if "text" in choice:
            return choice.text
    # retuen json
    return jsonify(response.choices[0].message.content)
    # return response.choices[0].message.content

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)



#HOW TO RUN
# 1. create virtual environment: (At root dir)python3 -m venv venv
# 2. activate virtual environment: source venv/bin/activate
# 3. install packages: pip install -r requirements.txt
# 4. run app: python3 app.py

#HOW TO RUN WITH DOCKER
# 1. build image: docker build -t chatgpt .
# 2. run container: docker run -d -p 5000:5000 chatgpt
# 3. check container: docker ps
# 4. Open browser and go to http://localhost:5000/
# 5. stop container: docker stop <container id>
# 6. remove container: docker rm <container id>