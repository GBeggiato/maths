import numpy as np
import matplotlib.pyplot as plt
from os import system, name


def hitomezashi(X: np.ndarray, Y: np.ndarray, borders=True, c=None):
    '''code to generate the plot, starting from binary arrays-like X and Y
    toggle "borders" for borders and "c" for a monochromatic plot'''
    plt.figure()
    if borders: # frame
        plt.plot([0, len(X)-1], [0, 0], color=c) 
        plt.plot([0, len(X)-1], [len(Y)-1, len(Y)-1], color=c)
        plt.plot([0, 0], [0, len(X)-1], color=c)
        plt.plot([len(Y)-1, len(Y)-1], [0, len(X)-1], color=c)
    row = 0 # horizontal lines
    for y in Y:
        j = 0 if y==1 else 1
        while j < len(X)-1:
            plt.plot([j, j+1], [row, row], color=c)
            j += 2
        row += 1
    col = 0 # vertical lines
    for x in X:
        j = 0 if x==1 else 1
        while j < len(Y)-1:
            plt.plot([col, col], [j, j+1], color=c)
            j += 2
        col += 1
    plt.yticks(range(len(Y)), [str(i) for i in Y]) # final plt touches
    plt.xticks(range(len(X)), [str(i) for i in X])
    plt.title("Hitomezashi Stitch Patterns")
    plt.show()


def main():
    rand = np.random.RandomState(seed=4628)
    tot = 30
    P = None #[0, 1]
    axis = rand.choice([0, 1], p=P, size=(2, tot))
    X = axis[0]
    Y = axis[1]

    hitomezashi(X, Y, c="k")
        

if __name__=="__main__":
    main()

