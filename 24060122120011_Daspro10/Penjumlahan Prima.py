# NAMA  : NAUFAL RIZKI SAPUTRA
# NIM   : 24060122120011

import ast
list_of_list = ast.literal_eval(input())

def IsEmpty(S):
    return S==[]

def IsList(S):
    return type(S) == list

def First(S):
    if not(IsEmpty(S)):
        return S[0]

def Tail(S) :
    if not(IsEmpty(S)) :
        return S[1:]

def IsPrima(n, i = 2) :
    if (n < 2) :
        return False
    elif (n == 2) :
        return True
    elif (n % i == 0) :
        return False
    elif (i * i > n) :
        return True

    return IsPrima(n, i + 1)

def PenjumlahanPrima (S) :
    if IsEmpty (S) :
        return 0
    elif not IsList(First(S)) :
        if IsPrima(First(S)) :
            return First(S) + PenjumlahanPrima(Tail(S))
        else :
            return PenjumlahanPrima(Tail(S))
    elif IsList(First(S)) :
        return PenjumlahanPrima(First(S)) + PenjumlahanPrima(Tail(S))

print (PenjumlahanPrima(list_of_list))