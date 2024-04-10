
# we can make the best use of List of Tuples as a replacement of Dictionary Data Structure 😏

# I have learnt it from Google Python IT Automation course.....


lst_of_tuple = [('adam', 'smasher@gmail.com'), ('silverhand', 'silver@ca.com'), ('judy', 'judy@gmail.com'), 
                ('araska', 'arasaka@nc.com'), ('mikoshy', 'mikoshy@nc.com'), ('kiroshy', 'kiroshy@nc.com')]

# dict_of_tuple = {'adam': 'smasher@gmail.com', 'silverhand': 'silver@ca.com', 'judy': 'judy@gmail.com', 
#                 'araska': 'arasaka@nc.com', 'mikoshy': 'mikoshy@nc.com', 'kiroshy': 'kiroshy@nc.com'}       # instead of Dict we have used List of tuple 😏

for name, mail in lst_of_tuple:
    print("usr: {} |  email: {}".format(name, mail))


