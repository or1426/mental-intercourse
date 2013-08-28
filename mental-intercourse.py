#! /usr/bin/python                                                                                                                                                                                                                                                                                                                                                                                         
# A fairly unpythonic brainfuck implementation                                                                                                                                                                                                                                                                                                                                                             
# I'm not very happy with the global variables                                                                                                                                                                                                                                                                                                                                                             
# and the use of the integer i is vaugely evil                                                                                                                                                                                                                                                                                                                                                             
import sys; #for stdin and stdout                                                                                                                                                                                                                                                                                                                                                                          

#initalise array, pointer and the bracket "stack"                                                                                                                                                                                                                                                                                                                                                          
arraySize = 30000 #this is in the "spec"...                                                                                                                                                                                                                                                                                                                                                                
ptr = 0
array = [0] * arraySize
bracketStack = []

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
    global ptr,array,bracketStack,i
    bracketStack.append(i)
def loopEnd():
    global ptr,bracketStack,i
    if array[ptr] > 0:
        i = bracketStack[-1]
    else:
        bracketStack.pop()

opDictionary = {'>': incPtr,
               '<': decPtr,
               '+': incEle,
               '-': decEle,
               ',': getEle,
               '.': putEle,
               '[': loopStart,
               ']': loopEnd
               }

inString = sys.stdin.readline()
inList = list(inString)

#the unpythonic i makes the [ and ] based loops easier                                                                                                                                                                                                                                                                                                                                                     
i = 0
while i < len(inList) - 1:
    if inList[i] in opDictionary.keys():
        opDictionary[inList[i]]()
    i += 1
