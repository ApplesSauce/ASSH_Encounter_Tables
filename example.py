import json
from pprint import pprint
from die import Die
from collections import OrderedDict


def stat_gen(ability_name, score):
    if ability_name == "strength":
        with open('strength_stats.json') as data_file:
            data = json.load(data_file)
        for entry in data['scores']:
            if entry['value'] == score:
                str_dict = OrderedDict()
                str_dict['hit probability'] = entry['hit']
                str_dict['damage adjustment'] = entry['damage']
                str_dict['weight allowance'] = entry['weight']
                str_dict['open doors on a'] = entry['door']
                str_dict['bend bars/lift gates'] = entry['bar']
    return str_dict

def ability_score():
    return Die(6).four_die_drop_low()

character_stats = OrderedDict()
character_stats['strength'] = ability_score()
#character_stats['intelligence'] = ability_score()
#character_stats['wisdom'] = ability_score()
#character_stats['dexterity'] = ability_score()
#character_stats['constitution'] = ability_score()
#character_stats['charisma'] = ability_score()

for x, y in character_stats.items():
    #print(ability)
    #print(score)
    final_stats = stat_gen(x, y)
    for a, b in final_stats.items():
        print(a + " " + str(b))
