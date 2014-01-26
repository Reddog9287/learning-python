# My First Python script
import urllib2
import ast

print "Testing"
def makeUrlReq(url):
    """ url is a url as a string """
    response = urllib2.urlopen(url)
    json = response.read()
    return json

out = ast.literal_eval(makeUrlReq("http://api.wunderground.com/api/a4e6a83d1d8bb393/conditions/q/CA/San_Francisco.json"))

print out["current_observation"]