#!/bin/python3
import ast
def EquivalentKeypresses(strArr):
    string1=strArr[0].split(',')
    string2=strArr[1].split(',')
    #function which erase one preseding character for backspace(-B) keypress
    def stringcheck(string):
        while '-B' in string:
            index=string.index('-B')                    #gets the index of backspace key
            string.pop(index)                           #backspace character is removed from string
            try:
                if index !=0:
                    string.pop(index-1)                 #erase one preseding character
            except:
                pass
        return string
    if '-B' in string1:                                 #check is backspace key is present in string1
        string1=stringcheck(string1)
    elif '-B' in string2:                               #check is backspace key is present in string2
        string2=stringcheck(string2)
    elif ('-B' in string1) and('-B' in string2):        #check is backspace key is present in string1 and string1
        string1=stringcheck(string1)
        string2=stringcheck(string2)
    if string1==string2:                                #after the check through backspace key now remaining elements are compared
        return 'true'
    else:
        return 'false'

print(EquivalentKeypresses(ast.literal_eval(input('enter')))) #input("enter").strip('["').strip('"]').split('", "')))
"""
Different Inputs
print(EquivalentKeypresses(["a,b,c,d", "a,b,c,c,-B,d"]))
print(EquivalentKeypresses(["-B,-B,-B,c,c", "c,c"]))
print(EquivalentKeypresses(["","a,-B,-B,a,-B,a,b,c,c,c,d"]))
"""