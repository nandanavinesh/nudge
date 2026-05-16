from flask import Flask, render_template, request, jsonify
from database import init_db, save_log, get_all_logs
from ml import get_analysis

app = Flask(__name__)
init_db()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/log', methods=['POST'])
def log():
    data = request.get_json()
    save_log(
        data['date'],
        data['social_media'],
        data['productive_screen'],
        data['tasks_completed'],
        data['sleep_hours'],
        data['mood']
    )
    return jsonify({'status': 'saved!'})

@app.route('/api/logs', methods=['GET'])
def logs():
    all_logs = get_all_logs()
    return jsonify(all_logs)

@app.route('/api/analysis', methods=['GET'])
def analysis():
    return jsonify(get_analysis())

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)