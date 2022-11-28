# NAMA  : NAUFAL RIZKI SAPUTRA
# NIM   : 24060122120011

import ast
list_of_list = ast.literal_eval(input())
x = int(input())

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

def KonsLo (L,S) :
    if IsEmpty(S) :
        return [L]
    else :
        return [L] + S

def HindariMonster(a,b) :
    if IsEmpty(b) :
        return []
    else :
        if not IsList(First(b)) :
            if First(b) %a == 0 :
                return HindariMonster(a,Tail(b))
            elif First(b) %a != 0 :
                return KonsLo(First(b),HindariMonster(a,Tail(b)))
        elif IsList(First(b)) :
            return KonsLo(HindariMonster(a,First(b)),HindariMonster(a,Tail(b)))

print (HindariMonster(x,list_of_list))