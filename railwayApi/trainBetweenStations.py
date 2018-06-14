#!/Users/Prateek/AppData/Local/Programs/Python/Python36-32/python.exe
import core.core as c

print("Content-Type: application/json")
print()

ob = c.RailwayApi()
print(ob.trainBetweenStations("stncode","destcode","ddate"))