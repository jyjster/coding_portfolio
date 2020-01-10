HOMEWORK 8: Classes & Algorithms

NAME:  Jordan Jackson

FREE RESPONSE:

PART 1

Q:
In your README file, list all 10 characteristics that you have created, and 
justify them. For the 5 predetermined variables, how did you choose to quantify
and measure them, and why did you choose to measure them that way? For the 5
custom variables, why did you choose them, how did you choose to quantify them,
and why did you choose to measure them in that way?

A: See 'worker.py' file for reference.

Characteristics:
1) "Gender"
      variable type: custom
      why: employee diversity via affirmative action
      how: Gender ('Male', 'Female', or 'Other') was referenced as a numerical
           value. See 'gender.py' file for reference. 
2) "Race"
      variable type: custom
      why: employee diversity via affirmative action
      how: Race was referenced as a numerical value. See 'race.py' file for
           reference. 
3) "Education"
      variable type: predetermined
      how: The maximum education-attainment level is represented as a numerical
           value. See edu_name_by_id in the 'worker.py' file for reference. 
4) "English-proficiency level"
      variable type: custom
      why: assuming the company/position primarily uses English for communicating,
           it is important for the employee to be able to communicate well
      how: Proficiency level represented by an integer from 1 to 5, with 5 being
           the most fluent level. Inspired by the Likert Scale.
5) "Number of other fluent languages"
      variable type: custom
      why: for positions/jobs that may require or prefer multi-lingual applicants
      how: count (number) of languages, self-reported by applicant
6) "Performance"
      variable type: predetermined
      how: a numerical score with 5 being the best, likely reported by boss
           from previous company
7) "Number of previous jobs"
      variable type: custom
      why: to calculate a turnover rate in conjunction with "Number of working
           years" for predictive purposes
      how: count (number) of jobs, self-reported by applicant
8) "Number of working years"
      variable type: predetermined
      why: to calculate a turnover rate in conjunction with "Number of previous
           jobs" for predictive purposes
      how: total number of years spent working/employed, self-reported by applicant
9) "Previous title"
      variable type: predetermined
      how: position ('Manager', 'Store Worker', or 'Office Worker') was referenced
           as a numerical value. See 'position.py' file for reference. 
10) "Number current jobs"
      variable type: predetermined
      how: count (number) of jobs held at the present, self-reported by applicant

PART 2

Q:
How does your Hiring algorithm work? What qualities are you weighing more than
others? What types of workers does it privilege, and what types of workers might
get left behind?

A: See 'hiringmanager.py' file for reference.
My Hiring algorithm hires the applicant with the highest fit_score for a given
position (manager, store worker, or office worker).
Among the three positions, english proficiency, performance, and affirmative 
action are weighted equally. I came up with the weighting for affirmative action 
based on the sum of  manager_fit_score's education and english_proficiency 
because I thought these two categories are the most, in my opinion, directly
influenced by gender and race of the included characteristics. As it so happens,
affirmative action (0.46) ended up being the highest weighted quality for each score. 

The store_worker_fit_score weights the number of languages one is fluent in
(excluding english) high because a store worker is the most likely of the
positions to interact with the most amount of people, and therefore the greatest
variety of languages. This may privilege those with the privilege of having
high-quality education. As office_worker_fit_score weights education high, the
education ranking privileges of an higher economic status, privileges white people
and may privilege men.


Q:
How does your Firing algorithm work? What qualities are you weighing more than
others? What types of workers does it privilege, and what types of workers might
get left behind?

A: See 'hiringmanager.py' and 'job.py' files for reference.
My Firing algorithm fires employees based on lowest productivity score, as 
compared to other employees in that same position (position_id) in the company. 
The productivity score is based on a the worker's performance score and the 
total number of years the worker has spent working. Based on the assumption/logic
that the longer one has worked, the better at working and productivity that
individual is, the productivity algorithm is ageist in that it privileges older
individuals. Furthermore, women that have had kids may be left behind because
they may have less years spent working if they took a leave of absence for 
maternity/child-care leave. Based on the logic that the past can be used for
reasonably accurate future predictions, My Firing algorithm weighs one's
performance score as the greatest quality. Basing productivity largely on one's
previous job performance disadvantages those who may have had discriminatory
reviewers--most likely, those of minority workers.


MISC. COMMENTS TO GRADER:  

I interpreted Part 1's 'Level of Prestige and Connections' characteristic as
the 'performance' characteristic in my code.

Numerical values for the characteristics do not correspond with worth/value. 
They are just for identification purposes.

For Part 1's Productivity Algorithm: I am assuming productivity does not influence
hiring decisions or the requirements algorithm. Productivity ranking is based on
the worker’s performance after they are hired.
