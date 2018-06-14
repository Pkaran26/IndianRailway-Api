import requests
r = requests.get('https://www.w3schools.com/js/json_demo.txt')
print(r.status_code)
#r.status_code == requests.codes.ok
#print(r.headers)
print (r.text)
#print(dir(r))
 #r = requests.post('http://httpbin.org/post', data = {'key':'value'})

#Nice, right? What about the other HTTP request types: PUT, DELETE, HEAD and OPTIONS? These are all just as simple:

#>>> r = requests.put('http://httpbin.org/put', data = {'key':'value'})
#>>> r = requests.delete('http://httpbin.org/delete')
#>>> r = requests.head('http://httpbin.org/get')
#>>> r = requests.options('http://httpbin.org/get')

