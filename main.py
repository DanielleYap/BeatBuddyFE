from flask import Flask, render_template, request
import openai
import api

app = Flask(__name__, static_folder='static', static_url_path='')

openai.api_key = api.CHAT_API_KEY

@app.route("/")
def home():    
    return render_template("chat.html")

if __name__ == "__main__":
    app.run(debug=True)
