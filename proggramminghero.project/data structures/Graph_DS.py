#
# We have seen the Google Map or any ordinary Papper Map, Right? 🙂

# What we can see there? Some Cities connected with Roads , Right? (Hence, many other things we can see also 😉)


# now let's Compare :) 

# Think of City as a 'Node'. Where a 'Node' has a name and some extra information like latitude and longitude..   || city as Node ||

# And think the roads as different lines, arcs or edges that connects two "Nodes" (two cities).    || roads as Edges || 


 
#            ======  Grpah Defination  ========

# When you have multiple "Nodes" connected via edges that's called a Graph, look at the "Graph_DS_1.jpg" in this directory 😎



#            ========  Directed Graph ========

# In some big cities, you might have seen one-way roads. That means you can go only one direction through those Roads. 
# And some roads have two direction also

# Similarly, if the lines or edges have any in a Graph, the that 'Graph' is called a 'Directed Graph'. (look at the "Graph_DS_2.jpg" in this directory)



#  ========= Existing Elements of a Graph DS ========

# Graph contains two things: 

#  1. Nodes
#  2. Edges



quuz = input('''What does a graph have? 
A. Color and lights
B. Nodes and Edges
C. Google Map
:-->> ''').upper()

if quuz == 'B':
    print('Correct Answer, Sir')
else:
    print('Wrong Answer, Sir')


#           A 'Graph' has Nodes and Edges. 


# if you make multi-city travel plan, that's also a Graph Data Structure :)  

## look at the "Graph_DS_3.jpg"

#
#