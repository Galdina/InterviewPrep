def isSubSequence(string1,string2):
    m=len(string1)
    n=len(string2)

    if m>n: 
        return False
    else:
        remainingString=string2
        i=0
        while i<m:
            if remainingString.find(string1[i])==-1: 
                # if it is not found, the value will be -1
                return False
            else: 
                # if it is found, the value will be the index of first occurrence
                index=remainingString.find(string1[i])
                remainingString=remainingString[index+1:]
                i+=1
        return True

string1='abc'
string2='asbsc'
string3='acedb'     

isSubSequence(string1,string2)