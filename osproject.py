import time
import os
import random
from enum import Enum
import tkinter as tk
from tkinter import messagebox, simpledialog
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



class State(Enum):
    READY = "Ready"
    RUNNING = "Running"
    WAITING = "Waiting"
    TERMINATED = "Terminated"



class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.state = State.READY
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.completion_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0



def fcfs(processes, root, canvas):
    print("Starting FCFS simulation...")
    current_time = 0
    completed = 0
    gantt = []

    processes.sort(key=lambda x: x.arrival_time)

    while completed < len(processes):
        for proc in processes:
            if proc.arrival_time <= current_time and proc.state != State.TERMINATED:
                if proc.state == State.READY:
                    proc.state = State.RUNNING
                    gantt.append((proc.pid, current_time))
                if proc.state == State.RUNNING:
                    proc.remaining_time -= 1
                    if proc.remaining_time <= 0:
                        proc.state = State.TERMINATED
                        proc.completion_time = current_time + 1
                        proc.turnaround_time = proc.completion_time - proc.arrival_time
                        proc.waiting_time = proc.turnaround_time - proc.burst_time
                        completed += 1
        update_display(processes, current_time, root, canvas, gantt, "FCFS")
        current_time += 1
        time.sleep(1)


def sjf(processes, root, canvas):
    print("Starting SJF simulation...")
    current_time = 0
    completed = 0
    gantt = []

    while completed < len(processes):
        available = [p for p in processes if p.arrival_time <= current_time and p.state != State.TERMINATED]
        if available:
            proc = min(available, key=lambda x: x.remaining_time)
            if proc.state == State.READY:
                proc.state = State.RUNNING
                gantt.append((proc.pid, current_time))
            if proc.state == State.RUNNING:
                proc.remaining_time -= 1
                if proc.remaining_time <= 0:
                    proc.state = State.TERMINATED
                    proc.completion_time = current_time + 1
                    proc.turnaround_time = proc.completion_time - proc.arrival_time
                    proc.waiting_time = proc.turnaround_time - proc.burst_time
                    completed += 1
        update_display(processes, current_time, root, canvas, gantt, "SJF")
        current_time += 1
        time.sleep(1)


def rr(processes, root, canvas, time_quantum=1):
    print("Starting Round Robin simulation...")
    current_time = 0
    completed = 0
    gantt = []
    queue = []
    i = 0

    while completed < len(processes):
        for proc in processes:
            if proc.arrival_time <= current_time and proc.state == State.READY and proc not in queue:
                queue.append(proc)

        if queue:
            proc = queue[i % len(queue)]
            if proc.state == State.READY:
                proc.state = State.RUNNING
                gantt.append((proc.pid, current_time))
            if proc.state == State.RUNNING:
                proc.remaining_time -= 1
                if proc.remaining_time <= 0:
                    proc.state = State.TERMINATED
                    proc.completion_time = current_time + 1
                    proc.turnaround_time = proc.completion_time - proc.arrival_time
                    proc.waiting_time = proc.turnaround_time - proc.burst_time
                    queue.remove(proc)
                    completed += 1
                elif random.random() < 0.2:
                    proc.state = State.WAITING
                    queue.remove(proc)
            i += 1
        for proc in processes:
            if proc.state == State.WAITING and random.random() < 0.3:
                proc.state = State.READY

        update_display(processes, current_time, root, canvas, gantt, "Round Robin")
        current_time += 1
        time.sleep(1)


