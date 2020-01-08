'''
This program reads in a data set on Irish immigration from Bellevue Hospital in
1920s New York City and parses the data into a list of dictionaries.

Program File: 01/03
This program is for Hw07, Dictionaries & Cleaning Data

Last modified: 04/20/19
By: Jordan Jackson
'''

### IMPORT STATEMENTS ###

import csv
import re

### FUNCTION DEFINITIONS ###

def translate_gender(gender_s):
    
    '''
    This function changes dictionary value of 'f' to 'female' or of 'm' to 'male'.
    
    Input parameters:
    gender_s: string, the dictionary value of the key 'gender'
    
    Return value:
    translated_d: string, translated version
    '''
    
    if gender_s == 'f':
        translated_s = "female"
    elif gender_s == 'm':
        translated_s = "male"
    else:
        translated_s = gender_s
        
    return translated_s


def translate_name(name_s):
    
    '''
    This function mutates a string so the first letter of every letter
    is an uppercase letter.
    
    Input parameters:
    string
    
    Return value:
    string, with string.title() capitalization
    '''
    
    return name_s.title()
    
    
def clean_site_code(string):
    
    '''
    This function 'cleans' the site codes by removing any spaces.
    
    Input parameters:
    string: string, the dictionary value of the key 'gender'
    
    Return value:
    cleaned_s: string, 'cleaner' version without spaces
    '''    
    
    cleaned_s = string.replace(' ','')
    
    return cleaned_s

def clean_s(string):
    '''
    This function 'cleans' a string by removing extraneous characters 
    that don't make sense.
    
    Input parameters:
    string
    
    Return value:
    cleaned_s: string, translated version
    '''
    
    # Eliminate any extraneous characters from a single word using re import
    # Allow any alphanumerical characters, spaces, periods (.), apostrophe's ('), 
       # parentheses, question marks (?), forward (\) and black (/) slashes, and dashes (-)
       # For example, '[blank]' would become 'blank'.
       
    regex = re.compile("[^a-zA-Z0-9 .'(?)\/-]")
    cleaned_s = regex.sub('', string)
    
    return cleaned_s


def clean_d(dictionary):
    
    '''
    This function takes in a dictionary of data (from when the data was read in) 
    and returns a dictionary with translated and 'cleaned' keys and values.
    
    Input parameters:
    dictionary: dict, with keys matching the column titles and the values of 
                the read-in .tsv file
    
    Return value:
    cleaned_d: dict, translated and 'cleaner' version
    '''    
    
    cleaned_d = {}
    
    # iterate over the key, value pairs in dictionary to create 
        # a 'cleaner' version of it ('cleaned_d')
        
    for key, value in dictionary.items():
        
        cleaned_key = key.lower()
        
        # 'clean' the values via clean_s() in cleaned_d dictiionary
        cleaned_d[cleaned_key] = clean_s(dictionary[key])
        
        # copy dictionary's ['gender'] values to cleaned_d's, but 
            # change the single letters to full words via translate_gender()
        if key == 'gender':
            cleaned_d[cleaned_key] = translate_gender(cleaned_d[cleaned_key])
            
        # apply .title() capitalization to thew value of fields representing a person's name
        elif key == 'full_name' or key == 'first_name' or key == 'last_name':
            cleaned_d[cleaned_key] = translate_name(cleaned_d[cleaned_key])
            
        # in cleaned_d, change any of dictionary's values that include 'blank' or 
            # are an empty string to be 'unspecified'
        if cleaned_d[cleaned_key] == 'blank':
            cleaned_d[cleaned_key] = 'unspecified'
        elif cleaned_d[cleaned_key] == '':
            cleaned_d[cleaned_key] = 'unspecified'
            
        # for cleaned_d, change any of dictionary's values containing 'illegible' 
            # to being just 'illegible'
        if 'illegible' in cleaned_d[cleaned_key]:
            cleaned_d[cleaned_key] = 'illegible'
            
        # remove any spaces for cleaned_d's ['sent_to_cleaned'] values
        if cleaned_key == 'sent_to_cleaned' and cleaned_d[cleaned_key] != 'unspecified':
            cleaned_d[cleaned_key] = clean_site_code(cleaned_d[cleaned_key])
    

    return cleaned_d


def translate_keys(dictionary):
    
    '''
    This function changes the names of a dictionary's keys from the column
    titles from the read-in .tsv file.
    
    Input parameters:
    dictionary: dict, with keys matching the column titles the read-in .tsv file
    
    Return value:
    dictionary: a mutated dict, with translated key names
    '''
    
    dictionary['diagnosis'] = dictionary.pop('disease')
    dictionary['diagnosis_edited'] = dictionary.pop('disease_control')
    dictionary['occupation'] = dictionary.pop('profession')
    dictionary['occupation_edited'] = dictionary.pop('profession_control')
    dictionary['site_edited'] = dictionary.pop('sent_to_cleaned')
    dictionary['site'] = dictionary.pop('sent_to')
    dictionary['child_edited'] = dictionary.pop('child_cleaned')
    
    return dictionary

def read_data(file):
    
    '''
    Given the file name (with its file extension), this function opens and reads
    the .tsv file into a list of translated and 'cleaned' dictionaries.
    
    Input parameters:
    file: string, the file name (with its file extension)
    
    Return value:
    master_L: list, list of dictionaries where 1 dictionary in the list 
            represents 1 row of data fromt the .tsv file
    '''
    
    master_L = []
    with open(file, mode='r') as csv_file:
        tsv_reader = csv.DictReader(csv_file, delimiter='\t')
        for row in tsv_reader:
            row_d = dict(row)
                
            # 'clean' and translate the original keys and values
            cleaned_d = clean_d(row_d)
            cleaned_d = translate_keys(cleaned_d)
            
            # after creating a dictionary from a row of data, append the dictionary
                # to master_L
            master_L.append(cleaned_d)
    
    return master_L











#######
##  The rest of this code was written to test the code and then
##  commented out.
#######
    
# TEST # master_L
    # print(L)
    # print(L[0])

# TEST # clean_s()
    # print(clean_s('[blank]47(?)'))
    
# TEST # clean_d()
    # print(cleaned_d[cleaned_key])

# TEST # read_data()
    # print(clean_d(master_L[0]))
    
    # write cleaned master_L output to a separate file
    # output_cleaned_L = open('test_funct-read_data.txt', "w")
    # for patient_d in master_L:
        # output_cleaned_L.write('{}\n\n\n'.format(patient_d))    
    # output_cleaned_L.write('{}'.format(master_L))
    
    # print(row_d)
    
    # import stat_dicts
    # stat_dicts.pprint_dict(row_d)




