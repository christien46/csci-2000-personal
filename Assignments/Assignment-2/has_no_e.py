#!/usr/bin/python



def has_no_e( str ):
    for i in str:
        if (i == 'e'):
	    return False
        else:
	    return True

	    



line = raw_input()


has_no_e( line )
if ( has_no_e( line ) == True ):
    print "e is not found"
else:
    print "e is found"
