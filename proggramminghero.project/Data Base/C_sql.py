# 
#   |\\  There are many kinds of Database management systems. like: MySQL, MongoDB, Oracle .....

#  hence, we'll learn SQL (Structured Querry Language)

#               in SQL we use table to store data in a organized way

#   Columns are Vertically and Rows are Horizontally  


#        ||||||||||   Selecting Column |||||| 

# to select all of the  Column in SQL we have to type  " Select * from (table name)"

# hence, we can select a specific Column by defining its name like " Select Name from (table name)"

# and we can also see or select multiple Columns at a time, like " Select Email, Password, Friends from Users"


#            |||||||||||   Selecting Row  ||||||||||||

# to select one specific Row we can use the 'Where' clause like " Select * from Users (table name) Where id = 2" 

# notice that here, 'Where' works almost like Python 'if' condition, we can give any conditon after 'Where' in SQL 

# to get all users that have more than 100 friends. You can write the query like below... 
# " Select * from Users Where friends < 100 "

#  and we can use multiple conditions after the 'Where' clause, using 'or'  'and' like>..

# " Select * from Users Where id > 3 and friends < 100"
# " Select * from Users Where id > 3 or friends > 100"



#  ||||||||||||||  SQL Functions |||||||||| 

# if we want to get the sum of every row, that means we want to add the values of every friends column's numbers

#  " SELECT SUM(Friends) From Users "

#  some SQL functions including SUM:
# 1. AVG()
# 2. COUNT()
# 3. FIRST()
# 4. LAST()
# 5. MAX()
# 6. MIN()
# 7. SUM()


# HERE, COUNT() is special if we pass any column name , it will return the Rows number of the selected Columns :D