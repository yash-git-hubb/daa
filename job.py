def printJobScheduling(jobs, t):
    jobs.sort(key=lambda x: x[2], reverse=True)
    
    result = [None] * t 

    # Schedule each job if a free slot is available before or on its deadline
    for i in jobs:
        for j in range(min(t,i[1])-1, -1, -1):
            if result[j] is None:  # Check for free slot
                result[j] = i[0]  # Assign job to slot
                break
    print("Job sequence to maximize profit:", result)

n = int(input("Enter the number of jobs: "))
jobs = [[input("Job ID: "), int(input("Deadline: ")), int(input("Profit: "))] for _ in range(n)]  #list bna rhe h [id,deadline,profit]
t = int(input("Enter the number of available time slots: "))
printJobScheduling(jobs,t)
