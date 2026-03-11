from flask import Flask, jsonify, render_template
import json
import subprocess
from ping_service import statuses, ping_loop
import threading
threading.Thread(target=ping_loop, daemon=True).start()
app=Flask(__name__)


@app.route('/api/status')
def route():
    result = []

    for ip, status in statuses.items():
        result.append({
            "ip": ip,
            "status": status
        })

    return jsonify(result)
@app.route('/')
def html():
    return render_template("index.html")


if __name__=="__main__":
    app.run(host="0.0.0.0", port=5001)