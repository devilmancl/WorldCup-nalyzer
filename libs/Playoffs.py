from libs.PlayoffMatch import PlayoffMatch


class Playoffs:
    def __init__(self):
        self.matches = {}
        self.winners = {}

    def get_results(self):
        matches = []
        for match_name in self.matches:
            matches.append(self.matches[match_name].get_results())
        return matches

    def process_definitions(self, definitions):
        for definition_name in definitions:
            match = PlayoffMatch(definition_name, definitions[definition_name], self.winners, self.matches)
            self.matches[definition_name] = match

    def process_groups(self, groups):
        for group in groups:
            group_name = group["group"]
            group_team_1 = group["classified"][0]
            group_team_2 = group["classified"][1]
            self.winners["GROUP_" + group_name + "_1"] = group_team_1
            self.winners["GROUP_" + group_name + "_2"] = group_team_2

    def process_predictions(self, predictions):
        for prediction_name in predictions:
            winner = self.matches[prediction_name].set_result(predictions[prediction_name], self.matches)
            if not winner is None:
                self.winners[prediction_name] = winner

    def process_results(self, results):
        for result_name in results:
            winner = self.matches[result_name].set_result(results[result_name], self.matches)
            if not winner is None:
                self.winners[result_name] = winner