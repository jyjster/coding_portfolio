'''
This program parses an article text file and compares the words in the article
with those in the positive and negative word files.

This program is for Hw06, Part 1: Parsing Files & Sets.

Last modified: 04/04/19
By: Jordan Jackson
'''


### IMPORT STATEMENTS ###

'''
Use the 're' Python module to strip extraneous characters.
Pass a word as a string into re.compile() and regex.sub() and module
will return the stripped word as a string, 
that can be appended to a data structure.
'''

import re



### FUNCTION DEFINITIONS ###

def format_str(L):
      
      '''
      This function reads in a list of strings, then returns a formatted
      list where each string is in lowercase and has been stripped of
      extraneous characters.
      
      Input parameters:
      L: a list of words (str)
          EX: list of words from article's content or from article's headline
           
      Return value:
      L_formatted: list of formatted words (str)
      '''           
      
      # Strip extra characters except for '+', given 'a+' is a possible word in 
      # provided the positive word list
      
      regex = re.compile('[^a-zA-Z-+]')
      
      L_formatted = []
      for string in L:
            # 1. Eliminate extraneous characters from a single word
            string = regex.sub('', string)
            
            # 2. Make all words in same case
            string = string.lower()
            if string != '':
                  L_formatted.append(string)
      
      return L_formatted


def parse_wordlist(file_name):
      
      '''
      This function reads and parses a text file containing a list of
      positive or negative words.
      
      Input parameters:
      file_name: file name of an artcile as a string, including the file extension
           
      Return value:
      set(word_bank): a set of the words (str) that will be compared with the
      words in an article
      '''           
      
      word_bank = []
      
      for line in open(file_name):
            
            line = line.strip()
            
            # 1. Skip the big comment block at the beginning of file surrounded by semicolons.
            # Also skip empty lines (lines with only whitespace).
            if line.startswith(';') or line == '':
                  continue
            else:

                  word_bank.append(line.lower())
                  
      # Retur a set in case the positive or negative word lists have duplicate words           
      return set(word_bank)


def parse_article(article_file):
      
      '''
      This function reads and parses an article text file.
      
      Input parameters:
      article_file: file name of an artcile as a string, including the file extension
           
      Return value:
      d: a dictionary storing data for a given club
           EX: {headline, authors, source, length_all, article_in_words (list of all words), 
                unique_words (set of unique words), length_unique}
      '''                
      
      d = {}
      f = open(article_file)
      
      # Store information on the article in the dictionary
      # (i.e. headline, author, source, and length of article)
      d['headline'] = f.readline().strip()
      # For latetr use: to use for analyzing positive/negative 
      # word matches in the headline
      d['headline_in_words'] = format_str(d['headline'].split())
      d['date'] = f.readline().strip()
      d['authors'] = f.readline().strip()
      d['source'] = f.readline().strip()
      
      # Store entire article text as 1 string
      article_txt_raw = f.read()
      
      # Reminder: split() removes the things it splits on
      d['article_in_words'] = format_str(article_txt_raw.split())
      
      # Inlcuded a set of unique words in article and two computations
      # for comparing the two word list files with the article text. 
      d['length_all'] = len(d['article_in_words'])
      d['unique_words'] = set(d['article_in_words'])
      d['length_unique'] = len(d['unique_words'])
      
      return d


def emoti_unique_count(emoti_words, unique_words):

      '''
      This function computes (#3) the number of occurences of 
      positive/negative words in article.
      
      Input parameters:
      emoti_words: set of emotive words
      unique_words: set of unique words in an article
      
      Return value:
      integer: number of words in both an emotive word set and
      an article unique word set
      '''                      
      shared_words = emoti_words.intersection(unique_words)

      return len(shared_words)


def emoti_all_count(emoti_words, all_words):

      '''
      This function computes (#5) the total number of
      all words in article that are positive/negative.
      
      Input parameters:
      emoti_words: set of positive/negative words
      all_words: list of all the words in article (includes duplicates)
      
      Return value:
      count: integer number of number of occurences of positive/negative
      words in article
      '''    
      
      count = 0
      
      for word in emoti_words:
            count += all_words.count(word)
      return count


def emoti_occurences(emoti_words, all_words):
      
      '''
      This function creates a dictionary of each positive/negative word
      in article and the number of occurences of each of those words in article.
      
      Input parameters:
      emoti_words: set of positive/negative words
      all_words: list of all the words in article (includes duplicates)
      
      Return value:
      d: dictionary
           key = positive/negative word
           value = integer number of occurences of that word in article
           
           EX: {word:occurences, word:occurences, ...}
      '''
      
      d = {}
      
      for word in emoti_words:
            occur = all_words.count(word)
            # If occurences = 0, don't include in resulting dictionary.
            if occur > 0:
                  d[word] = occur
      
      return d
      

