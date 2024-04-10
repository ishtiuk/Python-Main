from matplotlib import pyplot as plt

ages = [22, 55, 22, 55, 40, 35, 44, 24, 44, 52, 80, 80, 102, 7, 7, 4, 3] 
bins = [0, 10, 20, 30, 40, 50, 60, 70]

plt.hist(ages, bins)
plt.show()