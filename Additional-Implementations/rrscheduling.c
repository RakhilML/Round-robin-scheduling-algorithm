#include <stdio.h>

#define MAX_PROCESSES 100
#define TIME_QUANTUM 2

struct Process {
    int pid;
    int burst_time;
    int arrival_time;
};

int front = 0, rear = -1, current_time = 0, total_processes = 0;
struct Process queue[MAX_PROCESSES];

void enqueue(struct Process p) {
    if (rear == MAX_PROCESSES - 1) {
        printf("Queue is full\n");
    } else {
        queue[++rear] = p;
        total_processes++;
    }
}

struct Process dequeue() {
    if (front > rear) {
        printf("Queue is empty\n");
    } else {
        return queue[front++];
    }
}

int isQueueEmpty() {
    return front > rear;
}

void runProcess(struct Process p) {
    for (int i = 0; i < p.burst_time; i++) {
        if (i == TIME_QUANTUM) {
            enqueue(p);
            break;
        }
        current_time++;
    }
}

int main() {
    struct Process p1 = {1, 5, 0};
    struct Process p2 = {2, 3, 1};
    enqueue(p1);
    enqueue(p2);
    while (!isQueueEmpty()) {
        struct Process currentProcess = dequeue();
        runProcess(currentProcess);
    }
    printf("Total time taken: %d\n", current_time);
    return 0;
}