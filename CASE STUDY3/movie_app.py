# -------------------------------
# CASE STUDY 3: MOVIE TICKET API
# -------------------------------

from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy database
movies = [
    {"id": 1, "name": "Avatar"},
    {"id": 2, "name": "Inception"}
]

bookings = []

# GET all movies
@app.route("/movies", methods=["GET"])
def get_movies():
    return jsonify(movies), 200

# GET shows for a movie
@app.route("/movies/<int:movie_id>/shows", methods=["GET"])
def get_shows(movie_id):
    shows = ["10:00 AM", "2:00 PM", "6:00 PM"]
    return jsonify({"movie_id": movie_id, "shows": shows}), 200

# POST book ticket
@app.route("/bookings", methods=["POST"])
def book_ticket():
    data = request.json
    bookings.append(data)
    return jsonify({"message": "Ticket booked successfully", "booking": data}), 201

# GET booking details
@app.route("/bookings", methods=["GET"])
def get_bookings():
    return jsonify(bookings), 200

if __name__ == "__main__":
    app.run(port=5000, debug=True)