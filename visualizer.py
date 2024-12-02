import matplotlib.pyplot as plt

def plot_data(ax, x, y, title, xlabel, ylabel):
    ax.clear()
    ax.plot(x, y, label=title)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.legend()
    ax.grid(True)
