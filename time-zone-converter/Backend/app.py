from flask import Flask, request, jsonify, render_template
from datetime import datetime
import pytz
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    static_folder=os.path.join(BASE_DIR, "../frontend/static"),
    template_folder=os.path.join(BASE_DIR, "../frontend")
)


@app.route("/")
def home():
    return render_template("index.html")  # Flask will find frontend/index.html

@app.route("/convert", methods=["POST"])
def convert_logs():
    try:
        data = request.get_json()
        logs = data.get("logs", "")
        target_tz = data.get("tz", "Asia/Kolkata")

        utc = pytz.utc
        target_timezone = pytz.timezone(target_tz)

        converted_lines = []
        for line in logs.splitlines():
            try:
                # Parse strict format YYYY-MM-DD HH:MM:SS
                utc_time = utc.localize(datetime.strptime(line.strip(), "%Y-%m-%d %H:%M:%S"))
                converted_time = utc_time.astimezone(target_timezone)
                converted_lines.append(
                    f"{line} → {converted_time.strftime('%Y-%m-%d %H:%M:%S')} {target_tz}"
                )
            except Exception:
                converted_lines.append(f"{line} (invalid or skipped)")

        return jsonify({"converted_logs": converted_lines})

    except Exception as e:
        return jsonify({"error": str(e)}), 400




if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))