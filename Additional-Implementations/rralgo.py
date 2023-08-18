NOP = 5 # Number of processes
# Minimum burst time for each process
min_burst = 8
# Time quantum for each process
time_quantum = 4

# Process names
process_names = ["Process A", "Process B", "Process C", "Process D", "Process E"]

# List to store burst times for each process
burst_times = []
# List to store arrival times for each process
arrival_times = []
# List to store completion times for each process
completion_times = [0] * NOP
# List to store remaining burst times for each process
remaining_burst_times = []

# Generate burst times, arrival times, and remaining burst times for each process
for i in range(NOP):
    burst_times.append(min_burst)
    arrival_times.append(0)
    remaining_burst_times.append(min_burst)

# Keep track of time
current_time = 0

# Keep track of processes that have completed execution
completed_processes = []

# Keep track of processes that are ready to be executed
ready_queue = []

# Keep track of the last process to be executed
last_process = -1

# Keep track of the execution order of the processes
execution_order = []

while len(completed_processes) != NOP:
    # Add new processes to the ready queue
    for i in range(NOP):
        if arrival_times[i] <= current_time and i not in completed_processes and i not in ready_queue:
            ready_queue.append(i)
    
    # If there are no processes in the ready queue, increment time
    if not ready_queue:
        current_time += 1
        continue

    # Get the next process to be executed
    current_process = ready_queue.pop(0)
    # If the last process executed is the same as the current process, increment time
    if last_process == current_process:
        current_time += 1
        ready_queue.append(current_process)
        continue
    last_process = current_process

    # Record start time of process
    start_time = current_time
    # Execute process for the time quantum
    for i in range(time_quantum):
        if remaining_burst_times[current_process] > 0:
            current_time += 1
            remaining_burst_times[current_process] -= 1
            # Print the process name
            print(process_names[current_process])
        else:
            break
    # Record completion time of process
    completion_times[current_process] = current_time
    execution_time = current_time - start_time
    # Print execution time of process
    print(f"{process_names[current_process]} - completed execution at time {execution_time}")
    # Append the process to the execution order
    execution_order.append(process_names[current_process])
    # If the process has completed execution, add it to the completed processes list
    if remaining_burst_times[current_process] <= 0:
        completed_processes.append(current_process)
    
# Print the execution order
print("Execution order: ", execution_order)

# Print the completion times of the processes
print("Completion times: ", completion_times)

# Print the average waiting time
print("Average waiting time: ", sum(completion_times) / NOP)

# Print the average turnaround time
print("Average turnaround time: ", sum(completion_times) / NOP)

# Print the total time taken to execute all processes
print("Total time taken to execute all processes: ", current_time)



