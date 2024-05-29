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

# dict - {key:value}

third_sem_marks={"Python":96,"IOT":82,"NOSQL":86,"C#":82}

# adding values
third_sem_marks["IOT-Lab"]=99
print(third_sem_marks)

# accessing values using keys
print(third_sem_marks["Python"])


# to remove value
del third_sem_marks["IOT-Lab"]
print(third_sem_marks)


# get() it wont return error if that key not present

print(third_sem_marks.get("IOT1",-1))


# set {} a = set() , unique values, unordered - very efficient faster access

n={1,2,3,4,5}

# add()
n.add(20)
print(n)


# remove
n.remove(20)
print(n)
