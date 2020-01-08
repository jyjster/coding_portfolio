'''
This program stores the read-in data in proper entries in nested dictionaries. 

There are four dictionaries: two main dictionaries: 
    one for Admittors (admittors_d) and 
    one for Emigrants (emigrants_d), and 
two dictionaries that use the prior two dictionaries:
    one for diagnoses by gender (diagnoses_d) and 
    one for 'sent-to' sites by diagnosis (site_by_diagnosis_d).

Program File: 02/03
* Required Files (x2):
      'ID_to_Admittors.tsv'
      'ID_to_site.tsv'
      
This program is for Hw07, Dictionaries & Cleaning Data

Last modified: 04/21/19
By: Jordan Jackson
'''

### IMPORT STATEMENTS ###

import read_tsv_file
import csv
import pprint
import numbers


### FUNCTION DEFINITIONS ###

# pretty printer for dictionary data structures using pprint module
def pprint_dict(d):
    
    '''
    This function formats and represents dictionary data structures by breaking
    them onto multiple lines the dictionary is sorted by each key. This function
    constructs a PrettyPrinter instance for the pprint class.
    
    
    Input parameters:
    d: dictionary
    
    Return value: None
    prints formatted dictionary 'd'
    
    '''
    # Construct a PrettyPrinter instance
        # Use additional parameter with keyword 'indent' to control
            # the formatted representation
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(d)
    
    
def find_all_possibilities(key_of_interest, L):
    
    '''
    This function finds all possible unqiue values for a given key in 
    a list of dictionaries (master_L).
    
    Input parameters:
    key_of_interest: str, name of key in nested patient_d in master_L to    
                     find all possible unqiue values for
    L: list, master_L
    
    Return value: 
    list: list of unique values for key_of_interest 
    '''    
    
    possibilities_L = []
    
    for patient_d in L:
        value_of_interest = patient_d[key_of_interest]
        if value_of_interest in possibilities_L:
            continue
        # Exclude values of empty strings
        elif value_of_interest == '':
            continue
        else:
            possibilities_L.append(value_of_interest)
    
    return list(set(possibilities_L))

def initialize_d_numbs(possibilities_L):
    
    '''
    This function intializes a dictionary with values of 0, given 
    a list of its keys.
    
    Input parameters:
    possibilities_L: list of strings 
 
    
    Return value: 
    dictionary: dict, an intialized dictionary where each string element of 
                possibilities_L is a key with an initialized value of 0
    '''        
    
    dictionary = dict()
    
    for option in possibilities_L:
        dictionary[option] = 0
        
    return dictionary


def make_admittors_decoded_d(file):
    
    '''
    This function creates dictionary with keys of admittor_id's and 
    values of admittor_name's based on the Bellevue Alms House Dataset's
    'Admittors' dataset, renamed to''ID_to_Admittors.tsv'.
    
    Input parameters:
    file: string of file name, including file extension
 
    
    Return value: 
    master_d: dict, keys are admittor_id's and values are admittor_name's
    '''    
    master_d = dict()
    
    with open(file, mode='r') as csv_file:
        tsv_reader = csv.DictReader(csv_file, delimiter='\t')
        for row in tsv_reader:
            row_d = dict(row)
            master_d[row_d['admittor_code']] = \
                row_d['admittors_from_almshouse_register'].title()
    
    return master_d

def clean_site_code(string):
    
    '''
    This function removes any spaces from a site_code string. This 'cleaning' is
    necessary so the site_codes match the format of the site_codes in 
    'ID_to_site.tsv' so the site_codes can later be translates into their site_names.
    
    Input parameters:
    string: string
 
    
    Return value: 
    cleaned_s: string with spaces removed
    '''
    
    cleaned_s = string.replace(' ','')
    
    return cleaned_s    
    
def make_site_decoded_d(file):
    
    '''
    This function creates dictionary with keys of site_code's and 
    values of site_name's based on the Bellevue Alms House Dataset's
    'site_codes' dataset, renamed to''ID_to_sites.tsv'.
    
    Input parameters:
    file: string of file name, including file extension
 
    Return value: 
    master_d: dict,where keys are site code's and values are site name's
    '''    
    
    master_d = dict()
    
    
    with open(file, mode='r') as csv_file:
        tsv_reader = csv.DictReader(csv_file, delimiter='\t')
        for row in tsv_reader:
            row_d = dict(row)
            
            new_key = row_d['almshouse_register_site_code']
            new_key = clean_site_code(new_key)
            
            if row_d['site_general'] == '':
                master_d[new_key] = 'unspecified'
            else:
                master_d[new_key] = row_d['site_general'].title()
        
    return master_d

