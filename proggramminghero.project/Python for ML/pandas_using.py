import pandas
import numpy as np


data = np.array(["H", "E", "R", "O"])
serie = pandas.Series(data)
print(serie[0])
print(serie[1:])
print(serie)



file = pandas.read_csv('D:\\pip main\\proggramminghero.project\\Python for ML\\data.csv')

series1 = pandas.Series(file["Product_Names"])
series2 = pandas.Series(file["Price"])

# print(datafrm)




