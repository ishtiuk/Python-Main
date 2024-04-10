from matplotlib import pyplot as plt

# plt.scatter(["jhonny", "judy", "evlyen", "takmura"], [35, 23, 28, 50])
plt.plot(["jhonny", "judy", "evlyen", "takmura"], [35, 23, 28, 50])
plt.bar(["jhonny", "judy", "evlyen", "takmura"], [35, 23, 28, 50])

plt.title("Graph of Ages")
plt.xlabel("<--- Names --->")
plt.ylabel("<--- Ages --->")

plt.show()