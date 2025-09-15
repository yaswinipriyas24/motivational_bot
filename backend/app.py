from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import json
import os

from chatbot.value_mapping import get_values_for_problem
from chatbot.response_builder import build_response

load_dotenv()

app = Flask(__name__)
CORS(app)

# Load data files with UTF-8 explicitly
with open('data/problems.json', encoding='utf-8') as f:
    problems_data = json.load(f)

with open('data/values.json', encoding='utf-8') as f:
    values_data = json.load(f)

@app.route('/')
def home():
    return "Flask is running!"

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message", "")
    problem_key = identify_problem(user_input)
    values = get_values_for_problem(problem_key,values_data)
    reply, quote = build_response(problem_key, values, values_data,user_input)
    return jsonify({"reply": reply, "quote": quote})

def identify_problem(user_input):
    for key, keywords in problems_data.items():
        for word in keywords:
            if word.lower() in user_input.lower():
                return key
    return "general"

if __name__ == '__main__':
    app.run(debug=True)