def translate_emigrant_site_code(code_d, emigrantS_d):
    '''
    This function translates the site codes to site names in the main emigrants_d.
    In other words, this function translates site codes into their more 
    understandable names using the site_codes file, renamed to 'ID_to_site.tsv',
    from the Bellevue Alms House Dataset.
    
    Input parameters:
    code_d : dict, keys are side codes and values are site names
    emigrantS_d: dict, keys are admission code, values are a nested dictionary,
                 site codes as value of ['site_code'] in 
                 nested dictionary (emigrant_d)
    
    Return value:
    emigrantS_d: dict, with key, value pair of ['site_name'] : site name in
                 nested dictionary emigrant_d
    '''    
    
    # for emigrant_d in emigrantS_d:
    for admission_code, emigrant_d in emigrantS_d.items():
        
        site_code = emigrant_d['site_edited']
        
        # goal: ['site_code'] value --> ['site_name'] value
        if site_code in code_d:
            emigrant_d['site_name'] = code_d[site_code]
        else:
            emigrant_d['site_name'] = 'unspecified'
        
    return emigrantS_d


def make_emigrants_d(master_L):
    
    '''
    This function creates the main emigrants dictionary (emigrants_d).
    
    Input parameters:
    master_L : list of nested dictionaries
    
    Return value:
    emigrants_d : dictionary tracking each emigrant's admission id,
                  full name, diagnosis, and what location they were
                  sent to, and their gender
                  
                  { admission_id : {'full_name' : _____,  
                                    'diagnosis_edited' : _____, 
                                    'site_edited' : _____ , 
                                    'gender': _____, 
                                    'admission_id' : _____} }
    '''

    dictionary = dict()
    for patient_d in master_L:
        patient_ID = patient_d['admission_id']
        dictionary[patient_ID] = {'admission_id': patient_ID, \
                                  'full_name':patient_d['full_name'],\
                                  'diagnosis_edited':patient_d['diagnosis_edited'],\
                                  'site_edited':patient_d['site_edited'],\
                                  'gender':patient_d['gender']}
        
    site_name_by_id = make_site_decoded_d('ID_to_site.tsv')
    emigrants_d = translate_emigrant_site_code(site_name_by_id, dictionary)
    return emigrants_d

def translate_admittor_site_code(code_d, admittorS_d):
    '''
    This function translates the site code keys to site name keys in the 
    main admittors_d's nested ['facility_stats] dictionaries.
    
    Input parameters:
    code_d : dict, keys are side codes and values are site names
    admittorS_d: dict, keys are admittor code, values are a nested dictionary,
                 site codes as value of ['site_code'] in 
                 nested dictionary (emigrant_d)
    
    Return value:
    admittorS_d: dict, translated dict version with site name as keys in 
                 ['facility_stats'] nested dictionaries
    '''    
    
    # for admittor_d in admittorS_d:
    for admittor_code, admittor_d in admittorS_d.items():
        
        new_facility_d = dict()
        
        # for nested facility_stats dictionary in admittor_d
        for site_code, count in admittor_d['facility_stats'].items():
            if site_code in code_d:
                new_facility_d[code_d[site_code]] = count
            else:
                new_key = 'unspecified'
                
                # if statement tests if count is intialized
                
                # case: unspecified isn't an existing key
                if new_key not in new_facility_d:
                    new_facility_d[new_key] = 0
                # case: unspecified is an existing key
                elif not isinstance(new_facility_d[new_key], numbers.Number):
                    new_facility_d[new_key] = 0
                    
                new_facility_d[new_key] += count
        
        admittor_d['facility_stats'] = new_facility_d
        
    return admittorS_d


