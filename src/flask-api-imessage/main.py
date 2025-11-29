#!/usr/bin/env uv run

from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route("/send_message", methods=["POST"])
def send_message():
    data = request.get_json()
    if not data or "phone" not in data or "message" not in data:
        return jsonify({"error": "phone and message are required"}), 400

    phone = data["phone"]
    message = data["message"]

    # AppleScript to send message via Messages app
    applescript = f'''
    tell application "Messages"
        set targetService to 1st service whose service type = iMessage
        set targetBuddy to buddy "{phone}" of targetService
        send "{message}" to targetBuddy
    end tell
    '''

    try:
        subprocess.run(["osascript", "-e", applescript], check=True)
    except subprocess.CalledProcessError:
        return jsonify({"status": "failed to send"}), 500

    return jsonify({"status": "sent"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555)
