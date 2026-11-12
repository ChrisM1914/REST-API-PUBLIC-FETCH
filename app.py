from flask import Flask, jsonify
import requests

app = Flask(__name__)

URL = "https://vpic.nhtsa.dot.gov/api/vehicles/GetVehicleVariableList?format=json"


@app.route("/items", methods=["GET"])
def get_items():
    """Fetch NHTSA vehicle variables and return only the
    'Active Safety System' group."""
    try:
        resp = requests.get(URL, timeout=15)
        resp.raise_for_status()
        data = resp.json()

        # NHTSA nests the records inside a "Results" list
        results = data.get("Results", [])

        # Only change from the example: the filter
        filtered = [
            item for item in results if item.get("GroupName") == "Active Safety System"
        ]

        return jsonify(filtered), 200

    except requests.exceptions.HTTPError as http_err:
        return jsonify({"error": f"HTTP error: {http_err}"}), resp.status_code
    except requests.exceptions.RequestException as err:
        return jsonify({"error": f"Network error: {err}"}), 503


if __name__ == "__main__":
    app.run(debug=True, port=5000)
