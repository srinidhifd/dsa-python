#basic maths quetions

# count digits in the number 

def countNumber(num):
    count=0
    while num>0 :
        num=num//10
        count=count+1
    return count
    # return len(str(num))

num=int(input())
res=countNumber(num)
print(res)