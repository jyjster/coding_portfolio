import random

# SOURCES
# https://www.census.gov/topics/population/race/about.html
# https://en.wikipedia.org/wiki/Race_and_ethnicity_in_the_United_States#cite_note-c2010-12

# weighted based on presence in the U.S. population
races = {1: {'name': "White",
             'weighting': 72.4},
         2: {'name': "Black or African American",
             'weighting': 12.6},
         3: {'name': "American Indian or Alaska Native",
             'weighting': 0.9},
         4: {'name': "Asian" ,
             'weighting': 4.8},
         5: {'name': "Native Hawaiian or Other Pacific Islander",
             'weighting': 0.2},
         6: {'name': "Two or More",
             'weighting': 2.9},
         7: {'name': "Other",
             'weighting': 6.2}}

# ids are ints
race_ids = list(races.keys())

# names as strs
race_names = [r['name'] for r in races.values()]

# weights as floats
race_weights = [r['weighting'] for r in races.values()]

# keys as ids and values are names
# use if need to translate id to name
race_name_by_id = {k:v['name'] for (k,v) in races.items()}

# generate a race for a person
def random_race_id():
    return random.choices(race_ids, weights=race_weights)[0]


