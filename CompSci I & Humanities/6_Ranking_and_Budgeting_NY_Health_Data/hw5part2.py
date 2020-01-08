'''
This program should ask the user what budget they want to look at the statistics for, 
divide up the budget provided among the NY state counties, 
and then provide the statistics for what county gets what amount.

This program is for Hw05, Part 2: Ranking and Budgeting.

Last modified: 03/21/19
By: Jordan Jackson
'''

### IMPORT STATEMENTS ###


'''The utility module hw5_util.py provides a function read_deaths_all() 
that returns a tuple of 2 lists, 
a list of year numbers as strings and a list of lists of a county's name and its data points.'''

import hw5_util 

import statistics



### FUNCTION DEFINITIONS ###


def get_yr_data(all_data):
    
    '''
    This function reads in the death statistics, then returns a formatted 
    list of of county data lists with pertinent information. 
    
    Pertinent information per county includes ['county name', [ list of 3 numbers of rates for most recent 3 years ]]
    
    
    Input parameters:
    all_data: a tuple of 2 lists, 
              a list of year numbers as strings and 
              a list of lists of a county's name and its data points
    
    Return value:
    relevant_data: 1 list of c_data lists
    '''        
    
    relevant_data = []
    
    # There are 62 counties in NYS, but the data has extra columns tht are not valid counties
    invalid_counties = ["New York State", "New York City", "Grand Total", "Rest of State"]
    
    # for loop: iterates by county sublist in the second list in the tuple
    # EX: ['Albany', 956.2, 938.2, 954.6, 888.6, 887.7, 902.3, 864.9, 844.8, 888.4, 888.5, 853.6]
    for county in all_data[1]:
        
        # EX: 'Albany'
        c_name = county[0]
        
        # Get rid of invalid county names
        if c_name not in invalid_counties:
            c_data = []
            
            # Only include data values from 3 most recent years available in dataset
            # EX: [888.4, 888.5, 853.6]
            recent_3yrs = county[len(county)-3: len(county): 1]
            
            # EX: ['Albany', [888.4, 888.5, 853.6]]
            c_data = [c_name, recent_3yrs]
            
            relevant_data.append(c_data)
    
    return relevant_data


def get_avg_data(yr_data):
    
    '''
    This function computes the average death rate of the most recent 3 years of data per county,
    then returns a formatted list of of county data lists with pertinent information.
    
    Pertinent information per county includes ['county name', avg#]
    
    Input parameters:
    yr_data: a list of lists, the list returned from function get_yr_data()
             a list of lists of a county's name and its 3 most recent data points
    
    Return value:
    relevant_data: 1 list of c_data lists
             a list of lists of a county's name and its average numerical value
    '''            
    
    relevant_data = []
    
    # for loop: iterates by county sublist in yr_data list
    # EX: ['Albany', [888.4, 888.5, 853.6]]
    for county in yr_data:
        
        # EX: 'Albany'
        c_name = county[0]
        
        # EX: [888.4, 888.5, 853.6]
        c_yrs = county[1]
        
        # Compute average
        # EX: 876.8333333333334
        c_mean = statistics.mean(c_yrs)
        
        # Round: to 1 decimal place
        # EX: ['Albany', 876.8]
        c_data = [c_name, round(c_mean, 1)]
        
        relevant_data.append(c_data)
    
    return relevant_data


def get_cnames(L):

    '''
    This function returns a list of strings of valid counties in NYS 
    
    Input parameters:
    L: a list of lists, the list returned from function get_avg_data()
             a list of lists of a county's name and its average numerical value
    
    Return value:
    cnames: 1 list of strings of county names
             EX: ['county name', ''county name', ...]
    '''      
    
    cnames = []
    
    # for loop: iterates by county sublist in L list
    for county in L:
        c_name = county[0]
        cnames.append(c_name)
    
    # len(cnames) should == 62 if it only includes valid county names of NYS
    return cnames

# calculates the percent of part to whole
# porportion of money that county gets 
# highest statistics gets highest porportion

def sorting(L):
    
    '''
    This function:
    1) computes a ratio for each county based on
    a county's average death rate (of the most recent 3 years of data) 
         in relation to the sum (total) of all county average death rates
    
    ratio  =          avg. death rate for a specific county      = part
                 ______________________________________________   _____
                 
                      sum of all county avg. death rates          whole
                      
    This ratio will eventually be used in allocate_budget() to compute the money 
         a county is allotted. 
         
    2) Then returns a formatted list of of county data lists with pertinent information
         Pertinent information per county includes ['county name', ratio]                      
               
    Input parameters:
    L: a list of lists, the list returned from function get_avg_data()
             a list of lists of a county's name and its average numerical value
    
    Return value:
    relevant_data: 1 list of c_data lists
             a list of lists of a county's name and its ratio as a float
    '''                
   
    relevant_data = []
    total_avg = 0

    # Compute sum of county averages
    for county in L:
        c_avg = county[1]
        total_avg += c_avg

    # Compute ratio
        c_name = county[0]
        c_avg = county[1]
        
        c_ratio = c_avg / total_avg
        c_data = [c_name, c_ratio]
        
        relevant_data.append(c_data)
    
    return relevant_data


