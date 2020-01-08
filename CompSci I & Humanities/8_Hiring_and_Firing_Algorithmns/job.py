
import random
from positions import positions
import worker

class Job:
    def __init__(self, job_id, position_id = None):
        self.job_id = job_id
        
        # if position_id exists:
        if position_id:
            # assign to id passed in
            self.position_id = position_id
        else:
            # create a randomly-generated position_id
            self.position_id = int(random.uniform(1, 3))

    def tabbed_profile_str(self):
        # intialized to null string
        outstr = ''
        
        outstr += '\tJob-ID: {}\n'.format(self.job_id)
        outstr += '\tTitle: {}\n'.format(positions[self.position_id][0])
        outstr += '\tSalary: {}'.format(positions[self.position_id][1])
        return outstr    

    def __str__(self):
        # intialized to null string
        outstr = ''
        
        outstr += 'Job-ID: {}\n'.format(self.job_id)
        outstr += 'Title: {}\n'.format(positions[self.position_id][0])
        outstr += 'Salary: {}'.format(positions[self.position_id][1])
        return outstr
    
    
    ## REQUIREMENTS ALGORITHMN ##
    
    def prev_job_relevancy_score(self, worker):
        
        score = 0
        # TEST # print('prev_job: {}'.format(worker.prev_job_importance))
        # TEST # print(self.position_id)
        
        if worker.prev_job_importance == self.position_id:
            score = 10
            return score
        else:
            return score
    
    def manager_fit_score(self, worker):
        score = 0
   
        score += ( worker.edu_score()  * 0.23)
        score += ( worker.english_score() * 0.23)
        score += ( worker.performance_score() * 0.38)
        score += ( self.prev_job_relevancy_score(worker) * 0.15)
        
        score += ( worker.other_fluent_score() * 0.1)
        
        score += ( worker.turnover_score() * 0.2)
        score += ( worker.affirmative_action_score() * 0.46)
        
        return round(score, 2)
    
    def store_worker_fit_score(self, worker):
        score = 0
   
        score += ( worker.edu_score()  * 0.15)
        score += ( worker.english_score() * 0.23)
        score += ( worker.performance_score() * 0.38)
        score += ( self.prev_job_relevancy_score(worker) * 0.07)
        
        score += ( worker.other_fluent_score() * 0.36)
        score += ( worker.turnover_score() * 0.1)

        score += ( worker.affirmative_action_score() * 0.46)
        
        return round(score, 2)
    
    def office_worker_fit_score(self, worker):
        score = 0
   
        score += ( worker.edu_score()  * 0.35)
        score += ( worker.english_score() * 0.23)
        score += ( worker.performance_score() * 0.38)
        score += ( self.prev_job_relevancy_score(worker) * 0.1)
        
        score += ( worker.other_fluent_score() * 0.05)
        score += ( worker.turnover_score() * 0.18)
        
        score += ( worker.affirmative_action_score() * 0.46)
        
        return round(score, 2)    
    
    def fit_score(self, worker):
        # manager
        if self.position_id == 1:
            return self.manager_fit_score(worker)
        # store worker
        elif self.position_id == 2:
            return self.store_worker_fit_score(worker)
        # office worker
        elif self.position_id == 3:
            return self.office_worker_fit_score(worker)
    
    ## PRODUCTIVITY ALGORITHMN ##
    
    def productivity_score(self, worker):
        score = 0

        score += ( worker.performance_score() * 0.75)
        score += (worker.working_yrs_score() * 0.25)
        
        # TEST # print(score)
        
        return round(score, 2) 

