import numpy as np
import matplotlib.pyplot as plt

def estimated_coef(x,y):

    n= np.size(x)

    m_y = np.mean(y)
    m_x = np.mean(x)

    SS_xy = np.sum(y*x) - n*m_y*m_x
    SS_xx = np.sum(x*x) - n*m_x*m_x

    b_1 = SS_xy/SS_xx
    b_0 = m_y - b_1*m_x

    return b_0,b_1

def plot_regression_line(age,population,b):

    plt.scatter(age, population, color = "g", marker="*",s = 30)


    y_pred = b[0] + b[1]*age

    plt.plot(age, y_pred, color="b")

    plt.xlabel('age')
    plt.ylabel('population')

    plt.show()


def main():
    #observation
    age = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    population = np.array([40, 80, 90, 82, 65, 50, 35, 30, 15, 5])

    #estimating coefficient
    b = estimated_coef(age, population)
    print("Estimated coefficient:\nb_0 = {} \nb_1 = {}".format(b[0],b[1]))

    #plotting regression line
    plot_regression_line(age,population,b)

if __name__== '__main__':
    main()