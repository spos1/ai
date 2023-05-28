n = int(input("Enter number of jobs: "))
jobs = []
print("Enter Id and profit respectively for each job:")
for i in range(n):
    job = input("Job " + str(i + 1) + ": ").split()
    jobs.append(job)

sorter = lambda job: int(job[1])
jobs = sorted(jobs, key=sorter, reverse=True)

scheduled = []

for i in jobs:
    scheduled.append(i[0])

print("Jobs are scheduled as: ")
print(scheduled)
