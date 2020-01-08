### IMPORT STATEMENTS ###

import worker
import job
from positions import positions

# hiring manager handles both hiring and firing
class HiringManager:

    def __init__(self, employees):
        
        # employee/workers at company
        self.employees = employees

    def number_employees(self):
        return len(self.employees)
    

    # HIRING ALGORITHM
    
    # for a given specific job opportunity, hire 1 person (assign 1 worker that job)
    def hire(self, job, pool):
        # hiring_pool = dictionary of job candidates (worker objects)
        
        # for every candidate, calculate their position_specific_score
        candidate_by_score = {job.fit_score(candidate):candidate for candidate_id, candidate in pool.items()}
        
        # decide who to hire
        # find who is best candidate for this job
        best_score = max(candidate_by_score.keys())
        
        # worker object
        best_candidate = candidate_by_score[best_score]
        best_candidate_id = best_candidate.worker_id
        
        # hire the best-fit candidate
        best_candidate.assign_job(job)
        # add them to dictionary of employed workers
        self.employees[best_candidate_id] = best_candidate
        
        # remove the best-fit candidate from pool
        pool.pop(best_candidate_id)
        
        # Hired _______ for position #__
        print()
        print('HIRED NEW EMPLOYEE\n')
        print(best_candidate)
        
        # print(job)
        # candidate's profile
        
        
    # FIRING ALGORITHM
        
    def firing(self, position_id):
               
        # for a given position/job, fire 1 employee from pool of employees that have that position
        position_pool = list(filter(lambda e: e.job.position_id == position_id, self.employees.values()))
        
        employee_by_score = {e_obj.job.productivity_score(e_obj):e_obj for e_obj in position_pool}
        
        # decide who to fire by finding who has the worst/least productivity score
        worst_score = min(employee_by_score.keys())
        
        worst_employee = employee_by_score[worst_score]
        worst_employee_id = worst_employee.worker_id        
        
        # remove worker from self.employees
        self.employees.pop(worst_employee_id)
        
        print()
        print('FIRED EXISTING EMPLOYEE')
        print('Fired due to lowest productivity score of: {}\n'.format(worst_score))
        print(worst_employee)
        
        # update that worker's job status to fire
        worst_employee.remove_job()
        