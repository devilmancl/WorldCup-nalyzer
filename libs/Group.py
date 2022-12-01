from libs.GroupMember import GroupMember


class Group:
    def __init__(self, name, data_in):
        self.name = name
        self.members = {}

        self.get_members(data_in["teams"])
        self.process_matches(data_in["predictions"])
        self.process_matches(data_in["matches"])

    def get_results(self):
        table = self.get_table()

        classified = [table[0]["name"], table[1]["name"]]

        return {"group": self.name, "classified": classified, "table": table}

    @staticmethod
    def cmp_table_row(table_row_1):
        return table_row_1["points"] * 1000 + table_row_1["goals_difference"]

    def get_table(self):
        table_rows = []
        for member in self.members:
            table_rows.append(self.members[member].get_table_row())

        table_rows.sort(key=Group.cmp_table_row, reverse=True)

        return table_rows

    def get_members(self, teams_names):
        for team_name in teams_names:
            group_member = GroupMember(team_name)
            self.members[team_name] = group_member

    def process_matches(self, matches):
        for match in matches:
            teams = list(match.keys())

            team1 = teams[0]
            team2 = teams[1]

            team1goals = int(match[team1])
            team2goals = int(match[team2])

            team1points = 0
            team2points = 0

            if team1goals > team2goals:
                team1points = 3
            elif team1goals == team2goals:
                team1points = 1
                team2points = 1
            else:
                team2points = 3

            group_member1 = self.members[team1]
            group_member2 = self.members[team2]

            group_member1.add_game_played()
            group_member1.add_goals(team1goals)
            group_member1.add_goals_received(team2goals)
            group_member1.add_points(team1points)

            group_member2.add_game_played()
            group_member2.add_goals(team2goals)
            group_member2.add_goals_received(team1goals)
            group_member2.add_points(team2points)

            # print("match:" + team1 + " " + str(team1goals) + " " + str(team1points)
            #      + " " + team2 + " " + str(team2goals) + " " + str(team2points))
