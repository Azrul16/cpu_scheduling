class Process:
    def __init__(self, pid, arrival_time, burst_time, priority):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority  # Higher number = higher priority
        self.remaining_time = burst_time
        self.completion_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0

def get_processes():
    processes = []
    n = int(input("Enter number of processes: "))
    for i in range(n):
        pid = f"P{i+1}"
        at = int(input(f"Enter arrival time for {pid}: "))
        bt = int(input(f"Enter burst time for {pid}: "))
        prio = int(input(f"Enter priority for {pid} (higher number = higher priority): "))
        processes.append(Process(pid, at, bt, prio))
    return processes

def calculate_metrics(processes):
    for p in processes:
        p.turnaround_time = p.completion_time - p.arrival_time
        p.waiting_time = p.turnaround_time - p.burst_time

def print_results(processes, quantum):
    print(f"\nPriority-Based Round Robin (Q={quantum}) Results:")
    print("PID | Arrival | Burst | Priority | Completion | Turnaround | Waiting")
    for p in sorted(processes, key=lambda x: x.pid):
        print(f"{p.pid:3} | {p.arrival_time:7} | {p.burst_time:5} | {p.priority:8} | {p.completion_time:10} | {p.turnaround_time:10} | {p.waiting_time:7}")
    
    avg_tat = sum(p.turnaround_time for p in processes) / len(processes)
    avg_wt = sum(p.waiting_time for p in processes) / len(processes)
    print(f"\nAverage Turnaround Time: {avg_tat:.2f}")
    print(f"Average Waiting Time: {avg_wt:.2f}")

def priority_round_robin():
    processes = get_processes()
    quantum = int(input("Enter time quantum: "))
    time = 0
    completed = 0
    ready_queues = {}  # Dictionary to hold queues for each priority level
    
    # Initialize separate queues for each priority level
    priorities = sorted(list({p.priority for p in processes}), reverse=True)
    for prio in priorities:
        ready_queues[prio] = []
    
    while completed != len(processes):
        # Add arriving processes to their respective priority queues
        for p in processes:
            if p.arrival_time <= time and p.remaining_time > 0 and p not in ready_queues[p.priority]:
                ready_queues[p.priority].append(p)
        
        # Check queues from highest to lowest priority
        current = None
        for prio in priorities:
            if ready_queues[prio]:
                current = ready_queues[prio].pop(0)
                break
        
        if not current:
            time += 1
            continue
        
        # Execute for time quantum or remaining time
        exec_time = min(quantum, current.remaining_time)
        time += exec_time
        current.remaining_time -= exec_time
        
        if current.remaining_time == 0:
            current.completion_time = time
            completed += 1
        else:
            ready_queues[current.priority].append(current)
    
    calculate_metrics(processes)
    print_results(processes, quantum)

if __name__ == "__main__":
    print("=== Priority-Based Round Robin Scheduling ===")
    print("Note: Higher priority numbers indicate higher priority\n")
    priority_round_robin()