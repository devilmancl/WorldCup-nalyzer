class GroupMember:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.goals = 0
        self.goals_received = 0
        self.games_played = 0

    def get_table_row(self):
        data = {
            "name": self.name,
            "points": self.points,
            "goals_difference": self.goals - self.goals_received,
            "games_played": self.games_played,
            "goals": self.goals,
            "goals_received": self.goals_received
        }
        return data

    def add_goals(self, goals):
        self.goals = self.goals + goals

    def add_goals_received(self, goals_received):
        self.goals_received = self.goals_received + goals_received

    def add_points(self, points):
        self.points = self.points + points

    def add_game_played(self):
        self.games_played = self.games_played + 1