import os
import matplotlib

import numpy as np
import matplotlib.pyplot as plt


def set_plot_labels(title: str="Graph Title", x_label: str="X-Label", y_label: str=" Y-Label"):
    # Plot Title
    plt.title(title)

    # Label X-axis and Y-axis
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    
    return 


def main():
    set_plot_labels("Main Graph", "X", "Y")

    inputs = np.linspace(0, 40, 100)
    f = lambda x: x**x
    outputs = [f(a) for a in inputs]

    plt.plot(inputs, outputs, color='blue', label="main function")

    plt.legend()
    plt.show()


    for _ in range(len(inputs)):
        print(f"{inputs[_]} -> {outputs[_]}")
    return

if __name__ == '__main__':
    main()
