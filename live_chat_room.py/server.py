from flask import Flask, render_template, request, session, redirect
from flask_socketio import join_room, leave_room, send, SocketIO
import random
from string import ascii_uppercase

app =  Flask(__name__) # Create a Flask web application instance

app.config["SECRET_KEY"] = "sukashak" # Create a Flask web application instance
socketio = SocketIO(app) # Initialize SocketIO for real-time, bi-directional communication between client and server

@app.route("/", methods = ["POST", "GET"])
def home():
    return render_template("home.html")

# This block ensures that the server runs only when this script  is executed directly (not when imported as a module)
if __name__ == "__main__":
    socketio.run(app, debug=True)     # Run the Flask-SocketIO app in debug mode, Debug mode auto-reloads the server when code changes

