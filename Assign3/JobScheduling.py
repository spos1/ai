def schedule_jobs(jobs):
    sorted_jobs = sorted(jobs, key=lambda x: x[1], reverse=True)
    schedule = []
    current_time = 0

    for job in sorted_jobs:
        job_id, duration = job
        start_time = current_time
        finish_time = current_time + duration
        current_time = finish_time
        schedule.append((job_id, start_time, finish_time))

    return schedule


num_jobs = int(input("Enter the number of jobs: "))
jobs = []
for i in range(num_jobs):
    job_id = input(f"Enter the job ID for job {i+1}: ")
    duration = int(input(f"Enter the duration for job {i+1}: "))
    jobs.append((job_id, duration))


schedule = schedule_jobs(jobs)


for job in schedule:
    print(f"Job {job[0]}: start time = {job[1]}, finish time = {job[2]}")
