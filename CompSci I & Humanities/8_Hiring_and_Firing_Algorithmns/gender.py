import random
import names

# SOURCES
# https://en.wikipedia.org/wiki/LGBT_demographics_of_the_United_States
# https://www.kff.org/other/state-indicator/distribution-by-gender/?currentTimeframe=0&sortModel=%7B%22colId%22:%22Location%22,%22sort%22:%22asc%22%7D
# https://treyhunner.com/2013/02/random-name-generator/

# weighted based on presence in the U.S. population
genders = {1: {'name': 'Male',
               'weighting': 48},
           2: {'name': 'Female',
               'weighting': 50},
           3: {'name': 'Other',
               'weighting': 2}}

# ids are ints
gender_ids = list(genders.keys())

# names as strs
gender_names = [g['name'] for g in genders.values()]

# weights as ints
gender_weights = [g['weighting'] for g in genders.values()]

# keys as ids and values are names
gender_name_by_id = {k:v['name'] for (k,v) in genders.items()}

# generate a gender for a person
def random_gender_id():
    return random.choices(gender_ids, weights=gender_weights)[0]

# generate a name based on gender of person
def random_gender_name(ID):
    if ID == 1:
        return names.get_full_name(gender='male')
    elif ID == 2:
        return names.get_full_name(gender='female')
    else:
        return names.get_full_name()