def print_output(d_article, pos_words, neg_words):
      '''
      This function prints results of the data analysis among an article and two
      text files that contain lists of postive/negative words.
      
      Input parameters:
      d_article: dictionary storing information and calculations for a given article
      pos_words: set of positive words from positive.txt
      neg_words: set of negative words from negative.txt
      
      Return value:
      None
           Rather than returning something, this function prints things
      '''
      
      print('Headline: {}'.format(d_article['headline']))
      print('Author(s): {}'.format(d_article['authors']))
      print('Source: {}'.format(d_article['source']))
      print('Length of article (words): {}'.format(d_article['length_all']))
      print()
      pos_unique_count = emoti_unique_count(pos_words, d_article['unique_words'])
      print('Positive word count: {}'.format(pos_unique_count))
      neg_unique_count = emoti_unique_count(neg_words, d_article['unique_words'])
      print('Negative word count: {}'.format(neg_unique_count))
      print()
      
      # 4. Percentage of words in article that are unique
      deci_unique_all = d_article['length_unique'] / d_article['length_all']
      print('Percentage of article is unique words: {:.0f}%'.format(deci_unique_all * 100))
      
      # 6. Percentage of unique words in article that are positive
      deci_unique_pos = pos_unique_count / d_article['length_unique']
      print('Percentage of unique words in article that are positive: {:.1f}%'.\
            format(deci_unique_pos * 100))
      # 6. Percentage of unique words in article that are negative
      deci_unique_neg = neg_unique_count / d_article['length_unique']
      print('Percentage of unique words in article that are negative: {:.1f}%'.\
            format(deci_unique_neg * 100))
      print()
      
      # 5. Percentage of all words in article that are positive
      pos_all_count = emoti_all_count(pos_words, d_article['article_in_words'])
      deci_all_pos = pos_all_count / d_article['length_all']
      print('Percentage of all words in article that are positive: {:.1f}%'.\
            format(deci_all_pos * 100))
      # 5. Percentage of all words in article that are negative
      neg_all_count = emoti_all_count(neg_words, d_article['article_in_words'])
      deci_all_neg = neg_all_count / d_article['length_all']
      print('Percentage of all words in article that are negative: {:.1f}%'.\
            format(deci_all_neg * 100))
      print() 
      
      # 1. All of the positive word matches in the article
      # 2. Number of occurrences of each positive word in article      
      d_pos_occur = emoti_occurences(pos_words, d_article['article_in_words'])
      print('Positive words:')
      for word, occur in d_pos_occur.items():
            print('Word: {:<20}Occurences: {}'.format(word, occur))
      print()
      # 1. All of the negative word matches in the article
      # 2. Number of occurrences of each negative word in article         
      d_neg_occur = emoti_occurences(neg_words, d_article['article_in_words'])
      print('Negative words:')
      for word, occur in d_neg_occur.items():
            print('Word: {:<20}Occurences: {}'.format(word, occur))
      print()
      
      # 7. If there positive/negative word matches in the headline
      headline_pos_count = emoti_all_count(pos_words, d_article['headline_in_words'])
      headline_neg_count = emoti_all_count(neg_words, d_article['headline_in_words'])
            
      if headline_pos_count > headline_neg_count:
            headline_overall = 'positive'
      elif headline_pos_count < headline_neg_count:
            headline_overall = 'negative'
      else:
            headline_overall = 'neutral'
            
      print('Overall sentiment of headline: {}'.format(headline_overall))   
      print('Positive words in the headline: {}'.format(headline_pos_count))
      print('Negative words in the headline: {}'.format(headline_neg_count))     



### PROGRAM STARTS HERE ###
      
neg_word_bank = parse_wordlist('negative.txt')
pos_word_bank = parse_wordlist('positive.txt')

article = parse_article('article3.txt')

print_output(article, pos_word_bank, neg_word_bank)




#######
##  The rest of this code was written to test the code and then
##  commented out.
#######

'''
print(parse_wordlist('negative.txt'))
print(parse_wordlist('positive.txt'))
print(format_str(article['article_in_words']))

print (article['article_in_words'])
print(article['headline_in_words'])

print(neg_word_bank)
print(pos_word_bank)

print(d['article_in_words'])
print()
print(len(d['article_in_words']))

article = parse_article('article1.txt')
article = parse_article('article2.txt')
article = parse_article('article3.txt')
'''