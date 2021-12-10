from players_app.config.mysqlconnection import connectToMySQL
from datetime import datetime

class Player:

    db = "players_club"

    def __init__(self, data):
        # data: dictionary from mysqlconnection
        self.firstName = data["firstName"]
        self.lastName = data["lastName"]

        # Students do this - Edgar (interesting!)
        # self.full_name = f"{data['firstName']} {data['lastName']}"
        
        self.position = data["position"]
        self.dob = data["dob"]
        self.height = data["height"]
        self.weight = data["weight"]

    def weight_lbs(self):
        return f"{int(self.weight * 2.2)} lbs"

    def height_ft_in(self):
        #TODO: convert cm to ft' - in"
        pass

    def full_name(self):
        return f"{self.firstName} {self.lastName}!"

    @classmethod
    def get_all_players(cls):

        result = connectToMySQL(db).query_db("SELECT * FROM players")
        # players = []
        # for row in result:
        #     players.append(cls(row))
        
        players = [ cls(row) for row in result ]

        return players

