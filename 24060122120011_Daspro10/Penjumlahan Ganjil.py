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

def IsGanjil(S) :
    if not(IsEmpty(S)) :
        return S%2 != 0

def PenjumlahanGanjil (x) :
    if IsEmpty (x) :
        return 0
    elif not IsList(First(x)) :
        if IsGanjil(First(x)) :
            return First(x) + PenjumlahanGanjil(Tail(x))
        else :
            return PenjumlahanGanjil(Tail(x))
    elif IsList(First(x)) :
        return PenjumlahanGanjil(First(x)) + PenjumlahanGanjil(Tail(x))

print (PenjumlahanGanjil(list_of_list))