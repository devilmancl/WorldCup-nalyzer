from libs.Group import Group
from libs.JSonReader import JSonReader
from libs.Playoffs import Playoffs
import json

if __name__ == '__main__':
    reader = JSonReader()
    groups_in = reader.data["groups"]
    groups_names = groups_in.keys()
    groups = []
    for group_name in groups_names:
        group = Group(group_name, groups_in[group_name])
        groups.append(group.get_results())

    playoffs = Playoffs()

    playoffs.process_groups(groups)

    playoffs_in = reader.data["playoffs"]
    playoffs_definitions = playoffs_in["definitions"]
    playoffs_predictions = playoffs_in["predictions"]
    playoffs_results = playoffs_in["results"]

    playoffs.process_definitions(playoffs_definitions)
    playoffs.process_predictions(playoffs_predictions)
    playoffs.process_results(playoffs_results)

    result = {"groups": groups, "playoff": playoffs.get_results()}

    with open('out.json', 'w') as f:
        json_object = json.dumps(result, indent=2)
        print(json_object, file=f)

