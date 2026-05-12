import os
import json
from flask import Flask, render_template, jsonify, request

app = Flask(__name__, template_folder='.', static_folder='.')

# Arquivo para salvar estatísticas
STATS_FILE = 'user_stats.json'

def load_json(filename):
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_json(filename, data):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/questions')
def get_questions():
    questions = load_json('questions.json')
    return jsonify(questions)

@app.route('/api/stats', methods=['GET', 'POST'])
def manage_stats():
    if request.method == 'POST':
        new_stats = request.json
        save_json(STATS_FILE, new_stats)
        return jsonify({"status": "success"})
    
    current_stats = load_json(STATS_FILE)
    if not current_stats:
        current_stats = {"score": 0, "hits": 0, "total": 0}
    return jsonify(current_stats)

if __name__ == '__main__':
    print("Panasonic Academy Server Iniciado!")
    print("Acesse: http://localhost:5000")
    app.run(debug=True, port=5000)
