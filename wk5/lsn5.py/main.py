import math


num = int(input())
try:
    a = math.sqrt(num)
    print(a)
except ValueError :
    print( 'nelzya' )