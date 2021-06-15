import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl

#zad1
data = pd.read_csv('flags.csv', header=0, sep=';')
df = pd.DataFrame(data)
df2 = pd.DataFrame(data)
df2 = df2.iloc[60:136]
dane = (df2.groupby(['Religion']).agg({'Religion': ['count']}))
print(dane)
wyk = dane.plot.bar()
wyk.set_xlabel('Oś x')
wyk.set_ylabel('Oś y')
plt.title('Dane')
plt.savefig('zadanie_w.png')
plt.show()


#zad2
plt.subplot(1,3,1)
x = np.arange(-3,3.1,0.1)
plt.plot(x, 4*x**2-5*x+12,color='r', label='f(x)=4*x^2-5*x+12')
plt.axis([-3,3,10,30])
plt.title('Pierwszy wykres')
plt.legend(loc='upper center')
plt.grid()
plt.subplot(1,3,2)
plt.scatter(x, x**2/(10+x)+20,color='c',label='f(x)=x^2/(10+x)+20')
plt.axis([-3,3,19.9,21.2])
plt.title('Drugi wykres')
plt.grid()
plt.legend(loc='lower center')

plt.subplot(1,3,3)
plt.plot(x, 4*x**2-5*x+12,color='r', label='f(x)=4*x^2-5*x+12')
plt.scatter(x, x**2/(10+x)+20,color='c',label='f(x)=x^2/(10+x)+20')
plt.axis([-3,3,10,30])
plt.legend(loc='upper center')
plt.grid()
plt.show()
#zad4
data = pd.read_csv('flags.csv', sep=';')
df1 = pd.DataFrame(data)
df2 = pd.DataFrame(data)
df2 = df2.iloc[60:136]
x = np.random.randint(25, 200, 75)
w3 = sns.relplot(data=df2, x=df2['Area'], y=x,
                      hue=df2['Population'], palette='muted', legend=True)
w3.fig.set_size_inches(12, 12)
w3.set_ylabels('os y')
plt.legend()
plt.title("Wykres")
plt.show()

data = pd.read_csv('flags.csv', sep=';')
df1 = pd.DataFrame(data)
df2 = pd.DataFrame(data)
df2 = df2.iloc[60:136]
x1 = np.random.randint(25, 200, 75)

w3 = sns.relplot(data=df2, x=df2['Area'], y=x1,
                   hue=df2['Population'], palette='muted', legend=True)
w3.fig.set_size_inches(10, 10)
w3.set_ylabels('os y')
plt.legend(loc='upper right')
plt.title("Wykres")
plt.show()