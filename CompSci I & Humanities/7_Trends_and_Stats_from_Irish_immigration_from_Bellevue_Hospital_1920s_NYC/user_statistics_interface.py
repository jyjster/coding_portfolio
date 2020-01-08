'''
This program creates, formats, and prints the stats I've chosen to track.

Program File: 03/03
      
This program is for Hw07, Dictionaries & Cleaning Data

Last modified: 04/21/19
By: Jordan Jackson
'''

'''
EXPLANATION OF STATS I CHOSE TO TRACK
# at the top of your code, you should type out an explanation about your chosen
# statistics, why you chose them, and some analysis about the results.

    # 4: George W. Anderson's ratio of patients sent to each site
    # 5: Moses G. Leonard's ratio of patients sent to each site
It seems that explicit powers each admittor has is to diagnosis each emigrant and 
decide where the individual will be sent. As the required statistics already 
covered admittor diagnoses decisions, I wanted to look into their facility
assignment decisions. 

Admittor Moses G. Leonard sent all of his patients to the
Long Island site, which had the following description according to the 
site_description dataset from the Bellevue Alms House Dataset, 
"The Care of Destitute, Neglected and Delinquent Children." Admittor George W.
Anderson sent overwhelming majority to Bellevue Complex site, which housed a
variety of different intstitution types. Bellevue Complex may have been catch-all
site for diagnoses.

   # 6: The distribution of diagnoses by patient sites
According to http://crdh.rrchnm.org/essays/v01-10-(re)-humanizing-data/ , a 
given site could have multiple institution-types (e.g. a chapel). I was 
curious which sites 'housed' emigrants of what diagnoses. Such statistics may 
give insight into the cultural/associated assumptions (specifically, of the
admittors) of how to address each given diagnosis.

An overwhelming majority of emigrants sent to the Lunatic Asylum were diagnosed
as 'insane.' While this association may seem reasonable, we cannot assume this
diagnosis was accurately diagnosed for we do not know what did the admittors
or society deemed 'insane' at the time. Bellevue Complex housed the greatest
variety/number of diagnoses, perhaps confirming that Bellevue Complex was in
fact a catch-all for diagnoses because it had various types of insitutions
at the site.


'''

### IMPORT STATEMENTS ###

import read_tsv_file
import csv
import stat_dicts


### FUNCTION DEFINITIONS ###

def print_diagnoses_stat_ratio_d(stat_d):
  
    '''
    This function prints the statistics for option 3 (comparison of illnesses 
    diagnosed to each gender) in a table format. 
        Columns: diagnosis name, female %, and male %
    
    Input parameters:
    stat_d: dictionary where keys are diagnosis names and values are nested
            dictionaries containing values corresponding to 
            ['female_ratio'] and ['male_ratio']
    
    Return value:
    site_by_diagnosis_d: dict, with site_name as keys and values are a 
                         nested dictionary tracking the number of patients at a
                         particular site with each diagnosis
    '''    
    dash_line = '-' * 36
    
    print('DIAGNOSES BY GENDER')
    print()
    print(dash_line)
    print('{:<22s}{:>7s}{:>7s}'.format('DIAGNOSIS',\
                                         'FEMALE', 'MALE'))
    print(dash_line)    
    for diagnosis, diagnosis_d in stat_d.items():
        print('{:<20s}{:>7d}%{:>7d}%'.format(diagnosis,\
                                             diagnosis_d['female_ratio'],\
                                             diagnosis_d['male_ratio']))
    print(dash_line)
    print()

def print_stat_ratio(stat_ratio_d):
    '''
    This function iterates over a dictionary's (stat_ratio_d) key, value pairs so
    that each pair is printed with a formatted representation.
    
    Input parameters:
    stat_ratio_d: dictionary with values as ratios representating percentages
 
    Return value: None
    '''
    
    for key, ratio in stat_ratio_d.items():
        print("\t{:<20s}{:>7.1f} %".format(key, ratio))

# Not specific to any dictionary or statistic option
def stat_d_to_stat_ratio_d(stat_d):
    
    '''
    This function takes a dictionary of counts to return a dictionary 
    of percentages.
    
    Input parameters:
    stat_d: dictionary with values of counts
    
    Return value: 
    return stat_ratio_d:dictionary with values of ratios
    '''

    counts_L = list(stat_d.values())
    total_count = sum(counts_L)
    
    stat_ratio_d = dict()
    for name, count in stat_d.items():
        
        # don't include key if it's value = 0
            # any key in input_d with non-zero value will be a key in the output_d
        
        if count != 0:
            stat_ratio_d[name] = round(count / total_count * 100, 1)
            
    return stat_ratio_d

