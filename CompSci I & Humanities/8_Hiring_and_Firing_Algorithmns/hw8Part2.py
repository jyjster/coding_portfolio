### IMPORT STATEMENTS ###

import worker
import job
import hiringmanager
from positions import positions
import random

### FUNCTION DEFINITIONS ###

# FROM HW8PART1.PY
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
    

# CODE NEW TO HW8PART2.PY

def get_job_types(action):
    # {position_id : #, 'positiion_id': #, 'position_id', #}
    
    job_action_type = dict()
    for (position_id, position) in positions.items():
        quantity = int(input("How many {}s do you want to {}? ".format(position[0], action)))
        job_action_type[position_id] = quantity
        
    # returns dictionary
    return job_action_type

def create_new_jobs(quantity_by_position_id):
    # creates all new jobs with corresponding position_ids based on user input
    new_jobs = []
    for (position_id, quantity) in quantity_by_position_id.items():
        for i in range(0, quantity):
            new_jobs.append(job.Job(random.randint(2000,100000), position_id))
            
    # return list of job objects
    return new_jobs

# TEST # print(assign_worker_best_job(workers[1], [manager_job, store_worker_job, office_worker_job], workers))
# TEST # assign 1 worker a job
# TEST # assign_worker_best_job(workers[1], [manager_job, store_worker_job, office_worker_job], avail_workers)
# TEST # print(workers[1])

### PROGRAM STARTS HERE ###

# CODE FROM HW8PART1.PY
unique_id = 1
workers = dict()
for i in range(1, 26):
    workers[unique_id] = worker.Worker(unique_id)
    unique_id += 1

avail_workers = dict(workers)

# Create 3 jobs based on the 3 possible positions
manager_job = job.Job(unique_id, 1)
unique_id +=1
store_worker_job = job.Job(unique_id,2)
unique_id +=1
office_worker_job = job.Job(unique_id,3)
unique_id +=1

# Assign job to each worker
for worker_id, w in workers.items():
    assign_worker_best_job(w, [manager_job, store_worker_job, office_worker_job], avail_workers)


# CODE NEW TO HW8PART2.PY

hiring_manager = hiringmanager.HiringManager(workers)

while True:
    print("There are currently {} employees\n".format(hiring_manager.number_employees()))
    action = input("Do you want to hire, fire, or stop? ").strip().lower()
    # TEST # print(action)
    if action != 'hire' and  action != 'fire':
        break
    # either hiring or firing
    
    # dictionary
    num_job_types_by_position_id = get_job_types(action)
    
    if action == 'hire':
        # list
        new_jobs = create_new_jobs(num_job_types_by_position_id)
        # TEST # print(new_jobs)
        numb_requested = sum(num_job_types_by_position_id.values())
        worker_pool_count = 2 * numb_requested
        
        # TEST # print(worker_pool_count)
        # TEST # print(unique_id)
        
        # make candidate pool for hiring
        hiring_pool_d = dict()
        for i in range(1, worker_pool_count + 1):
            
            hiring_pool_d[unique_id] = worker.Worker(unique_id)
            # print(hiring_pool_d[unique_id])
            unique_id += 1
        
        for j in new_jobs:
            hiring_manager.hire(j, hiring_pool_d)
            
    if action == 'fire':
        
        # keys: position_ids, values: jobs to deal with
        # num_job_types_by_position_id
        
        for position_id, fire_count in num_job_types_by_position_id.items():
            for i in range(1, fire_count + 1):
                hiring_manager.firing(position_id)
        
       