# ChatGPT example

# Steps
## venv
* cd to root directory of this project
* python3 -m venv venv
* source venv/bin/activate(every time you open a new terminal)
* pip install -r requirements.txt

## API KEY
* Put your API KEY in .env file at root directory

## development server
* python3 app.py

## production server(waitress)
* waitress-serve --port=5000 app:app

## Docker
* docker build -t chatgpt .
* docker run -dp5000:5000 --name chatgpt chatgpt