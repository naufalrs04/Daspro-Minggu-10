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
def MultiPermenGenap (S) :
    if IsList(First(S)) :
        return sum(First(S)) %2 == 0

def MultiPermenGanjil (S) :
    if IsList(First(S)) :
        return sum(First(S)) %2 != 0

def PenjualPermen (S) :
    if IsEmpty (S) :
        return 0
    elif not IsList(First(S)) :
        if First(S) %2 == 0 :
            return First(S) * 4000 + PenjualPermen(Tail(S))
        else :
            return First(S) * 3000 + PenjualPermen(Tail(S))
    elif IsList(First(S)) :
        if MultiPermenGenap (S) :
            return sum(First(S)) * 2000 + PenjualPermen(Tail(S))
        elif MultiPermenGanjil (S) :
            return sum(First(S)) * 1000 + PenjualPermen(Tail(S))

print (PenjualPermen(list_of_list))