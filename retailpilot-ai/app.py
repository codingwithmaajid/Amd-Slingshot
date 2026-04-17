from flask import Flask, render_template, request, jsonify
from engine import RetailDecisionEngine
import os

app = Flask(__name__)
engine = RetailDecisionEngine()

# Simulated database for notifications/actions
system_logs = [
    {"type": "info", "msg": "RetailPilot AI Engine Initialized", "detail": "System ready for autonomous operations.", "time": "System Start"}
]

@app.route('/')
def customer_interface():
    return render_template('index.html')

@app.route('/admin')
def owner_interface():
    return render_template('admin.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    query = data.get('query', '')
    
    if not query:
        return jsonify({"error": "No query provided"}), 400

    # 1. Agent Processes Decision
    decision = engine.process_request(query)
    
    # 2. Agent Notifies the Owner (Logging the action)
    log_entry = {
        "type": decision['status'],
        "msg": f"Agent Action: {decision.get('decision', 'LOG')} for '{query}'",
        "detail": decision.get('message', ''),
        "time": "Just Now"
    }
    system_logs.insert(0, log_entry) # Newest first
    
    return jsonify(decision)

@app.route('/api/logs')
def get_logs():
    return jsonify(system_logs)

if __name__ == '__main__':
    # Cloud Run provides the PORT environment variable
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)