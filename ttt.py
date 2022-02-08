
#1st  -1
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time
import math

# 순환하지 않는 Case가 존재하여야 한다. 이를 종료Case라 한다.
# 모든 Case는 종료 Case로 수렴해야 한다.

def Factorial(number):
    if number <= 1 : return 1
    return number*Factorial(number-1)

def Pibonachi(number):
    if number <= 1 : return 1
    if number == 2 : return 1
    return Pibonachi(number-1) + Pibonachi(number-2)

def Power(x,n):
    if n <= 0  : return 1
    return x*Power(x,n-1)

def Gcd(m,n): # m > n 인 조건
    if m % n == 0 :
        return n
    return Gcd(n,m % n)   

def Search(string,n,target):
    if n < 0 : 
        return -1
    if string[n] == target : 
        return n
    return Search(string,n-1,target)

#a="12346665"
#print(Search(a,len(a)-1,'4'))


def Max(a,b):
    if a >= b : return a
    if a <  b : return b

def FindMax(n,data):
    if n <= 0 : 
        return data[0]
    return Max(data[n], FindMax(n-1,data))

#a=[1,2,3,5,4,3,2,1]
#print(FindMax(len(a)-1,a))

def PrintInBinary(number):
    if number < 2 : 
        print(number,end='') 
        return 1
    PrintInBinary(number//2)
    print(number%2,end='') 

#PrintInBinary(255)

a=[5,4,3,2,1]
b=[]
c=[]
print(a)
print(b)
print(c)
print("")

def Move(From,To):
    To.append(From.pop())
    print(a)
    print(b)
    print(c)    
    print("")
    time.sleep(0.1)

def Hanoi(N,From,To,via):
    if N==1 : 
        Move(From,To)
        return
    Hanoi(N-1,From,via,To)
    Move(From,To)
    Hanoi(N-1,via,To,From)
    
#Hanoi(5,a,c,b) 

DP = [0]*5000
def PibonachiDP(number):
    if number <= 1 : return 1
    if number == 2 : return 1
    if DP[number] != 0: return DP[number]

    DP[number] = PibonachiDP(number-1) + PibonachiDP(number-2)
    return DP[number]

#a=time.time()
#print(Pibonachi(40))
#b=time.time()
#print("time:{}".format(b-a))

#a=time.time()
#print(PibonachiDP(40))
#b=time.time()
#print("time:{}".format(b-a))


#Question Tile
#2xn 크기의 직사각형을 1x2, 2x1의 타일로 채우는 방법의 경우의 수를 10007로 나눈 나머지

def NTile1(n):
    if n == 1 : return 1
    if n == 2 : return 2
    if DP[n] != 0 : return DP[n]
    DP[n] =( NTile1(n-1) + NTile1(n-2))%10007
    return DP[n]

#print(NTile1(9))

#Question Tile
#2xn 크기의 직사각형을 1x2, 2x1, 2x2의 타일로 채우는 방법의 경우의 수를 10007로 나눈 나머지
def NTile2(n):
    if n == 1 : return 1
    if n == 2 : return 3
    if DP[n] != 0 : return DP[n]
    DP[n]= (NTile2(n-1) + 2*NTile2(n-2))%10007
    return DP[n]

#print(NTile2(8))

#Question Tile
#3xn 크기의 직사각형을 1x2, 2x1의 타일로 채우는 방법의 경우의 수를 10007로 나눈 나머지
#n이 짝수배로 늘어날때마다 경우의 수는 2가지씩 더 존재

def NTile3(n):

    if n == 1 : return 0
    if n == 2 : return 3
    if DP[n] != 0 : return DP[n]
    DP[n] = 3*NTile3(n-2)%10007
    for i in range(4,n):
        if i%2 == 0 :
            DP[n]+= 2*NTile3(n-i)%10007
    return DP[n]

#print(NTile3(100))

primeN = list(range(0,100001,1))

def EratosSieve(N):
    primeN[1] = 0
    endpoint = int(math.sqrt(N))
    for i in range(2,endpoint):
        if primeN[i] == 0 : continue
        for j in range(2*i,N,i):
            primeN[j] = 0 
    j = 0
    for i in range(2,N):
        if primeN[i] !=0:
            print('{:8d}'.format(primeN[i]),end=" ")
            j+=1
            if (j % 10) == 0 : 
                print("")

EratosSieve(100000)



