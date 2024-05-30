# pattern based questions
# -------------------------------------------------------------------

# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 

# time complexity - O(n2)

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print("*",end=" ")
#     print()


# ---------------------------------------------------------------------

# *
# * *
# * * *
# * * * *
# * * * * *

# time complexity - 0(n2)

# for i in range(5):
#     for j in range(i):
#         print("*",end=" ")
#     print("*")

# ---------------------------------------------------------------------

# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 

# time complexity - 0(n2)

# for i in range(1,6):
#      for j in range(1,i+1):
#          print(j,end=" ")
#      print("")


# -------------------------------------------------------------------

# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5 

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()

# ---------------------------------------------------------------------
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

# n=5
# for i in range(n):
#     for j in range(n-i):
#         print("*",end=" ")
#     print()

# --------------------------------------------------------------------
# 1 2 3 4 5 
# 1 2 3 4 
# 1 2 3 
# 1 2 
# 1 

# n=5
# for i in range(n):
#     for j in range(1,n-i+1):
#         print(j,end=" ")
#     print()

# ------------------------------------------------------------------
#         * 
#       * * * 
#     * * * * * 
#   * * * * * * * 
# * * * * * * * * *

# n=5

# for i in range(n):
#     for j in range(n-1-i):
#         print(" ",end=" ")

#     for j in range(2*i+1):
#         print("*",end=" ")
    
#     print()

# ----------------------------------------------------------------
# * * * * * * * * * 
#   * * * * * * * 
#     * * * * * 
#       * * * 
#         * 

# n=5

# for i in range(n):
#     for j in range(i):
#         print(" ",end=" ")

#     for j in range(2*(n-1-i)+1):
#         print("*",end=" ")
    
#     print()



# -------------------------------------------------------------------

#         * 
#       * * * 
#     * * * * * 
#   * * * * * * * 
# * * * * * * * * * 
# * * * * * * * * * 
#   * * * * * * * 
#     * * * * * 
#       * * * 
#         * 

# n=5

# for i in range(n):
#     for j in range(n-1-i):
#         print(" ",end=" ")

#     for j in range(2*i+1):
#         print("*",end=" ")
    
#     print()

# n=5

# for i in range(n):
#     for j in range(i):
#         print(" ",end=" ")

#     for j in range(2*(n-1-i)+1):
#         print("*",end=" ")
    
#     print()


# -------------------------------------------------------------------------------------

# 1  
# 0 1  
# 1 0 1  
# 0 1 0 1  
# 1 0 1 0 1  

# n=5

# for i in range(n):
#     for j in range(i+1):
#         print((i+j+1)%2,end=" ")
#     print(" ")

# ------------------------------------------------------------------------------------


