# What is this?
This repository is made for the assignment of CSE316 (Operating Systems) as a part of CA3, for 4th Semester.   

- Write a program to implement priority scheduling algorithm with context switching time.
Prompt to user to enter the number of processes and then enter their priority, burst time and
arrival time also. Now whenever operating system preempts a process and shifts cpu’s control to some another process of higher priority assume that it takes 2 seconds for context
switching(dispatcher latency).Form a scenario, where we can give the processes are assigned
with priority where the lower integer number is higher priority and then context switch .. as the process waits the priority of the process increase at rate of one per 2 time units of wait.
Calculate waiting time and turnaround time for each process.

#### Priority Scheduling Algorithm:
 Priority scheduling is a non-preemptive algorithm and one of the most common scheduling algorithms in batch systems. Each process is assigned a priority. Process with the highest priority is to be executed first and so on. Processes with the same priority are executed on first come first served basis. Priority can be decided based on memory requirements, time requirements or any other resource requirement.   
To run: Open the file in a terminal and type ```python3 prorityScheduling.py```
