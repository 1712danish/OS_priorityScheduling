def waitingTime(processes, n, wt): 
	wt[0] = 0

	for i in range(1, n): 
		wt[i] = processes[i - 1][1] + wt[i - 1] 

def turnAroundTime(processes, n, wt, tat): 
	
	for i in range(n): 
		tat[i] = processes[i][1] + wt[i]         

def priorityScheduling(proc, n): 

	proc = sorted(proc, key = lambda proc:proc[2],reverse =True); 
    print("Order in which processes gets executed") 
	for i in proc: 
		print(i[0], end = " ") 

if __name__ =="__main__": 
	
	process = [[1, 10, 1], 
			[2, 20, 0], 
			[3, 15, 1],
			[4, 11, 2]] 
    n = 4
	priorityScheduling(process, n)        