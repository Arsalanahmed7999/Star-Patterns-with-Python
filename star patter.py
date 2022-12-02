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
  * * * * * * * * * 
    * * * * * * * 
      * * * * * 
        * * * 
          * 
'''
# n = 5

# for i in range(n): #counting rows
#     for j in range(i + 1): #counting columns
#         print(' ', end=" ")
#     for j in range(i, n - 1): #counting columns
#         print('*', end=" ")
#     for j in range(i, n): #counting columns
#         print('*', end=" ")
#     print()

# Diamond Pattern

'''
          * 
        * * * 
      * * * * * 
    * * * * * * * 
  * * * * * * * * * 
    * * * * * * * 
      * * * * * 
        * * * 
          * 
'''

# n = 5
# for i in range(n-1): #counting rows
#     for j in range(i, n): #counting columns
#         print(' ', end=" ")
#     for j in range(i+1): #counting columns
#         print('*', end=" ")
#     for j in range(i): #counting columns
#         print('*', end=" ")
#     print()
# for i in range(n): #counting rows
#     for j in range(i + 1): #counting columns
#         print(' ', end=" ")
#     for j in range(i, n - 1): #counting columns
#         print('*', end=" ")
#     for j in range(i, n): #counting columns
#         print('*', end=" ")
#     print()

# Butterfly Pattern
'''
*                     * 
* *                 * * 
* * *             * * * 
* * * *         * * * * 
* * * * *     * * * * * 
* * * *         * * * * 
* * *             * * * 
* *                 * * 
*                     * 

'''
# n = int(input('Enter the value n: \n'))
# for i in range(n - 1):
#   for j in range(i+1):
#     print('*', end=' ')
#   for j in range(i, n - 1):
#     print(' ', end=' ')
#   for j in range(i, n -1):
#     print(' ', end=' ')
#   for j in range(i + 1):
#     print('*', end=' ')
#   print()
# for i in range(n):
#   for j in range(i, n):
#     print('*', end=' ')
#   for j in range(i):
#     print(' ', end=' ')
#   for j in range(i):
#     print(' ', end=' ')
#   for j in range(i, n):
#     print('*', end=' ')
#   print()

# Sandglass Pattern
'''
  * * * * * * * * * 
    * * * * * * * 
      * * * * * 
        * * * 
          * 
          * 
        * * * 
      * * * * * 
    * * * * * * * 
  * * * * * * * * * 
'''

# n = int(input('Enter the value n: \n'))
# # n = 5

# for i in range(n):

#   for j in range(i+1):
#     print(' ', end=' ')
#   for j in range(i, n-1):
#     print('*', end=' ')
#   for j in range(i, n):
#     print('*', end=' ')
#   print()
# for i in range(n):

#   for j in range(i ,n):
#     print(' ', end=' ')
#   for j in range(i+1):
#     print('*', end=' ')
#   for j in range(i):
#     print('*', end=' ')
#   print()


# Double Hill Pattern
'''

          *                 * 
        * * *             * * * 
      * * * * *         * * * * * 
    * * * * * * *     * * * * * * * 
  * * * * * * * * * * * * * * * * * * 
'''

