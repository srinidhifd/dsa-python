name=input("Enter you name:")
print("My Name is ", name)

#converting string to integer
n=int(input("enter number"))

#converting string to floating value
n=float(input("enter radius"))


#type() is used to check datatype of value
print(type(name))
print(type(n))
print(type(True))
print(type(4))

#cannot convert hello to int ,it will throw error
#print(int("hello"))

#to take multiple values give as input storing as list
#assuming it will be space separated
val=input().split(" ")

#taking multiple input , assigning them to individual values
#3 5 7 if space separated
a,b,c=map(int,input().split(" "))

#if lot of values to be taken as input in list and add in list/tuple/set
# list(),tuple(),set()
# 1,2,3,4,5,6,7,8,9
lst=list(map(int,input().split(",")))