def priorityScheduling(proc, n): 

	proc = sorted(proc, key = lambda proc:proc[2],reverse =True); 

if __name__ =="__main__": 
	
	process = [[1, 10, 1], 
			[2, 20, 0], 
			[3, 15, 1],
			[4, 11, 2]] 
    n = 4
	priorityScheduling(process, n)        