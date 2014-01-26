# My First Python script
import urllib2
import ast

print "Testing"

response = urllib2.urlopen('http://api.wunderground.com/api/a4e6a83d1d8bb393/conditions/q/CA/San_Francisco.json')
json = response.read()
out = ast.literal_eval(json)


print out["current_observation"]