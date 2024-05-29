# operations that can be performed on string , list , tuple , dict , set

# string is immuatble , we can never change/ edit string

# concatenation can be done on string 

a="abc"
b="efg"
c=a+b
print(c)

# list operations - append() , insert() , pop() , remove() , update

lst=[1,2,3,4,5]

#append at last
lst.append(25)
print(lst)

#insert anywhere insert(position,value)
lst.insert(0,11)
print(lst)

#pop from last by default
lst.pop()
print(lst)

#update
lst[0]=0
print(lst)

#remove
lst.remove(5)
print(lst)


# tuple is immutable , we can just access the values