import json
from die import Die
from collections import OrderedDict


def encounter_gen(file_location, encounter_location, die_role):
    with open(file_location + encounter_location.replace(" ", "_").replace("'", "").lower()+'.json') as data_file:
        data = json.load(data_file)
    for entry in data['encounter']:
        if entry['roll'] == die_role:
            encounter_dict = OrderedDict()
            encounter_dict['terrain'] = data['terrain']
            encounter_dict['encounter'] = entry['value']
            encounter_dict['is_italic'] = entry['italic']
            encounter_dict['is_special'] = entry['special']
            encounter_dict['number'] = entry['number']
            if 'bold' in entry.keys():
                encounter_dict['is_bold'] = entry['bold']
            if entry['rand_num']:
                encounter_dict['die_type'] = entry['die_type']
                encounter_dict['die_num'] = entry['die_num']
                return encounter_dict
            else:
                return encounter_dict


location = "tables\\location\\"

location_choice = "test"

encounter = encounter_gen(location, location_choice, Die(6).three_die_straight())

if encounter['is_italic']:
    print("Encounter Occurs")
    for x, y in encounter.items():
        print(f'{x:7} \t\t {str(y)}')
elif encounter['is_bold']:
    print(f"roll 3d6 on {encounter['encounter']} {encounter['terrain']} Table")
    terrain = "tables\\terrain\\" + encounter['terrain'] + "\\"
    terrain_encounter = encounter_gen(terrain, encounter['encounter'], Die(6).three_die_straight())
    for x, y in terrain_encounter.items():
        print(f'{x:7} \t\t {str(y)}')
elif encounter['is_special']:
    print(f"A special encounter has occurred with {encounter['encounter']}")
else:
    print("Roll again!")

