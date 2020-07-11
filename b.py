import numpy as np
import os
import cv2
import matplotlib.pyplot as plt
import tensorflow
import pickle


def read_file():
    f = open('names.txt')
    names_list = f.readlines()
    new_names = []
    for i in range(len(names_list)):
        new_names.append(str(names_list[i][:str(names_list[i]).find('.')]))
    print(new_names[3])
    f.close()
    return(new_names)


def create_traning_data(PATH, names):
    traning_data = []
    last = ""
    i = 0
    for name in names:
        img = cv2.imread(PATH + name+'.png', cv2.IMREAD_GRAYSCALE)
        last = img
        if last.shape[0] == 72:
            traning_data.append([img, i])
        i += 1
        print(name)

    return(traning_data)


if __name__ == "__main__":
    PATH = 'heroes/small/'
    names = read_file()
    data = create_traning_data(PATH, names)

    X = []
    y = []
    for featuers, label in data:
        print(featuers.shape)
        X.append(featuers)
        y.append(label)
    #X = np.array(X, dtype=object)
    X = np.array(X, dtype=object).reshape(-1, 72, 128, 1)
    print(X.shape)

    pickle_out = open("X.pickle", 'wb')
    pickle.dump(X, pickle_out)
    pickle_out.close()

    pickle_out = open("y.pickle", 'wb')
    pickle.dump(y, pickle_out)
    pickle_out.close()