def site_by_diagnosis_to_ratio(site_by_diagnosis_data_d):
    
    '''
    This function creates the dictionary for statistic option 6 (the distribution of 
    diagnoses by patient sites). This function takes a dictionary with 
    patient counts as values to ratios representing percentages.
    
    Input parameters:
    site_by_diagnosis_data_d: dictionary, key: site name, value: nested dictionary 
                         with each key as diagnosis and value as the number of
                         patients sent to that site
    
    Return value:
    site_by_diagnosis_d: dictionary, key: site name, value: nested dictionary 
                         with each key as diagnosis and value as ratio of 
                         patients diagnosed to number of patients sent to that site
    '''
    
    site_by_diagnosis_d = dict()
    for site_name, diagnosis_d in site_by_diagnosis_data_d.items():
        site_by_diagnosis_d[site_name] = stat_d_to_stat_ratio_d(diagnosis_d)
        
    return site_by_diagnosis_d


def print_site_by_diagnosis(site_by_diagnosis_d):
    
    '''
    This function prints the statistics for option 6 (the distribution of 
    diagnoses by patient sites).
    
    Input parameters:
    site_by_diagnoses_d: dictionary, key: site name, value: nested dictionary 
                         with each key as diagnosis and value as ratio of 
                         patients diagnosed to number of patients sent to that site
    
    Return value: None
    '''
    
    print('DISTRIBUTION OF DIAGNOSES PER SITE')
    print()
    for site_name, diagnosis_d in site_by_diagnosis_d.items():
        if diagnosis_d != {}:
            print('Site: {}'.format(site_name))
            print_stat_ratio(diagnosis_d)
            print()
        

def print_site_ratio_output(admittors_d, admittor_code):
    
    '''
    This function prints the statistics for option 4 or option 5 (for a 
    given admittor, ratio of patients sent to each site).
    
    Input parameters:
    admittors_d: dictionary, key: admittor, value: nested dictionary storing 
                                  data about that admittor
            
    admittor_code: string of numerical characters
    
    Return value: None
    '''
    
    # string
    admittor_name = admittors_d[admittor_code]['full_name']
    # integer
    total_patient_count = admittors_d[admittor_code]['patient_count']
    
    stat_ratio_d = stat_d_to_stat_ratio_d\
        (admittors_d[admittor_code]['facility_stats'])
    
    print('SITE STATISTICS FOR ADMITTOR {}:'.format(admittor_name))
    print()
    print('Ratio of patients sent to:\n')
    print_stat_ratio(stat_ratio_d)
    print()    


def print_admittor_to_diagnoses(admittors_d, admittor_code):
    
    '''
    This function prints the statistics for option 1 or option 2 (for a 
    given admittor, total patients and the ratio of the diagnoses given).
    
    Input parameters:
    admittors_d: dictionary, key: admittor, value: nested dictionary storing 
                                  data about that admittor
            
    admittor_code: string of numerical characters
    
    Return value: None
    '''
    
    # string
    admittor_name = admittors_d[admittor_code]['full_name']
    
    # integer
    patient_count = admittors_d[admittor_code]['patient_count']
    
    stat_ratio_d = stat_d_to_stat_ratio_d\
        (admittors_d[admittor_code]['disease_stats'])
    
    print('DIAGNOSIS STATISTICS FOR ADMITTOR {}:'.format(admittor_name))
    print()
    print('Total Patients: {}'.format(patient_count))
    print()
    print('Ratio of diagnoses given:\n')
    print_stat_ratio(stat_ratio_d)
    print()


def ask_file_name():
    
    '''
    This function asks the user the file name of the tsv file containing the
    dataset that the statistics will be based upon.
    
    Input parameters: None
 
    Return value: 
    file_name: string
    '''
    
    file_name = input('Enter data file name => ').strip()
    file_name += '.tsv'
    return file_name
    
def print_user_options():
    
    '''
    This function prints the statistic options the user may view, asks
    the user which statistic to view, then returns the number 
    corresponding to the chosen statistic option.
    
    Input parameters: None
    
    Return value: 
    stat_to_view: integer from 1-6
    '''
    
    print()
    print('With the Bellevue data, these are the three things chosen to track:\n')
    print("\t1: George W. Anderson's total patients and the ratio of the diagnoses given\n")
    print("\t2: Moses G. Leonard's total patients and the ratio of the diagnoses given\n")
    print("\t3: The comparison of illnesses diagnosed to each gender\n")
    print("\t4: George W. Anderson's ratio of patients sent to each site\n")
    print("\t5: Moses G. Leonard's ratio of patients sent to each site\n")
    print("\t6: The distribution of diagnoses by patient sites\n")
    
    stat_to_view = input('What would you like to view? ').strip()
    stat_to_view = int(stat_to_view)
    
    # Correct user's input
        # Keep asking question until valid user input
    while stat_to_view not in (1, 2, 3, 4, 5, 6):
        stat_to_view = input('What would you like to view? ').strip()
        stat_to_view = int(stat_to_view)
    
    return stat_to_view

        
