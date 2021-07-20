#fibb = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ... ]
import keras


ciagFib = [0,1] # definiuje dwa pierwsze wyrazy ciągu

def fibonacci(a):

    nowa_liczba = 0 #
    for i in range(a):
        nowa_liczba = ciagFib[-1] + ciagFib[-2]  # obliczam nową liczbe jako sume dwóch ostatnich liczb z ciągu
        ciagFib.append(nowa_liczba)  # dodaje nową liczbe do listy
        print (nowa_liczba)
#a = int(input()) # 12 "12"
#fibonacci(a)    #sprawdzenie


x = int(input())
y = int(input())
def whiteOrBlack():
  if (x%2 and y%2) or (x%2 == 0 and y%2 == 0):
     return False
  else:
     return True

print(whiteOrBlack())
# obie parzyste lub obie nieparzyste