def make_admittors_d(master_L):
    
    '''
    This function creates the main admittors dictionary (admittors_d).
    
    Input parameters:
    master_L : list of nested dictionaries
    
    Return value:
    admittors_d : dictionary tracking each admittors's code, name,
                  number of patients, facility stats (how many emigrants they 
                  sent to each facility), and disease stats (how many emigrants
                  they diagnosed with each condition)
                  
                  { admittor_code : {'patient_count' : _____, 
                                     'facility_stats' : {} , 
                                     'disease_stats': {} , 
                                     'admittor_code' : _____
                                     'full_name' : _____} }
    '''
    
    admittors_d = dict()
    
    possible_admittors_L = find_all_possibilities('admittor_1_code', master_L) + \
        find_all_possibilities('admittor_2_code', master_L)
    
    possible_admittors_L = list(set(possible_admittors_L))
    
    admittor_name_by_id = make_admittors_decoded_d('ID_to_Admittors.tsv')
    
    for admittor_code in possible_admittors_L:
        
        # { admittor_1 : {}, admitor_2:, {}, ...}
        admittors_d[admittor_code] = dict()
        
        # { admittor_code : { 'admittor_code' : admittor_code} }
        admittors_d[admittor_code]['admittor_code'] = admittor_code
        
        admittor_name = admittor_name_by_id[admittor_code]
        
        # One admittor_name is [Blank]. I kept this way because only 1 of 
            # them in 'Bellevue_Full.tsv' has this "name"
            
        admittors_d[admittor_code]['full_name'] = admittor_name
        # given code, look up in original 
        
        admittors_d[admittor_code]['facility_stats'] = dict()
        
        # { admittor_code : { 'full_name' : admittor_name, 'patient_count' : 0, 'facility_stats' : {facility_a : 0, facility_b : 0, facility_c : 0} }
        admittors_d[admittor_code]['facility_stats'] = initialize_d_numbs(find_all_possibilities('site_edited', master_L))
        
        admittors_d[admittor_code]['disease_stats'] = dict()

        admittors_d[admittor_code]['disease_stats'] = initialize_d_numbs(find_all_possibilities('diagnosis_edited', master_L))        
            
        admittors_d[admittor_code]['patient_count'] = 0

    
    for patient_d in master_L:
        
        patient_disease = patient_d['diagnosis_edited']
        
        patient_facility = patient_d['site_edited']
   
        # for each patient, there is a maximum of two admittor_code's
        for admittor in (patient_d['admittor_1_code'], patient_d['admittor_2_code']):
            # if there is a listed admittor
            if admittor != '':
                
                admittors_d[admittor]['patient_count'] += 1
                
                # and if there is a listed facility
                if patient_facility != '':
                    
                    admittors_d[admittor]['facility_stats'][patient_facility] += 1
                    
                # and if there is a listed facility
                if patient_disease != '':
                    
                    admittors_d[admittor]['disease_stats'][patient_disease] += 1
                    
    site_name_by_id = make_site_decoded_d('ID_to_site.tsv')
    
    admittors_d = translate_admittor_site_code(site_name_by_id, admittors_d)

    return admittors_d


def make_diagnoses_d (master_L, emigrantS_d):
    
    '''
    This function creates the main admittors dictionary (admittors_d).
    
    Input parameters:
    master_L : list of nested dictionaries
    emigrantS_d: the main emigrants dictionary
    
    Return value:
    diagnoses_d : dictionary for each diagnosis key, there is a value 
                  consisting of a nested dictionary storing the total number of
                  patients diagnosed with that condition, the number of females
                  diagnosed with this condition, and the number of males diagnosed
                  with this condition.
                  
                  { emigrant_diagnosis : {'patient_count' : _____, 
                                          'female_count' : _____ , 
                                         'male_count': _____ }
    '''
    
    diagnoses_d = dict()
    
    possible_diagnoses_L = find_all_possibilities('diagnosis_edited', master_L)
    for diagnosis in possible_diagnoses_L:
        diagnoses_d[diagnosis] = {'patient_count': 0, 'female_count': 0, 'male_count': 0}
     
    for admission_id, emigrant_d in emigrantS_d.items():
        # emigrantS_d = { id:{}, id:{}, ...}
        
        emigrant_diagnosis = emigrant_d['diagnosis_edited']
        diagnoses_d[emigrant_diagnosis]['patient_count'] += 1
        
        if emigrant_d['gender'] == 'female':
            diagnoses_d[emigrant_diagnosis]['female_count'] += 1
        elif emigrant_d['gender'] == 'male':
            diagnoses_d[emigrant_diagnosis]['male_count'] += 1
        else:
            continue

    return diagnoses_d

