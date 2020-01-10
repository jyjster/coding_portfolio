HOMEWORK 7: Dictionaries & Cleaning Data

NAME:  Jordan Jackson

FREE RESPONSE:

Q1) 
As you are cleaning your data, be sure to note down the decisions you’re making for your
README. What have you chosen to do with the data that doesn’t fit your program? Why
doesn’t it fit? How much have you altered the “original” dataset? What do these “dirty”
elements of the dataset represent?

A1)
'Cleaning' Values
    • values of [‘gender’] from single-letter characters to equivalent word 
        - EX: f —> female and m —> male
	- why: because such a translation was shown in the hw’s assignment sheet in the example
          dictionaries and outputs
	- see: translate_gender()
    • values of [‘full_name’], [‘last_name’], and [‘first_name’] from only lowercase 
      characters to the mixed-case letters where the first letter of each word is uppercase
        - EX: jane —> ‘Jane’
	- why: because such capitalization was shown in the hw’s assignment sheet in the example 
          dictionaries and outputs
	- see: translate_name()
    • values of [‘sent_to_cleaned’] / [‘site_edited’] where all spaces were removed
	- why: because I needed them to match the same format of site names in ‘ID_to_site.tsv’ 
          (for later translation from code to name)
	- EX: ‘h 29’ —> ‘h29’
	- see: clean_site_code()
    • all values (of any/all key/keys) were “cleaned” via clean_s()
	- As I wanted to maintain any entry/data notes (such as ‘[blank]’ and ‘(illegible)’
          and ‘(?)’, I did not see any need to eliminate any characters because I did not
          perceive any as “extraneous” or not making sense. However, part of the assignment
          was to handle ‘extraneous characters that don’t make sense.’ Plus, perhaps I personally
          had not seen the extraneous characters that the assignment sheet referred to so I 
          may/might as well “clean” it just in case, it wouldn’t hurt
	      - Based on my interpretation ‘extraneous characters’ to mean symbols, I 
                changed values:
		    - I only kept symbols in (?) and essential to string/words values 
                      (e.g. names O’Connor and M. G. Leonard, and dates -)
                    - I kept ‘(?)’  because I thought it was important for viewers of my data/
                      statistics knew the accuracy of what was being viewed (vs. thinking it was 
                      exactly)
	- I handled ‘(illegible)’ by changing values containing ‘illegible’ to the whole value 
          being ‘illegible’
	- assumption: data fields left empty and values marked as ‘[blank]’  both mean their
          values were ‘unspecified’
	    - I handled values of empty strings (after removing “unnecessary symbols”) to value 
              of “unspecified”
	    - I handled ‘[blank]’ by changing whole value to ‘unspecified’
        - If “extraneous characters” included words or letters that are incomprehensible, then I 
          later use ‘ID_to_Admittors.tsv’ and ‘ID_to_site.tsv’  to translate the admittor_codes 
          entries and site_codes to more recognizable/meaningful words. The site_codes, which 
          contain a mix of alphabetical and numerical characters, represent references known by 
          the people recording the data, but are no longer known by today’s average person 
	- see: clean_s()

'Cleaning' Keys
	• In any/all cases where the dataset had an “_cleaned” or “_control” version of a data 
          variable, I chose to use these edited versions, rather than the original because their 
          values were more ‘cleaned’ and translated (well-understood/understandable) than their  
          original counterparts.
	    - I changed the names of these data variables to “_edited” to represent any    
              “cleaning” or translated before/prior to my cleaning/translating of the data
	    - EX: child_cleaned —> child_edited
	• When creating statistics and sorting data, I used admission_id’s, rather than 
          full_name’s, admittor_1_code and admittor_2_code, rather than their names in admittor_1 
          and admittor_2 because for a single entity, it’s code/number/id will always be 
          constant, whereas its names can be different/varied. Plus, words, as opposed to 
          numbers, are more vulnerable to user/data-entry error.
	    - numbers always constant, names can be different/varied, subject to less 
              user/data-entry error
	• At first, I was not going to change the names of the key names because I thought the 
          key names were arbitrary to the actual data. Although, I felt the wording of some of 
          them were problematic, I thought keeping their original names would be fine because it 
          would reflect their names when the data was actually collected. However, after CS lab, 
          where we discussed how there is great power and potential implications of a 
          programmer’s choice to use/continue with problematic associations/assumptions. Plus, I
          did not want to reinforce any stereotypes and problematic biases to the viewer of my 
          data/statistics, who may not be reading the keys with a historical lens and ‘grain of 
          salt’.
	    - [‘disease’] —> [‘diagnosis’]
	    - [‘disease_control]] —> [‘diagnosis_edited’]
	    - [‘profession’] —> [‘occupation’]
	    - [‘profession_control’] —> [‘occupation_edited’]
            - [‘sent_to’] —> [‘site’]
	    - [‘sent_to_cleaned’] —> [‘site_edited’]
	    - [‘child_cleaned’] —> [‘child_edited’]


