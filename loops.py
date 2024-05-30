# Loops in python 

# for 

# while

# there is no do-while in python 

# parts of loop - condition , operation , updation

# while condition:
#incre/decre

# for variable in SEQUENCE:

# range(start,end,step) , "end" is always one element less

# for i in lst1:
# lst=[3,6,1,9,23,56]
# for i in range(len(lst)):
#     print("Index :" , i , "value :", lst[i])


#linear search
k=23
lst=[3,6,1,9,23,56]
for i in range(len(lst)):
    if lst[i] == k:
        loc=i
        break
print("element found at",loc,"location")