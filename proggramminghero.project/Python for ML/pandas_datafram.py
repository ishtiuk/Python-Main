import pandas

file = pandas.read_csv('D:\\pip main\\proggramminghero.project\\Python for ML\\ipHone_price.csv')

series_names = pandas.Series(file["Devices"])
series_prices = pandas.Series(file["Prices"])


empty_dataframe = pandas.DataFrame()
# print(empty_dataframe.info())


dataframe_using_list = pandas.DataFrame(["Jhon", "Sam", "Silver", "Judy"])
# print(dataframe_using_list)



lst = {
    "TV": [45444, 34443, 86865, 28888], 
    "Mobile": [1222, 8866, 6664, '777'],
    "Speakers": [332, 45, 566, 71]
}

dataframe_using_dictionary = pandas.DataFrame(lst)
print(dataframe_using_dictionary)




datafram_from_csv = pandas.read_csv('D:\\pip main\\proggramminghero.project\\Python for ML\\ipHone_price.csv', index_col=0)
print(datafram_from_csv.head())

print(datafram_from_csv.tail())

print(datafram_from_csv.info())