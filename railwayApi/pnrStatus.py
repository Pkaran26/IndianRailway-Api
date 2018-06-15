#!/Users/Prateek/AppData/Local/Programs/Python/Python36-32/python.exe

import core.core as c
import sys, json

print ("Access-Control-Allow-Origin: *")
print()

myjson = json.load(sys.stdin)
pnr = myjson['pnr']


ob = c.RailwayApi()
print(ob.pnrStatus(pnr))
