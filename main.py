import urllib
import facebook
import sys

print ("Hello World, this is python")
if (len(sys.argv) == 2):
    token = sys.argv[1]
    print "Token is "+token
    facebook = facebook.Facebook(token)
    facebook.postOnWall("Playing with facebook from Graph API is fun :)")
    

else:
    print "Usage: "+sys.argv[0]+" token"