def allocate_budget (budget_total, base_allocation, L):
    
    '''
    This function computes the amount of money given to each county,
    then returns a formatted list of of county data lists with pertinent information.
    
    Pertinent information per county includes ['county name', float_$]
    
    Input parameters:
    budget_total: integer, amount of money in a particular NYS state budget 
    base_allocation: float, percent written in decimal form representing the 
         porportion of how much of budget_total is going to be split evenly, as opposed to
         how much of budget_total is distributed based on the porportion calcualated from get_ratio()
    L: a list of lists, the list returned from function get_ratio()
             a list of lists of a county's name and its ratio

    Return value:
    relevant_data: 1 list of c_data lists
             a list of lists of a county's name and its average numerical value
    '''   
    
    # Total amount of budget money that will be evenly distributed among counties
    budget_even = budget_total * base_allocation
    
    # Total amount of budget money that will be distributed based on porportion from get_ratio()
    budget_ratio = budget_total - budget_even
    
    relevant_data = []
    
    # Minimum amount of money that each county will recieve
    # len(L) == # of counties 
    c_budget_even = budget_even / len(L)
    
    for county in L:
        c_name = county[0]
        c_ratio = county[1]
        
        # Total amount of money a given county recieves in dollars
        c_budget = c_ratio * budget_ratio + c_budget_even
        
        # Total amount of money a given county recieves in millions of dollars
        c_budget_million = c_budget / 1000000
        
        c_data = [c_name, round(c_budget_million, 2)]
        
        relevant_data.append(c_data)
        
    return relevant_data


def print_c_budgets(title, L):
    
    '''
    This function formats and prints the statistics, from the budget the user requests to look at,
    for what county gets what amount
    
    Input parameters:
    title: string, header for statistics
    L: list of lists, the list returned from function allocate_budget()
             a list of lists of a county's name and its allotted money in the millions
    
    Return value:
    printed strings
    '''    
    
    print()
    print(title)
    for c in L:
        c_name = c[0]
        c_budget = c[1]
        print('{} : ${} million'.format(c_name, c_budget))
    
def get_avg_key(L):
    '''
    This key function returns a key parameter so a list will be sorted by its avg#
    
    Input parameters:
    L: a list of lists, the list returned from function get_avg_data(),
       a list of lists of a county's name and its average numerical value
       
    Return value: 
    key paramter for list.sort()
    '''
    return L[1]

def get_name_key(L):
    '''
    This key function returns a key parameter so a list will
    be alphabetically sorted by its county name
    
    Input parameters:
    L: a list of lists, the list returned from function allocate_budget()
       
    Return value: 
    key paramter for list.sort()
    '''    
    return L[0]    



### PROGRAM STARTS HERE ###

""" data format: ( ['2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', ''], 
                   [ ['Albany', 956.2, 938.2, ...],  ['Allegany', ...], ..., ['Grand Total', ...] ] ) """
all_data = hw5_util.read_deaths_all()

""" data format: [ ['Albany', [888.4, 888.5, 853.6]], ['Allegany', [994.3, 978.1, 958.2]],
                   ['Bronx', [639.8, ...], ..., ['Yates', [...] ] """
yr_data = get_yr_data(all_data)

""" data format: [ ['Albany', avg#], ..., ['Yates', avg#] ] """
avg_data = get_avg_data(yr_data)

# HEALTH INSURANCE

insurance_data = list(avg_data)

""" data format: [ ['Albany', c_ratio], ..., ['Yates', c_ratio] ] """
insurance_ratio = sorting(insurance_data)

insurance_budget = allocate_budget(71000000, 0.5, insurance_ratio)
insurance_budget.sort(key = get_name_key)

# SCHOOL AID/SPECIAL EDUCATION

edu_data = list(avg_data)

i_ratio_low_high = list(insurance_ratio) 
i_ratio_low_high.sort(key = get_avg_key) 
i_ratio_high_low = list(insurance_ratio) 
i_ratio_high_low.sort(key = get_avg_key, reverse = True) 

# reversed sorting() so that 
edu_ratio = [] 
for i in range(0,len(i_ratio_low_high)): 
    edu_ratio.append([i_ratio_low_high[i][0], i_ratio_high_low[i][1]]) 

edu_budget = allocate_budget(42000000, 0.75, edu_ratio)
edu_budget.sort(key = get_name_key)

# SOCIAL SERVICES

socialserv_budget = allocate_budget(33000000, 0.87, insurance_ratio)



# Ask the user what budget they want to look at the statisitcs for

print('NY State Budgets')
print()
print('You can see the broken up budgets by county for NY State. You can choose from:')
print('\t1. Health Insurance\n\t2. School Aid/Special Education\n\t3. Social Services')
print()

while True:
    
    budget_view = input('Which budget would you like to see? => ').strip().lower()
    
    # Check user input and provide the statisitics for what couny gets what amount
    if budget_view in ['1', 'health insurance']:
        print_c_budgets('Health Insurance Statistics', insurance_budget)
        break
    
    elif budget_view in ['2', 'school aid/special education', 'school aid', 'special education']:
        print_c_budgets('School Aid/Special Education Statistics', edu_budget)
        break
    
    elif budget_view in ['3', 'social services']:
        print_c_budgets('Social Services Statistics', socialserv_budget)
        break
    
    else:
        print('The budget entered could not be found.')
        continue


    








#######
##  The rest of this code was written to test the code and then
##  commented out.
#######

# print(hw5_util.read_deaths_all())
# print(insurance_budget)
'''
edu_ratio = get_ratio(edu_data)
print(edu_ratio)
edu_ratio.sort(key = get_avg_key)
'''
# print('edu ratio:', edu_ratio)
'''
# TEST RATIOS
edu_check = 0
for c in edu_budget:
    edu_check += c[1]
print(edu_check)
'''
# print(edu_budget)
# c_budget = round(33000000 / len(socialserv_data) / 1000000, 2)
'''
socialserv_budget = []
for c in socialserv_data:
    socialserv_budget.append([c, c_budget])
print(socialserv_budget)
'''
# print(len(socialserv_data))
# print(edu_data)
# print(insurance_data)
# print(avg_data)
# print(yr_data)
# print( get_yr_data(all_data) )
# print(len(relevant_data))