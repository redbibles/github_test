
#1st  -1
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time

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
    
Hanoi(5,a,c,b) 