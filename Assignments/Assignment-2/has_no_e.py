#!/usr/bin/python



def has_no_e( str ):
    for i in str:
        if (i == 'e'):
	    return False
        
    return True 

	    


print "please enter a word"

word = raw_input()


has_no_e( word )
if ( has_no_e( word ) == True ):
    print "e is not found"
else:
    print "e is found"



searchfile = open("gadsby.txt", "r")
for line in searchfile: 
    if(has_no_e( line ) == False  ):
        print "There is an e in the line"
        break

     


