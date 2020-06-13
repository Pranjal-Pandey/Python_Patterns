"""
Pattern 1: Square of Stars
    * * * * *
    * * * * *
    * * * * *
    * * * * *
    * * * * *

"""
number_of_rows = int(input("Enter the number of rows you want ?"))
for i in range(number_of_rows):
    print('* ' * number_of_rows)

""" 
Pattern 2: Square Pattern of any Number
    5 5 5 5 5 
    5 5 5 5 5 
    5 5 5 5 5 
    5 5 5 5 5 
    5 5 5 5 5 

"""
number_of_rows = int(input("Enter the number of rows you want ?"))
for i in range(number_of_rows):
    print('5 ' * number_of_rows)

""" 
Pattern 3: Square Pattern according to input value
    1 1 1 1 1
    2 2 2 2 2
    3 3 3 3 3
    4 4 4 4 4
    5 5 5 5 5

"""
# Nested For loops
number_of_rows = int(input("Enter the number of rows you want ?"))
for i in range(1, number_of_rows+1):
    for j in range(number_of_rows):
        print(str(i) +' ' ,end='')
    print()

#Single for loop
number_of_rows = int(input("Enter the number of rows you want ?"))
for i in range(1, number_of_rows+1):
    print((str(i)+ ' ') * number_of_rows)

""" 
Pattern 4: Square Pattern from Alphabets
    A A A A A
    A A A A A
    A A A A A 
    A A A A A
    A A A A A

"""
number_of_rows = int(input("Enter the number of rows you want ?"))
for i in range(number_of_rows):
    print((str(chr(65)) + ' ') * number_of_rows)

""" 
Pattern 5: Half Pyramid
    *
    * *
    * * * 
    * * * *
    * * * * *

"""
number_of_rows = int(input("Enter the number of rows you want ?"))
for i in range(number_of_rows+1):
    print("* " * i)

""" 
Pattern 6: Half Pyramid of numbers
    1
    1 1
    1 1 1 
    1 1 1 1
    1 1 1 1 1

"""
number_of_rows = int(input("Enter the number of rows you want ?"))
for i in range(number_of_rows+1):
    print("1 " * i)

""" 
Pattern 7: Half Pyramid of numbers(Version 2)
    1
    1 2
    1 2 3 
    1 2 3 4
    1 2 3 4 5

"""
number_of_rows = int(input("Enter the number of rows you want ?"))
for i in range(1, number_of_rows+1):
    j = 1
    while j <= i:
        print(j, end=' ')
        j += 1
    print()

"""
Pattern 8: Half Pyramid of Alphabets
    A
    A A
    A A A 
    A A A A
    A A A A A

"""
number_of_rows = int(input("Enter the number of rows you want ?"))
for i in range(number_of_rows+1):
    print((str(chr(65)) + ' ') * i)

"""
Pattern 9: Half Pyramid of Alphabets(version 2)
    A
    A B
    A B C 
    A B C D
    A B C D E

"""
number_of_rows = int(input("Enter the number of rows you want ?"))
for i in range(number_of_rows+1):
    j = 0
    while j <= i:
        print(str(chr(65 + j)) + ' ', end='')
        j += 1

    print()

"""
Pattern 10: Half Pyramid of Alphabets(version 3)
A 
B B 
C C C 
D D D D 
E E E E E 


"""

number_of_rows = int(input("Enter the number of rows you want ?"))
for i in range(number_of_rows):
    j = 0
    while j <= i:
        print(str(chr(65 + i)) + ' ', end='')
        j += 1

    print()


"""
Pattern 11
Triangle Version 1
      1 
     2 2 
    3 3 3 
   4 4 4 4 
  5 5 5 5 5 
 6 6 6 6 6 6 
7 7 7 7 7 7 7

"""
n = int(input("Enter the number of rows you want ?"))

for i in range(n):
    # print("i =",i)
    k = 0
    for j in range((2 * n) + 1):

        if(i + j) % 2 != 0 and k <= i and j >= (n - 1) - i:
            # print('p =',j)
            print(i + 1, end='')
            k += 1
        else:
            # print('j =',j)
            print(' ', end='')

    print()
"""
Pattern 12: Diamond

        *
       * *
      * * *
     * * * *
    * * * * *
     * * * *
      * * *
       * *
        *

"""

n = int(input("Enter the number of rows you want ?"))

for i in range(n):
    k = 0
    for j in range((2 * n) - 1):

        if (n-(i + j)) % 2 != 0 and k <= i and j >= (n - 1) - i:

            print('*', end='')
            k += 1
        else:
            print(' ', end='')

    print()
for i in range(n, (2 * n) - 1):
    s = (2 * n) - 1

    for j in range((2 * n)):
        if (n-(i + j)) % 2 != 0 and s > i and j > (i - n):
            print('*', end='')
            s -= 1
        else:
            print(' ', end='')

    print()

"""
Pattern 13: Inverted Half Pyramid

    * * * * *
    * * * *
    * * *
    * *
    *

"""

n = int(input("Enter the number of rows you want ?"))
while n > 0:
    print('* ' * n, end='')
    n -= 1
    print()

"""
Pattern 14: Numerical Inverted Half Pyramid
    1 2 3 4 5
    1 2 3 4
    1 2 3 
    1 2
    1

"""
"Method 1-Multiple for loop"
n = int(input("Enter the number of rows you want ?"))
for i in range(n, 0, -1):
    for x in range(1, i + 1):
        print(x, end=' ')
    print()

"Method 2- Single loop"
n = int(input("Enter the number of rows you want ?"))
for i in range(n, 0, -1):
    print(*range(1, i+1), end=' ')
    print()

"""
Pattern 15- Numerical Pyramid(Model 1) 
                  1 
                2 1 2 
              3 2 1 2 3 
            4 3 2 1 2 3 4 
          5 4 3 2 1 2 3 4 5

"""
n = int(input("Enter the number of rows you want ?"))
for i in range(0, n):
    s = n
    k = 1
    for j in range(0, (2*n)-1):
        if (i+j) >= s-1 and k <= 1:
            print(*range(i+1, 0, -1), end=' ')
            print(*range(2, i+2), end=' ')
            k += 1
            s -= 1
        else:
            print('  ', end='')
    print()


"""
Pattern 16:
        E
       E D
      E D C
     E D C B
    E D C B A
"""


import string
n = int(input("Enter the number of rows you want ?"))
for i in range(n):
    k=1
    s=0
    for j in range((2*n)-1):
        if (n-(i+j)) % 2 != 0 and (i+j) >= n-1 and k <= i+1:
            print(string.ascii_uppercase[n-1-s], end='')
            k += 1
            s += 1
        else:
            print(' ', end='')
        print()







