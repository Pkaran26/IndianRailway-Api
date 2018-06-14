#!/Users/Prateek/AppData/Local/Programs/Python/Python36-32/python.exe
import core.core as c

ob = c.RailwayApi()
print(ob.fareEnq("trainnumber","stncode","destcode","age","classcode","quota","ddate"))
