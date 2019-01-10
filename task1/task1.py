import numpy
import matplotlib.pyplot

file = open('task_1_capital.txt', 'r')
file.readline()
lines = file.read().splitlines()
x = []
y = []
for line in lines:
    x.append(int(line.split('\t\t')[0]))
    y.append(int(line.split('\t\t')[1]))
x_matrix = numpy.array([[i, 1] for i in x])
x_matrix.shape = (len(x), 2)
y_matrix = numpy.array(y)

result = numpy.linalg.inv(x_matrix.T.dot(x_matrix)).dot(x_matrix.T.dot(y_matrix))

for i, j in zip(x, y):
    matplotlib.pyplot.scatter(i, j, c='blue')
a = [0, max(x)]
b = [result[1], result[0] * max(x) + result[1]]

matplotlib.pyplot.plot(a, b, c='black')

matplotlib.pyplot.show()