Q2) 
At the top of your code, you should type out an explanation (approximately 250 words)
about your chosen statistics, why you chose them, and some analysis about the results. We’ll
reward the extra credit based on what you’ve chosen.

A2) 
see top of user-statistics_interface.py' for my answer

Q3)
How are the categories of the dataset you're working with socially constructed? 

A3)
The 'gender,' 'disease,' and 'profession' fields of the original dataset are 
especially socially constructed.

Gender is like an ontological category for describing one's identity. Disease and profession
 are socially constructed in terms of what counts as part of the category/term 'disease' and
 'profession' is due to the mental maps of the data recorders, norms and common understandings
 within New York institutions, and socio-cultural beliefs and assumptions at the time.

For the next questions, run at the following tests and answer the following questions:


Q4)
Run through your data and track the diagnosed disease of each immigrant. 
Create a list that populates and tallies the kind and number of each disease. 
Cross reference these diseases by gender, admittor, Facility sent to, 
and age.

A4)

From my results from the Bellevue_Full dataset, of the 76 diagnoses, I found the following
 correlations interesting:

regarding diagnoses and gender
    - 'emotional' and 'ungovernable' were only diagnosed to men
    - 'drunkenness,' 'beggar,' and 'poorly' were only diagnosed to women
    - 'insane,' 'intemperance,' and 'destitution' were diagnosed with about 
      an equal distribution among men and women.
 
regarding site and diagnoses:
- it seems being diagnosed as 'recent emigrant' could mean the emigrant is most likely sent 
  to any of the sites except the Lunatic Asylum.
- Although a small percentage, I was surprised 'pregnant' (5.5%) individuals would be sent
  the Lunatic Asylum because of their pregnancy
- Bellevue Complex mainly had patients diagnosed with'sickness' and 'recent emigrant', W 
  site with 'recent emigrant,', Long Island with 'destitution' and 'recent emigrant' and 
  Blackwell's Island with 'destitution,' 'recent emigrant,' and 'sickness'


Q5) 
What trends do you see?  How is disease being constructed, i.e., what counts 
as a disease, and therefore who gets counted as diseased? How do these 
accountings change according to the admittor, by facility, and by gender?

A5) 
- Diagnoses such as pregnancy, poorly, and destitution are counted as diseased, even though
  by today's standards, they would not be. It's also quite confusing because there are very
  general and vague diagnoses or repetitive or overlapping ones (synonyms).
- As the dataset is no Irish immigrants, every immigrant would be diagnosed with a 'disease,'
  including those who are perfectly healthy.
- Data and statistics show racist, gendered, and xenophobic implications.

Q6) 
Run a similar track and tally for profession, cross-referencing with the same 
variables listed above. How is work constructed in the dataset, and by whom? How
does this construction vary by age, gender, and admittor?
A6)

As 'married' and 'spinster' professions are only associated with females, the data suggests most
women did not have a formal (paid) occupation. However, what is considered a profession or work
in itself is very socially constructed.


Q7)
Consider Virginia Eubanks's book, especially Chapter 4, the Allegheny 
Algorithm. How are categories and decisions about parenting, childcare, and 
appropriate care constructed in in Pittsburgh? What parallels do you see between
that example and the data presented in this assignment?

A7)
In both cases of the Child Abuse dataset and the Bellevue Hospital datasets:
- There is a lot of ambiguity in terms of the definition of various conditions and
  categorizations. 
- Burdened with a heavy workload, the workers making these decisions as to what counts
  as a certain designation face additional decision-making challenges due to time 
  pressure and varied expertise.
- It is likely that many of these decision-makers were not explicitly racist, sexist, 
  homophobic, xenophobic ect., although they datasets they still represent, contain, and
  implicate such problematic biases.

MISC. COMMENTS TO GRADER:
 
I realize the title() method made some incorrect capitalization (e.g. it would capitalize first letter after an apostrophe), but I choose to leave it.

I exported the Admittors and Site_Codes datasets from https://drive.google.com/open?id=0B0l93P9e8zrEbEdrS2pTRk91S0U as .tsv files.

Sources I used for this hw assignment:

    https://realpython.com/python-csv/#reading-csv-files-into-a-dictionary-with-csv
    https://www.tutorialspoint.com/python/python_reg_expressions.htm
    https://docs.python.org/2/library/pprint.html

    http://crdh.rrchnm.org/essays/v01-10-(re)-humanizing-data/
    www.nyuirish.net/almshouse/the-almshouse-records/  
    https://drive.google.com/open?id=0B0l93P9e8zrEbEdrS2pTRk91S0Uv


