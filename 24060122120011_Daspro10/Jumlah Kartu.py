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

def JumlahKartu(S):
    if IsEmpty(S):
        return 0
    elif not IsList(First(S)) :
        return 1 + JumlahKartu(Tail(S))
    elif IsList(First(S)) :
        if not IsList(First(S[0])) :
            return 1 + JumlahKartu(Tail(S[0])) + JumlahKartu(Tail(S))
        elif IsList(First(S[0])) :
            return 1 + JumlahKartu(Tail(S))

print (JumlahKartu(list_of_list))