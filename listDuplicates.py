mylist = int(input("What is the length of the list?\n"))
lista = []
for i in range(mylist):
    lista.append(input("Enter the item: "))

newlist = []
duplist = []
for i in lista:
    if i not in duplist and i not in newlist:
        newlist.append(i)
    elif i in newlist and i not in duplist:
        duplist.append(i)
    elif i in duplist and i  in newlist:    
        pass
        
print("Duplicated Item List", duplist)
print("Unique Item List", newlist)