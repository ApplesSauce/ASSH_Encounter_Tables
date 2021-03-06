import json
from die import Die
from collections import OrderedDict


def encounter_gen(location, die_role):
    with open(tables+location+'.json') as data_file:
        data = json.load(data_file)
    for entry in data['encounter']:
        if entry['roll'] == die_role:
            encounter_dict = OrderedDict()
            encounter_dict['encounter'] = entry['value']
            encounter_dict['is_lower'] = entry['lower']
            encounter_dict['is_italic'] = entry['italic']
            encounter_dict['is_bold'] = entry['bold']
            encounter_dict['is_special'] = entry['special']
            encounter_dict['number'] = entry['number']
            return encounter_dict

tables = "tables\\"
encounter_location = "abbica_mere"

encounter = encounter_gen(encounter_location, str(Die(6).three_die_straight()))

for x, y in encounter.items():
    print(f'{x:7} \t\t {str(y)}')

