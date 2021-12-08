from players_app.config.mysqlconnection import connectToMySQL
from datetime import datetime

class Player:
    db_name = "players_club"

    def __init__(self, data):
        self.firstName = data["firstName"]
        self.lastName = data["lastName"]
        self.position = data["position"]
        self.dob = data["dob"]
        self.height = data["height"]
        self.weight = data["weight"]
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM players;"
        results = connectToMySQL("players_club").query_db(query)
        return [ cls(x) for x in results ]

    @classmethod
    def create(cls, data):
        query = "INSERT INTO players \
                (firstName, lastName, position, dob, height, weight) VALUES \
                (%(firstName)s,%(lastName)s,%(position)s,%(dob)s,%(height)s,%(weight)s)"
        connectToMySQL("players_club").query_db(query, data)

    @property
    def full_name(self):
        return f"{self.firstName} {self.lastName}"
    
    @property
    def dob_formatted(self):
        return datetime.strftime(self.dob, "%D")

    @property
    def age(self):
        return int((datetime.now() - self.dob).days / 365)
    
    @property
    def height_formatted(self):
        to_ft_inches = divmod(
            self.height/2.54,
            12
        )
        return f"{to_ft_inches[0]}\' {round(to_ft_inches[1])}\""