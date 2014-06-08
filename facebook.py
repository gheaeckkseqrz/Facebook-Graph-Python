import urllib
import json
from pprint import pprint

class Facebook:
    """Facebook interaction class"""

    
    def __init__(self, token):
        self.acces_token = token
        self.userName = ""

    def getUserInfos(self):
        args = {};
        args["access_token"] = self.acces_token
        params = urllib.urlencode(args)
        f = urllib.urlopen("https://graph.facebook.com/v1.0/me?%s" % params)
        print f.read()
        
    def likeObject(self, objectId):
        args = {}
        args["access_token"] = self.acces_token
        params = urllib.urlencode(args)
        f = urllib.urlopen("https://graph.facebook.com/v1.0/"+objectId+"/likes", params)
        print f.read()

    def getProfilePictureId(self, userId):
        args = {}
        args["access_token"] = self.acces_token
        params = urllib.urlencode(args)
        f = urllib.urlopen("https://graph.facebook.com/v1.0/"+userId+"/albums?%s" % params)

        self.jsondata2 = f.read()
        self.jsondata2 = json.loads(self.jsondata2)

        for item in self.jsondata2['data']:
            if (item['name'] == "Profile Pictures"):
                print "Profile Album : "+item['name']+" : "+item['id']
                if (item['cover_photo']):
                    print "Profile picture : "+item['cover_photo']
                    self.likeObject(item['cover_photo'])

    def getFriendsList(self):
        args = {}
        args["access_token"] = self.acces_token
        params = urllib.urlencode(args)
        f = urllib.urlopen("https://graph.facebook.com/v1.0/me/friends?%s" % params)
        
        self.jsondata = f.read()
        self.jsondata = json.loads(self.jsondata)

        i = 0
        for item in self.jsondata['data']:
            i = i+1
            print item['name']+" : "+item['id']+"("+str(i)+")"
            try:
                self.getProfilePictureId(item['id'])
            except KeyError:
                print "No profile picture for "+item['name']


    def postOnWall(self, msg):
        args = {}
        args["access_token"] = self.acces_token
        args["message"] = msg
        params = urllib.urlencode(args)
        f = urllib.urlopen("https://graph.facebook.com/v1.0/me/feed", params)
        print f.read()
