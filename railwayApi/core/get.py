import requests
r = requests.get('https://www.w3schools.com/js/json_demo.txt')
print(r.status_code)
#r.status_code == requests.codes.ok
#print(r.headers)
print (r.text)
#print(dir(r))


#import requests

#r = requests.get('https://github.com/timeline.json')
#print r.text

# The Requests library also comes with a built-in JSON decoder,
# just in case you have to deal with JSON data

#import requests

#r = requests.get('https://github.com/timeline.json')
#print r.json

#print (r.encoding)
#>>>utf - 8
#r.encoding = ‘ISO - 8859 - 1’