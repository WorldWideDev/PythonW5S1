from players_app import app
from players_app.controllers import players
print("in server.py")
if __name__ == "__main__":
    print("in main")
    app.run(debug=True)