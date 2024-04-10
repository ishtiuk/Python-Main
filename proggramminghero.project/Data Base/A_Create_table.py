# 
# Before adding or extracting data from Table we have to create table, Right?

# so, to create a Table we have to do three simple things:
# 1. Type the keyword:  CREATE TABLE
# 2. Provide the name of the Table
# 3. Provide a collection of column name and data type.

# that's all

#         ||||||  CREATE TABLE  ||||||||

# so, suppose we are creating a Table named Users , and we'll put there id, email, password, friends number

# now, here id is INTEGER, email is TEXT that means string, password also TEXT, friends number is INTEGER


# now, the complete table creating query is:

# " CREATE TABLE Users (Id INTEGER Email TEXT Password TEXT Friends INTEGER) "
# _______________________________________________________________________________________

#  ||||||||||||||     Insert Data  ||||||||

# after Creating table we have to store or insert data there, Right?

# adding DAta means inserting data, that's why you will type " INSERT INTO " at first then the table name where you want to inset like this:>

# " INSERT INTO Users"

# and then just 3 steps:
# 1. Type the keyword ' VALUES '
# 2. Provide all the column data inside of first parenthisis "()".
# 3. YEah, separate each column data or datas by a comma (,) . 😎

# now, the complete table creating query is:

# " INSERT INTO Users VALUES (1, 'xys@protonmail.com', 'pwdfeR' 200) "
# _______________________________________________________________________________________


# make sure that provide datas depending on column number, like if there are 4 columns then provide 4 datas, 
# and careful to provide data, datas should match to that column's data type. 😎


#  ||||||||||||  Update DATA  |||||||||

# Imagine that our Users table's one user jhony's friends number has increased, so we want to Update that Data, right?

# to Update Data we have to do 5 things:
# 1. Type the keyword UPDATE
# 2. Then type the Table Name 
# 3. Type the keyword SET
# 4. Write the column name = the new value.
# 5. then type 'Where' clause to identify the rows. 

# now, the complete table creating query is:

# " UPDATE Users SET Friends = 300 Where Id = 3 "
# _____________________________________________________________________________________


# if Where clause condition matches with one row then it will update one row, if it matches with multiple rows then it will update on those multiple rows..

# and yeah, if you forget to use the 'Where' clause then it will update all the rows in the table like this:  " UPDATE Users SET Friends 500 " 🤣

# '🚫    So, never forget to use 'Where' clause when updating data, otherwise your whole DATAbase or Table will be wasted then you have to organize them again  🚫


# also, we can update multiple Columns data by separating with (,) like : " UPDATE Users SET Friends = 500, Password = 'dja' Where id = 3"
#________________________________

# hence, query can be written in multiple lines: 
# UPDATE Users
# SET 
#     Password = 'dja',
#     Friends = 500

# WHERE
#     Id = 3
#________________________________