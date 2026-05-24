import time
import os
import concurrent.futures
import multiprocessing
import threading
import psutil
import matplotlib.pyplot as plt
from datetime import timedelta
import numpy as np

# -------- Utility Functions -------- #

def format_time(seconds):
    """Format time as H:M:S:ms"""
    ms = int((seconds - int(seconds)) * 1000)
    return str(timedelta(seconds=int(seconds))) + f":{ms:03d}"

def heavy_task(n):
    """CPU-bound task."""
    s = 0
    for i in range(500_000_00):  # Adjustable workload
        s += (i ** 2) % (n + 1)
    return s

def record_cpu_usage(history, stop_event):
    """Records CPU usage of all cores until stop_event is set."""
    start_time = time.time()
    while not stop_event.is_set():
        usage = psutil.cpu_percent(interval=0.1, percpu=True)
        elapsed = time.time() - start_time
        history.append((elapsed, usage))

def measure_runtime(func, label, all_results, *args):
    """Run a function, record CPU usage, and measure runtime."""
    cpu_history = []
    stop_event = threading.Event()
    monitor = threading.Thread(target=record_cpu_usage, args=(cpu_history, stop_event))
    monitor.start()

    start = time.time()
    func(*args)
    end = time.time()

    stop_event.set()
    monitor.join()

    duration = end - start
    all_results[label] = cpu_history
    return duration


# -------- Parallelism Modes -------- #

def run_threading(workers, iterations):
    threads = []
    for i in range(workers):
        t = threading.Thread(target=heavy_task, args=(iterations,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

def run_multiprocessing(workers, iterations):
    with multiprocessing.Pool(workers) as pool:
        pool.map(heavy_task, [iterations] * workers)

def run_interpreters_simulated(workers, iterations):
    # Simulate interpreter-level parallelism (no GIL)
    with multiprocessing.Pool(workers) as pool:
        pool.map(heavy_task, [iterations] * workers)


# -------- Plot Function (merged) -------- #

def plot_combined(all_results, methods, times):
    """Plot efficiency + CPU usage in one figure."""
    fig = plt.figure(figsize=(10, 10))
    gs = fig.add_gridspec(len(all_results) + 1, 1, height_ratios=[1.2] + [1]*len(all_results))
    
    # --- Efficiency Plot ---
    min_time = min(times)
    efficiency = [(min_time / t) * 100 for t in times]
    ax0 = fig.add_subplot(gs[0])
    bars = ax0.bar(methods, efficiency, color=["orange", "green", "blue"])
    ax0.set_title("Execution Efficiency & CPU Usage (GIL vs Parallelism vs Interpreters)")
    ax0.set_ylabel("Efficiency (%)")
    ax0.set_ylim(0, 110)
    for bar, eff, t in zip(bars, efficiency, times):
        ax0.text(bar.get_x() + bar.get_width()/2, eff + 2, f"{eff:.1f}%\n{format_time(t)}",
                 ha="center", va="bottom", fontsize=9)

    # --- CPU Usage Plots ---
    for idx, (title, history) in enumerate(all_results.items(), start=1):
        ax = fig.add_subplot(gs[idx])
        if not history:
            continue

        times_sec = [h[0] for h in history]
        usage_per_core = list(zip(*[h[1] for h in history]))

        # Plot each core
        for core, usage in enumerate(usage_per_core):
            ax.plot(times_sec, usage, label=f"Core {core}")

        ax.set_title(title)
        ax.set_ylabel("CPU %")
        ax.set_ylim(0, 100)
        ax.legend(loc="upper right", fontsize=8)
        ax.grid(True)

    ax.set_xlabel("Time (HH:MM:SS:ms)")

    # --- Convert x-axis to formatted time ---
    def format_x(x, pos):
        return format_time(x)
    from matplotlib.ticker import FuncFormatter
    ax.xaxis.set_major_formatter(FuncFormatter(format_x))

    plt.tight_layout()
    plt.show()


# -------- Main -------- #

if __name__ == "__main__":
    cores = os.cpu_count() or 4
    iterations = 5
    print(f"Detected {cores} CPU cores 🧠")

    all_results = {}

    print("\nRunning Threading (GIL-limited)...")
    threading_time = measure_runtime(run_threading, "Threading (GIL)", all_results, cores, iterations)

    print("Running Multiprocessing (True Parallelism)...")
    multiprocessing_time = measure_runtime(run_multiprocessing, "Multiprocessing", all_results, cores, iterations)

    print("Running Interpreters (Simulated)...")
    interpreters_time = measure_runtime(run_interpreters_simulated, "Interpreters (Sim)", all_results, cores, iterations)

    methods = ["Threading (GIL)", "Multiprocessing", "Interpreters (Sim)"]
    times = [threading_time, multiprocessing_time, interpreters_time]

    print("\n=== Execution Summary ===")
    for method, t in zip(methods, times):
        print(f"{method:<20}: {format_time(t)}")

    plot_combined(all_results, methods, times)
