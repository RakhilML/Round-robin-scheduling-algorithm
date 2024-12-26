# Round robin scheduling algorithm

Round Robin is a scheduling algorithm used in operating systems and computer networking. It ensures that each process in a queue receives a fair share of CPU time by allocating CPU time slices to each process in a queue in a cyclic order. 

Due to the algorithm's guarantee of CPU time for each process, it is effective for quick tasks and prevents starvation. 
It is possible to modify the time slice, or "quantum," to adapt the algorithm to various workloads.

# Requirements
The number of processes to consider = (8 % 3 )+3 = 5 processes
Min Burst requirement for each process= (8 % 5)+5 = 8
Time Quantum -> 3

The time quantum for each process is set to 3. The algorithm schedules the processes based on
these parameters, giving each process a slot of 3 units of time to execute before switching to the
next process.

# working demonstration (XOS)
(https://youtu.be/plLCkaWzzgo)

When only 4 processes is loaded we get the results , when 5 processes is loaded we get the error
as (OS exceeds block 1) it is probably because the code size exceeds 3 pages. 
XOS only has 3 pages and 1 stack for all the processes Timer is randomly taken from 1 to 10. 
For time quantum 3 we need to use timer=6.
