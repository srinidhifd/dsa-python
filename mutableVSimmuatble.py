# muatble vs immutable 

# mutables (change on same address) - list , dict , set , classes 

# immutable - int , str , float , bool , tuple

# id() address

x= 5 
print(id(x))
x=12
print(id(x))
x= 5 
print(id(x))


a=10
b=10
print(id(a))
print(id(b))