# Increasing Triangle Pattern 

"""
*
**
***
****
*****
"""

# n = 5 
# Square Pattern
# for i in range(n):
#     for j in range(n):
#         print('*', end=" ")
#     print() 

# Increasing Triangle
# for i in range(n): #counting rows
#     for j in range(i+1): #counting columns
#         print('*', end=" ")
#     print()


# Decreasing Triangle

'''
*****
****
***
**
*
'''
# for i in range(n): #counting rows
#     for j in range(i, n): #counting columns
#         print('*', end=" ")
#     print()

# Right sided triangle
'''
    *
   **
  ***
 ****
*****
'''
# n = 5
# for i in range(n): #counting rows
#     for j in range(i, n): #counting columns
#         print(' ', end=" ")
#     for j in range(i+1): #counting columns
#         print('*', end=" ")
#     print()

# Reverse Right sided triangle
'''
*****
 ****
  ***
   **
    *
'''
# n = 5
# for i in range(n): #counting rows
#     for j in range(i+1): #counting columns
#         print(' ', end=" ")
#     for j in range(i, n): #counting columns
#         print('*', end=" ")
#     print()

# Hill Pattern
"""
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 
"""
# n = 5

# for i in range(n): #counting rows
#     for j in range(i, n): #counting columns
#         print(' ', end=" ")
#     for j in range(i+1): #counting columns
#         print('*', end=" ")
#     for j in range(i): #counting columns
#         print('*', end=" ")
#     print()


# Reverse Hill Pattern
'''
  * * * *  * * * * * 
    * * *  * * * * 
      * *  * * * 
        *  * * 
           * 
'''
n = 5

for i in range(n): #counting rows
    for j in range(i + 1): #counting columns
        print(' ', end=" ")
    for j in range(i, n - 1): #counting columns
        print('*', end=" ")
    for j in range(i, n): #counting columns
        print('*', end=" ")
    print()