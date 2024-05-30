# function - block of code use to perform certain task

# main feature - resuability

# def keyword is used to create a function 

# def summation(a,b,c):
#     print(a+b+c)

# summation(1,2,3)


def upd(lst):
    sum=0
    for i in range(len(lst)):
        lst[i]=lst[i]+1
        sum=sum+lst[i]
    print(lst)
    return sum

lst=[1,2,3]
res=upd(lst)
print(res)
print(lst)