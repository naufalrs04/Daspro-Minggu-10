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

def HargaNinja(S) :
    if IsEmpty(S) :
        return 0
    elif not IsList(S) :
        return First(S) * 10000000 + HargaNinja(Tail(S))
    elif IsList(First(S)) :
        return max(First(S)) * 10000000 + HargaNinja(Tail(S))

print (HargaNinja(list_of_list))