# ---------------------------------
# CASE STUDY 4: HOSPITAL API
# ---------------------------------

from flask import Flask, request, jsonify

app = Flask(__name__)

patients = []

# Register patient
@app.route("/patients", methods=["POST"])
def add_patient():
    data = request.json
    patients.append(data)
    return jsonify({"message": "Patient added", "patient": data}), 201

# Get all patients
@app.route("/patients", methods=["GET"])
def get_patients():
    return jsonify(patients), 200

if __name__ == "__main__":
    app.run(port=6000, debug=True)