### PROGRAM STARTS HERE ###

file_name = ask_file_name()

'''
file names:
    
Bellevue_1k
Bellevue_2.5k
Bellevue_5k
Bellevue_Full
'''

stat_id = print_user_options()

# Create dictionaries that statistics will be based upon
data_L = read_tsv_file.read_data(file_name)

emigrants_d = stat_dicts.make_emigrants_d(data_L)

admittors_d = stat_dicts.make_admittors_d(data_L)

diagnoses_data_d = stat_dicts.make_diagnoses_d(data_L, emigrants_d)
diagnoses_d = stat_dicts.stat_to_stat_ratio_diagnoses_d(diagnoses_data_d)

site_by_diagnosis_data_d = (stat_dicts.make_site_by_diagnosis(emigrants_d, data_L))
site_by_diagnosis_d = site_by_diagnosis_to_ratio(site_by_diagnosis_data_d)

print()

# Return statistic results
    # G.W. Anderson's admittor_code = 48
    # M. G. Leonard's admittor_code = 87

if stat_id == 1:
    print_admittor_to_diagnoses(admittors_d, '48')
elif stat_id == 2:
    print_admittor_to_diagnoses(admittors_d, '87')
    
elif stat_id == 3:
    print_diagnoses_stat_ratio_d(diagnoses_d)
    
elif stat_id == 4:
    print_site_ratio_output(admittors_d, '48')
elif stat_id == 5:
    print_site_ratio_output(admittors_d, '87')
    
elif stat_id == 6:
    print_site_by_diagnosis(site_by_diagnosis_d)












#######
##  The rest of this code was written to test the code and then
##  commented out.
#######
    
# file_name = 'Bellevue_1k'
# file_name += '.tsv'

# TEST # master_L (AKA data_L)
    # print(master_L)
    
    # stat_dicts.pprint_dict(data_L)
    
# TEST # dianoses_d
    
    # diagnoses_data_d = stat_dicts.make_diagnoses_d(data_L, emigrants_d)
    # diagnoses_d = stat_dicts.stat_to_stat_ratio_diagnoses_d(diagnoses_data_d)
    
    # stat_dicts.pprint_dict(diagnoses_d)
    # stat_dicts.pprint_dict(stat_dicts.stat_to_stat_ratio_diagnoses_d(diagnoses_d))
    
# TEST # stat_dicts.stat_to_stat_ratio_diagnoses_d()
    # diagnoses_d = stat_dicts.stat_to_stat_ratio_diagnoses_d(diagnoses_data_d)
    # stat_dicts.pprint_dict(stat_dicts.stat_to_stat_ratio_diagnoses_d(diagnoses_d))
    
# TEST # print_diagnoses_stat_ratio_d()
    # print_diagnoses_stat_ratio_d(diagnoses_d)
    
# TEST # emigrants_d
    # print(emigrants_d)
    # stat_dicts.pprint_dict(emigrants_d)
    
# TEST # make_site_by_diagnosis()
    # site_by_diagnosis_data_d = (stat_dicts.make_site_by_diagnosis(emigrants_d, data_L))
        
# TEST # stat_d_to_stat_ratio_d()
    # site_by_diagnosis_d = stat_d_to_stat_ratio_d(site_by_diagnosis_data_d)
    
    # stat_ratio_1 = stat_d_to_stat_ratio_d(admittors_d['48']['disease_stats'])
    # print(stat_1)
    # stat_dicts.pprint_dict(stat_1)
    # stat_ratio_2 = stat_d_to_stat_ratio_d(admittors_d['87']['disease_stats'])
    # print(stat_2)
    # stat_dicts.pprint_dict(stat_2)    
        
# TEST # site_by_diagnosis_to_ratio()
    # site_by_diagnosis_d = site_by_diagnosis_to_ratio(site_by_diagnosis_data_d)
    
# TEST # site_by_diagnosis_d
    # stat_dicts.pprint_dict(site_by_diagnosis_d)
    
# TEST # stat_dicts.make_admittors_d()
    # admittors_d = stat_dicts.make_admittors_d(data_L)
    # print(admittors_d)

# TEST # admittors_d
    # stat_dicts.pprint_dict(admittors_d)
    
    # admittors_d[admittor_code][stats_d]
    # print(admittors_d[48])

# TEST Stats # 

        # G.W. Anderson's admittor_code = 48
        # M. G. Leonard's admittor_code = 87

    # TEST # print_admittor_to_diagnoses()
        # print_admittor_to_diagnoses(admittors_d, '48')
        # print_admittor_to_diagnoses(admittors_d, '87')

    # TEST # print_site_ratio_output()  
        # print_site_ratio_output(admittors_d, '48')
        # print_site_ratio_output(admittors_d, '87')
    
    # print_selected_stat(stat_id)
