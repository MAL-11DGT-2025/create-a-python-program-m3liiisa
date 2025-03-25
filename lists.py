#colours = ['red', 'green', 'blue', 'yellow', 'purple']
#print(colours[0]) #this prints the first colour red.
#print(colours[1])

#for i in colours:
 #   print(i)  #this prints the whole list

#print(colours[-1])  #this outputs the last colour in the list

#print(len(colours))  #this tells us how many colours are on the list

#for i in colours:
 #   if i == 'yellow':
  #      print('There is yellow') #this will only print if 'yellow' is on the list.


colours = []
print(colours)
colours.append('green') #this adds the item 'green' to the list
print(colours)
colours.append('blue') #adds blue to the list that already has green
print(colours)
print(colours[1]) #prints the 2nd item (1st position) in the list
print(len(colours)) #prints how many items in the list
colours.append('green')
colours.append('green')
print(colours)
print(colours.count('green')) #counts how many green items there are on the list.
colours.sort()
print(colours) #this sorts the items from least to most
