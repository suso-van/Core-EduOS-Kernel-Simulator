import matplotlib.pyplot as plt

def plot_gantt(gantt):
    fig, ax = plt.subplots()

    for pid, start, end in gantt:
        ax.barh(y=pid, width=end - start, left=start)

    ax.set_xlabel("Time")
    ax.set_ylabel("Process ID")
    ax.set_title("CPU Scheduling Gantt Chart")
    plt.show()

def plot_page_faults(faults_over_time):
    plt.plot(faults_over_time)
    plt.xlabel("Time")
    plt.ylabel("Cumulative Page Faults")
    plt.title("Page Fault Growth")
    plt.show()