# WORKING # 
def stat_to_stat_ratio_diagnoses_d(stat_d):
    
    '''
    Takes a dictionary with values corresponding to patient counts and returns a
    dictionary with values corresponding to a percentage.
    
    Input parameters:
    stat_d : dictionary with diagnosis as key and values containing the 
             total patient count and the the count of males and females 
             with that diagnosis
    
    Return value:
    stat_ratio_d: dictionary containing the percentage of male vs. female 
                  patients with that diagnosis
                  
                  percentage value is calculated by 
                  round(gender_count / patient_count * 100, 2)
   '''
    
    
    stat_ratio_d = dict()
    
    for diagnosis_name, diagnosis_d in stat_d.items():
        
        female_fract = diagnosis_d['female_count'] / diagnosis_d['patient_count']
        male_fract = diagnosis_d['male_count'] / diagnosis_d['patient_count']
        
        female_ratio = round(female_fract * 100, 0)
        female_ratio = int(female_ratio)
        
        male_ratio = round(male_fract * 100, 0)
        male_ratio = int(male_ratio)       
        
        stat_ratio_d[diagnosis_name] =  {'female_ratio':female_ratio, 'male_ratio' : male_ratio}
  
    return stat_ratio_d
        

def make_site_by_diagnosis(emigrantS_d, master_L):
    
    '''
    This function creates the site_by_diagnosis_d for the statistic on 
    the distribution of diagnoses by patient sites.
    
    Input parameters:
    master_L: list of dictionaries with nested dictionaries
    emigrantS_d: the main emigrants_d
    
    Return value:
    site_by_diagnosis_d: dict, with site_name as keys and values are a 
                         nested dictionary tracking the number of patients at a
                         particular site with each diagnosis
    '''
    
    site_name_by_id = make_site_decoded_d('ID_to_site.tsv')
    
    # intialize
    site_by_diagnosis_d = dict()
    possible_sites_s = set(site_name_by_id.values())
    for site in possible_sites_s:
        site_by_diagnosis_d[site] = initialize_d_numbs(find_all_possibilities\
                                                       ('diagnosis_edited', master_L))
        
    for admission_id, emigrant_d in emigrantS_d.items():
        patient_disease = emigrant_d['diagnosis_edited']
        patient_site = emigrant_d['site_name']
        
        site_by_diagnosis_d[patient_site][patient_disease] += 1
    
    return site_by_diagnosis_d










#######
##  The rest of this code was written to test the code and then
##  commented out.
#######

        
# TEST # make_site_by_diagnosis()
    # pprint_dict(site_by_diagnosis_d)

# TEST # translate_emigrant_site_code()
    # pprint_dict(admittorS_d)
    
    # pprint_dict(emigrantS_d)
    
# TEST # translate_admittor_site_code()
    # pprint_dict(admittorS_d)

# TEST # make_emigrants_d()
    # emigrants_d = make_emigrants_d(data_L)
    
    # print(emigrants_d)
    
    # pprint_dict(emigrants_d)

# TEST # make_admittors_d()

    # admittors_d = make_admittors_d(data_L)
    
    # print(admittors_d)
    
    # pprint_dict(admittors_d)

    # print(possible_admittors_L)
    # print(find_all_possibilities('site_edited', master_L)) 
    # print(admittors_d)
    # print(patient_disease)
    # print(patient_facility)
    # print(admittor)
    # print('incrementing facility')
    # print('incrementing disease')
    # print(admittors_d)
    # pprint_dict(admittors_d)
    # pprint_dict(admittors_d)
    # pprint_dict(site_name_by_id)
     
# TEST # make_diagnoses_d()
    # print(emigrant)
    
# TEST # make_admittors_decoded_d()
    # print(make_admittors_decoded_d('ID_to_Admittors.tsv'))
    # admittor_name_by_id = make_admittors_decoded_d('ID_to_Admittors.tsv')
    
# TEST # make_site_decoded_d
    # site_name_by_id = make_site_decoded_d('ID_to_site.tsv')
    # print(site_name_by_id)

# TEST # data from 'read_tsv_file.py'
    # file_name = input('Enter file name => ').strip()

    # file names: Bellevue_1k, Bellevue_2.5k, Bellevue_5k, Bellevue_Full
    # file_name = 'Bellevue_1k'
    # file_name = 'Bellevue_2.5k'

    # file_name += '.tsv'

    # data_L = read_tsv_file.read_data(file_name)
    # print(master_L)

    # print(L)
    # print(L[0])
