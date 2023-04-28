# Simple ChatGPT example with LINE Messaging API
為了能更簡單的使用 chatGPT for LINE, 這裡提供簡單的範例
未來會慢慢完善整個步驟

# Requirements


# Steps
* clone this repo
* cd to root directory of this project
* python3 -m venv venv
* source venv/bin/activate
* pip install -r requirements.txt
* cp .env.example .env

## About KEYs
### OpenAI API KEY
* OPENAI_API_KEY

### LINE Messaging API KEY
* LINE_CHANNEL_ACCESS_TOKEN
* LINE_CHANNEL_SECRET


## Start development server
* 將 app.py 中的 `app.route("/")` 整個部分反註解
* python3 app.py
* Open your browser and go to http://localhost:5000

## production server(waitress)
* waitress-serve --port=5000 app:app

## Docker
* docker build -t chatgpt .
* docker run -dp5000:5000 --name chatgpt chatgpt

## About ngrok
* 這個東西可以將 localhost:5000 轉換成一個可以讓外部網路存取的網址，拿來測試很方便
