import numpy as np
import matplotlib.pyplot as plt

class regression():

    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.slop=0
        self.intersept=0

    def mean(self):
        return np.mean(self.x),np.mean(self.y)
    
    def fit(self):
        num,den=0,0
        x_mean,y_mean=self.mean()
        for i in range(len(self.x)):
            num+=(self.x[i]-x_mean) * (self.y[i]-y_mean)
            den+=(self.x[i]-x_mean)**2
        self.slop=num/den
        self.intersept=y_mean-(self.slop*x_mean)

    def regression_line(self):
        plt.scatter(self.x,self.y,color='red')
        plt.plot(self.x,(self.slop*self.x)+self.intersept,color = 'green')

    def pridict(self,x):
        return (self.slop*x)+self.intersept
    
    def plot_pridic_line(self,x,y):
        plt.scatter(x,y,color='red')
        plt.plot(x,(self.slop*x)+self.intersept)

    def accuracy(self,x,y):
        x_mean,y_mean = self.mean()
        num,den=0,0
        for i in range(len(x)):
            pred=(self.slop*x[i])+self.intersept
            num+=(y[i]-pred)**2
            den+=(y[i]-y_mean)**2
        r2=1-(num/den)
        return r2