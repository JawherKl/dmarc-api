from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import subprocess
import json  # Import json for pretty-printing

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/checkdmarc', methods=['POST'])
def check_dmarc():
    # Get the domain and format from the request
    domain = request.json.get('domain')
    output_format = request.json.get('format', 'json').lower()

    if not domain:
        return jsonify({"error": "Domain is required"}), 400

    if output_format not in ['json', 'csv']:
        return jsonify({"error": "Invalid format. Use 'json' or 'csv'."}), 400

    # Prepare the checkdmarc command
    try:
        result = subprocess.run(
            ['checkdmarc', domain, '-f', output_format],
            capture_output=True,
            text=True
        )

        # Return the output based on the requested format
        if output_format == 'json':
            # Use json.loads to convert string to JSON and pretty-print it
            pretty_json = json.dumps(json.loads(result.stdout), indent=4)
            return jsonify(json.loads(pretty_json)), 200
        elif output_format == 'csv':
            return result.stdout, 200, {'Content-Type': 'text/csv'}

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9060)
