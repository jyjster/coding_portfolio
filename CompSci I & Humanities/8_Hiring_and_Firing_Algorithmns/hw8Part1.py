### IMPORT STATEMENTS ###

import worker
import job
from positions import positions


### FUNCTION DEFINITIONS ### 

def assign_worker_best_job(worker, jobs, avail_workers):
    
    # {rating : job rating : job, rating : job}
    ratings = {job.fit_score(worker):job for job in jobs}
    # TEST # print(list(ratings.keys()))
 
    score_best_fit = max(ratings.keys())
    
    position_id_best_fit = ratings[score_best_fit].position_id
    
    # TEST # print(position_id_best_fit)
    # TEST # return position_id_best_fit
    
    # create a new job based on position_id
    worker_id = worker.worker_id
    
    # use worker_id as job_id because we know it will be unique
    new_job = job.Job(worker_id, position_id_best_fit)
    
    # assign worker that new job
    worker.assign_job(new_job)
    
    # remove worker from avail_workers
    avail_workers.pop(worker_id)

# TEST # print(assign_worker_best_job(workers[1], [manager_job, store_worker_job, office_worker_job], workers))
# TEST # assign 1 worker a job
# TEST # assign_worker_best_job(workers[1], [manager_job, store_worker_job, office_worker_job], avail_workers)
# TEST # print(workers[1])

### PROGRAM STARTS HERE ###
workers = dict()
for worker_id in range(1, 26):
    workers[worker_id] = worker.Worker(worker_id)
    # TEST # print(workers[worker_id].name)
    
avail_workers = dict(workers)

# Create 3 jobs based on the 3 possible positions
manager_job = job.Job(1000, 1)
store_worker_job = job.Job(1001,2)
office_worker_job = job.Job(1002,3)

# Assign job to each worker
for worker_id, worker in workers.items():
    assign_worker_best_job(worker, [manager_job, store_worker_job, office_worker_job], avail_workers)
    
for w_id, worker in workers.items():
    print()
    print(worker)
    
    # TEST # productivity # print(worker.job.productivity_score(worker))
    