def update_display(processes, current_time, root, canvas, gantt, algorithm):
    try:
        for widget in canvas.winfo_children():
            widget.destroy()

        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))

        data = {
            "PID": [p.pid for p in processes],
            "State": [p.state.value for p in processes],
            "Arrival": [p.arrival_time for p in processes],
            "Burst": [p.burst_time for p in processes],
            "Remaining": [p.remaining_time for p in processes]
        }
        df = pd.DataFrame(data)
        ax1.axis('tight')
        ax1.axis('off')
        table = ax1.table(cellText=df.values, colLabels=df.columns, loc='center')
        table.auto_set_font_size(False)
        table.set_fontsize(8)
        ax1.set_title(f"Time: {current_time} (Algorithm: {algorithm})")


        y = [0]
        for pid, start in gantt[-10:]:
            ax2.barh(y, 1, left=start, color=f"C{pid % 10}", edgecolor='black')
            ax2.text(start + 0.4, 0, f"P{pid}", ha='center', va='center')
        ax2.set_ylim(-0.5, 0.5)
        ax2.set_xlim(max(0, current_time - 10), current_time + 1)
        ax2.set_yticks([])
        ax2.set_xlabel("Time")
        ax2.set_title("Gantt Chart")

        canvas_widget = FigureCanvasTkAgg(fig, master=canvas)
        canvas_widget.draw()
        canvas_widget.get_tk_widget().pack()
        plt.close(fig)
        root.update()
    except Exception as e:
        print(f"Error in update_display: {e}")



def main():
    print("Initializing Process Scheduling Simulator...")
    try:
        root = tk.Tk()
        root.title("Process Scheduling Simulator")
        root.geometry("800x600")

        tk.Label(root, text="Select Scheduling Algorithm:").pack()
        algo_var = tk.StringVar(value="FCFS")
        algorithms = [("FCFS", "FCFS"), ("SJF", "SJF"), ("Round Robin", "RR")]
        for text, value in algorithms:
            tk.Radiobutton(root, text=text, variable=algo_var, value=value).pack()

        processes = []
        process_labels = []

        def clear_process_labels():
            for label in process_labels:
                label.destroy()
            process_labels.clear()

        def add_processes(num_processes):
            clear_process_labels()
            processes.clear()
            for pid in range(1, num_processes + 1):
                arrival = simpledialog.askinteger("Input", f"Arrival Time for Process {pid}:", parent=root, minvalue=0)
                if arrival is None:  # User canceled
                    return False
                burst = simpledialog.askinteger("Input", f"Burst Time for Process {pid}:", parent=root, minvalue=1)
                if burst is None:  # User canceled
                    return False
                processes.append(Process(pid, arrival, burst))
                label = tk.Label(root, text=f"Process {pid}: Arrival={arrival}, Burst={burst}")
                label.pack()
                process_labels.append(label)
                print(f"Added Process {pid}: Arrival={arrival}, Burst={burst}")
            return True

        canvas = tk.Canvas(root)
        canvas.pack(fill=tk.BOTH, expand=True)

        def start_simulation():
            print("Starting simulation...")
            algo = algo_var.get()
            num_processes = simpledialog.askinteger("Input", "Enter number of processes:", parent=root, minvalue=1)
            if num_processes is None:
                print("Simulation canceled: No number of processes provided")
                return
            if not add_processes(num_processes):
                print("Simulation canceled: Process input incomplete")
                messagebox.showwarning("Warning", "Process input was canceled.")
                clear_process_labels()
                processes.clear()
                return
            if not processes:
                messagebox.showerror("Error", "No processes added!")
                print("Error: No processes added")
                return
            if algo == "FCFS":
                fcfs(processes, root, canvas)
            elif algo == "SJF":
                sjf(processes, root, canvas)
            elif algo == "RR":
                rr(processes, root, canvas)
            print("Simulation completed")
            avg_wait = sum(p.waiting_time for p in processes) / len(processes)
            avg_turn = sum(p.turnaround_time for p in processes) / len(processes)
            messagebox.showinfo("Metrics",
                                f"Average Waiting Time: {avg_wait:.2f}\nAverage Turnaround Time: {avg_turn:.2f}")

        tk.Button(root, text="Start Simulation", command=start_simulation).pack()

        print("Entering mainloop...")
        root.mainloop()
    except Exception as e:
        print(f"Error in main: {e}")
        input("Press Enter to exit...")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Fatal error: {e}")
        input("Press Enter to exit...")