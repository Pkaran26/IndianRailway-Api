#!/Users/Prateek/AppData/Local/Programs/Python/Python36-32/python.exe
import core.core as c

print("Content-Type: application/json")
print()

ob = c.RailwayApi()
print(ob.liveTrainStatus("12251","20-06-2018"))
