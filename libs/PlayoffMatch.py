class PlayoffMatch:
    def __init__(self, name, definition, winners, matches):
        self.name = name
        self.team1 = definition[0]
        self.match_to_change = None
        if not self.team1.startswith("GROUP_"):
            matches[self.team1].match_to_change = name
        if not winners.get(definition[0]) is None:
            self.team1 = winners[definition[0]]

        self.team2 = definition[1]
        if not self.team2.startswith("GROUP_"):
            matches[self.team2].match_to_change = name
        if not winners.get(definition[1]) is None:
            self.team2 = winners[definition[1]]

        self.team1goals = 0
        self.team2goals = 0
        self.team1penalties = 0
        self.team2penalties = 0
        self.winner = None

    def set_result(self, result, matches):
        teams = list(result.keys())
        self.team1 = teams[0]
        self.team2 = teams[1]

        self.team1goals = result[teams[0]]["goals"]
        self.team2goals = result[teams[1]]["goals"]
        self.team1penalties = result[teams[0]]["penalties"]
        self.team2penalties = result[teams[1]]["penalties"]

        self.winner = self.get_winner()
        if not self.match_to_change is None:
            matches[self.match_to_change].replace_team(self.name, self.winner)
        return self.winner;

    def replace_team(self, definition_name, prev_winner):
        if self.team1 == definition_name:
            self.team1 = prev_winner

        if self.team2 == definition_name:
            self.team2 = prev_winner

    def get_winner(self):
        if self.team1goals > self.team2goals:
            return self.team1
        elif self.team1goals < self.team2goals:
            return self.team2

        if self.team1penalties > self.team2penalties:
            return self.team1
        elif self.team1penalties < self.team2penalties:
            return self.team2

        return None

    def get_results(self):
        return {"match": self.name,
                "teams": {
                    self.team1: {"goals": self.team1goals, "penalties": self.team1penalties},
                    self.team2: {"goals": self.team2goals, "penalties": self.team2penalties}},
                "winner": self.winner,
                "match_to_change": self.match_to_change}