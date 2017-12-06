import numpy as np

file = open("data/input_data.txt")
data = file.read()
list = list()
data = data.replace("\t"," ").replace("\n",";")
matrix = np.matrix(data)