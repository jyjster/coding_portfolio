
### IMPORT STATEMENTS ###
import random
from positions import positions
from job import Job
import gender
import race

'''
WORKER CHARACTERISTICS
1. Education
       highest level of edu attainment
2. Level of Prestige and Connections
       performance/quality in your previous job(s)
3. Number Previous Jobs
4. Number of Current Jobs
5. Importance of previous position
       previous position title
6. Years of Work (total)
7. Gender
8. Race
9. English proficiency (rating)
10. Fluent Languages 
       number of other languages fluent other than English
'''


# number does not corresponding with worth/value, it's just for idenfitifation
# limitations: only 1 possible
edu_name_by_id = {1: 'Highschool_GED',
                  2: 'Other',
                  3: 'Associate',
                  4: 'Bachelor',
                  5: 'Master',
                  6: 'Phd'}

# allowing halves, a little more granularity/choices/options
ratings_with_halves = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]

ratings_with_ints = [1, 2, 3, 4, 5]
current_jobs_L = [0, 0, 0, 0, 1, 1, 1, 2, 2, 3]


class Worker:

    def __init__(self, worker_id):

        self.worker_id = worker_id
        
        self.gender_id = gender.random_gender_id()
        self.name = gender.random_gender_name(self.gender_id)
        
        self.race_id = race.random_race_id()

        # assumption: everyone has worked
        
        self.edu = random.choices([1, 2, 3, 4, 5, 6], [.02, .01, .05, .75, .15, .02])[0]

        self.performance = random.choice(ratings_with_halves)

        self.employ_status = 0
        self.current_job_count = random.choice(current_jobs_L)

        self.previous_job_count = int(random.uniform(1, 10))
        
        # 6. Years of Work (total)
        self.working_years_count = int(random.uniform(1, 50))

        # reference occupation_by_id
        self.prev_job_importance = int(random.uniform(1, 3))
        
        # 9. English proficiency
        self.english_level = random.choice(ratings_with_ints)
        
        # 10. Fluent Languages 
        self.fluent_lang_count = random.choices([0, 1, 2, 3, 4], [.6, .3, .08, .02, 0])[0]

        self.job = None
        
        
    def __str__(self):
        outstr = ''
        outstr += 'Name: {}\n'.format(self.name)
        outstr += 'Worker-ID: {}\n\n'.format(self.worker_id)
        
        outstr += '\tGender: {}\n'.format(gender.gender_name_by_id[self.gender_id])
        outstr += '\tRace: {}\n'.format(race.race_name_by_id[self.race_id])
        outstr += '\tEducation: {}\n\n'.format(edu_name_by_id[self.edu])
        
        outstr += '\tEnglish-proficiency level: {}\n'.format(self.english_level)
        outstr += '\tNumber of other fluent languages: {}\n\n'.format(self.fluent_lang_count)
        
        outstr += '\tPeformance: {}\n'.format(self.performance)
        outstr += '\tNumber of previous jobs: {}\n'.format(self.previous_job_count)
        outstr += '\tNumber of working years: {}\n'.format(self.working_years_count)
        outstr += '\tPrevious title: {}\n'.format(positions[self.prev_job_importance][0])  
        outstr += '\tNumber of current jobs: {}\n\n'.format(self.current_job_count)
        
        # check if self.job is not = None
        if self.job:
            outstr += Job.tabbed_profile_str(self.job)
            outstr += '\n'
            outstr += '\tProductivity score: {}\n'.format(self.job.productivity_score(self))
        

        return outstr
        
    def affirmative_action_score(self):
        score = 0
        
        # 1 is male
        if self.gender_id != 1:
            score += 5
        # 1 is white
        if self.race_id != 1:
            score += 5
            
        return score
    
    def edu_score(self):
        score = 0
        if self.edu == 1:
            score += 6
        elif self.edu == 2:
            score += 6.5
        elif self.edu == 3:
            score += 7
        elif score == 4:
            score += 8
        elif score == 5:
            score += 9
        elif score == 6:
            score += 10
            
        return score
    
    def english_score(self):
        return self.english_level * 2
    
    def other_fluent_score(self):
        return (self.fluent_lang_count + 1) * 2
    
    def performance_score(self):
        return self.performance * 2
    
    def turnover_score(self):
        if self.working_years_count == 0:
            return 8
        turnover_rate = self.previous_job_count / self.working_years_count
        if turnover_rate < 0.1:
            return 10
        elif turnover_rate <= 0.6:
            return 8
        elif turnover_rate < 1.0:
            return 5
        else:
            return 1
        
    def working_yrs_score(self):

        if self.working_years_count < 3:
            return 2
        elif self.working_years_count < 6:
            return 5
        elif self.working_years_count < 20:
            return 8   
        else:
            return 10    
    
    # ASSIGNING JOB

    # assign that job to that worker
    def assign_job(self, job):
        self.job = job
        

    def remove_job(self):
        if self.job:
            old_job = self.job
            self.job = None
        else:
            old_job = None
            
        return old_job
   

    
        
        
    
    