'''
This program reads in death statistics from an external finale, then creates a
trendline visualization comparing death trends between two different ocunties over
11 years from 2003 to 2013.

This program is for Hw05, Part 1: Mapping Trends.

Last modified: 03/21/19
By: Jordan Jackson
'''


### IMPORT STATEMENTS ###

'''Given a string containing a county name, the utility module hw5_util.py
provides a function read_deaths(county) that returns you a list of 11 numbers.'''

import hw5_util
import sys


### FUNCTION DEFINITIONS ###


def get_data(cname):
    
    
    '''
    This function checks input string and 
    reads in the death statistics for a given area of NYS.
    
    Input parameters:
    cname: string containing a county name
    
    Return value:
    list: list of 11 numbers corresponding to annual death rate of county
    '''        
    
    data = hw5_util.read_deaths(cname)
    
    # Check whether user input is a valid county name
    # hw5_util.read_deaths will return an empty list whenever the county cannot be found    
    if data == []:
        print('{} is an invalid name'.format(cname))
        
        # You can ignore any warnings you get from using sys.exit() that may show up after your error message
        sys.exit()
        
    else:
        return data
    

def diff_list(L1, L2):
    
    '''
    This function computes the difference between the death rates of 2 areas for each year.
    
    Input parameters:
    L1 and L2: each a list of a county's data
    
    Return value:
    list: returns a list of differences as numerical values
    '''        
    
    diff = []
    
    # Assumption: L1 and L2 are the same length
    # for loop: iterates for each year in dataset
    for i in range(0, len(L1), 1):
        
        # Calculate difference between corresponding indices in L1 and L2
        # rounding: differences are rounded to one decimal place
        result = round(L1[i] - L2[i], 1)
        diff.append(result)
        
    return diff


def encode_diff_list(L):

    '''
    This function encodes the list of differences using symbols =, +, and -. 
    Each element in L, is translated into 1 symbol.
    
    Input parameters:
    L: list of differences
    
    Return value:
    trend_line: string representing encoded trendline, consisting of symbol characters
    '''            
    
    trend_line = ''
    for value in L:
        
        # - implies that the first area has more than 50 more deaths for that year
        if value > 50:
            trend_line += '-'
            
        # + implies the first area has more than 50 fewer deaths for that year
        elif value < -50:
            trend_line += '+'
            
        # = implies the two areas are within +/- 50 deaths per 100,000 for that year
        else:
            trend_line += '='     
    
    # Order: trendline should be in reverse order from 2013 to 2003
    return trend_line[::-1]
        
     
def compare_c(str, cname1, cname2):

    '''
    This function determines the healthier county based on the assumption that 
    the area with lower deaths per 100,000 is a healthier place to live.
    
    Input parameters:
    str: encoded string of symbols
    cname1: string, name of county
    cname2: string, name of county
    
    Return value:
    string: determination of the healthier area as a string to be printed
    '''            
        
    # Compare the number of + and - symbols in str to determine the healthier area
    # + favors the first area and - favors the second area
    
    plus = str.count('+')
    minus = str.count('-')
    
    if plus > minus:
        # returns cname1 as healthier area
        return 'I would rather live in {} than {}'.format(cname1, cname2)
        
    elif plus < minus:
        # returns cname2 as healthier county
        return 'I would rather live in {} than {}'.format(cname2, cname1)
        
    else:
        return '{} and {} are the same'.format(cname1, cname2)


def format_to_print(trendline):
    
    '''
    This function formats and prints the trend line including a header for the data labeling the start 
    and end years, in reverse order from 2013 to 2003, and determination of the healthier area
    
    Input parameters:
    trendline: encoded string of symbols
    
    Return value:
    printed strings
    '''    
    
    print()
    
    # The 2013 and 2003 are printed to line up with the margins of the trend data
    print(' ' * 7 + '2013' + ' ' * (len(trendline) - 8) + '2003')
    print('Trend: {}'.format(trendline))
    
    print()
    


### PROGRAM STARTS HERE ###

# Input with white space at the left or right of the text 
# and input of any case (lowercase or uppercase) will be valid input

cname1 = input('Enter the first area to check => ').strip()
print(cname1)

cdata1 = get_data(cname1)


cname2 = input('Enter the second area to check => ').strip()
print(cname2)

cdata2 = get_data(cname2)



trendline = encode_diff_list(diff_list(cdata1, cdata2))


# Print trendline, header, and labels
format_to_print(trendline)
# Print determination of the healthier area
print(compare_c(trendline, cname1.lower().title(), cname2.lower().title()))



#######
##  The rest of this code was written to test the code and then
##  commented out.
#######

# print(diff_list(cdata1, cdata2))
# diff_list(cdata1, cdata2)

# print(encode_diff_list(diff_list(cdata1, cdata2)))
# encode_diff_list(diff_list(cdata1, cdata2))

# print(trendline)

# print(compare_c(encode_diff_list(diff_list(cdata1, cdata2)), cname1, cname2))

'''
import hw5_util
cdata1 = hw5_util.read_deaths('Erie')
cdata2 = hw5_util.read_deaths('Cattaraugus')
print('Erie:', cdata1)
print('Cattaraugus:', cdata2)
'''
