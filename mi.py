#! /usr/bin/python
# A fairly unpythonic brainfuck implementation
# I'm not very happy with the global variables
# and the use of the integer tapePtr is vaugely evil

import sys; #for stdin and stdout                                                                                                                                                                   

#initalise array, pointer and the bracket "stack"                                                                                                                                               
arraySize = 30000 #this is in the "spec"...                                                                               
ptr = 0 #where we are in the array
array = [0] * arraySize

#define functions

def incPtr():
    global ptr, array
    ptr += 1
def decPtr():
    global ptr, array
    ptr -= 1
def incEle():
    global ptr,array
    array[ptr] += 1
def decEle():
    global ptr,array
    array[ptr] -= 1
def putEle():
    global ptr,array
    sys.stdout.write(str(unichr(array[ptr])))
def getEle():
    global ptr,array
    array[ptr] = ord(sys.stdin.read(1))
def loopStart():
    global ptr,array,bracketMap,tapePtr
    if array[ptr] == 0:
        for start,end in bracketMap:
            if start == tapePtr:
                tapePtr = end
def loopEnd():
    global ptr,bracketMap,tapePtr
    for start,end in bracketMap:
        if tapePtr == end:
            tapePtr = start - 1

opDictionary = {'>': incPtr,
               '<': decPtr,
               '+': incEle,
               '-': decEle,
               ',': getEle,
               '.': putEle,
               '[': loopStart,
               ']': loopEnd
               }

tape = sys.stdin.readline() 

openingBracketStack = [] 
bracketMap = [] #list of startBracket, endBracket touples so we can match them

#its really annoying that we have to read the list twice *sad face*
for i, char in enumerate(tape):
    if char == '[':
        openingBracketStack.append(i)
    elif char == ']':
        matchingOpeningBracket = openingBracketStack.pop()
        touple = matchingOpeningBracket, i
        bracketMap.append(touple)

#the unpythonic tapePtr makes the [ ] loops easier
tapePtr = 0
while tapePtr < len(tape) - 1:
    if tape[tapePtr] in opDictionary.keys():
        opDictionary[tape[tapePtr]]()
    tapePtr += 1
