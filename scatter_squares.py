import matplotlib.pyplot as plt

x_values=list(range(1,1001))
y_values=[x**2 for x in x_values]

plt.scatter(x_values,y_values,edgecolor=None,s=40)

#Set chart title and label axes.
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of value",fontsize=14)

#Set the range for each axes
plt.axis([0,1100,0,1100000])

plt.show()