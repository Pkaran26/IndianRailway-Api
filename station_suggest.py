#!/Users/Prateek/AppData/Local/Programs/Python/Python36-32/python.exe
import core.core as c

print("Content-Type: application/json")
print()

ob = c.RailwayApi()
result = ob.stationSuggest("bilas")
print(result)
