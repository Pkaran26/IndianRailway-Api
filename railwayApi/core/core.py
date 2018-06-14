#!/Users/Prateek/AppData/Local/Programs/Python/Python36-32/python.exe
import requests
import json

class RailwayApi:

    apikey = "26jsavkcor"
    
    def stationSuggest(self, search):
        res = requests.get('https://api.railwayapi.com/v2/suggest-station/name/'+search+'/apikey/'+self.apikey)
        return self.checkResponse(res.text)

    def liveTrainStatus(self, trainnumber, depdate):
        res = requests.get('https://api.railwayapi.com/v2/live/train/'+trainnumber+'/date/'+depdate+'/apikey/'+self.apikey)
        return self.checkResponse(res.text)

    def pnrStatus(self, pnr):
        res = requests.get('https://api.railwayapi.com/v2/pnr-status/pnr/'+pnr+'/apikey/'+self.apikey)
        return self.checkResponse(res.text)

    def trainRoute(self, trainnumber):
        res = requests.get('https://api.railwayapi.com/v2/route/train/'+trainnumber+'/apikey'+self.apikey)
        return self.checkResponse(res.text)

    def checkSeat(self, trainnumber, stncode, destcode, ddate, classcode, quota):
        res = requests.get('https://api.railwayapi.com/v2/check-seat/train/' + trainnumber + '/source/' + stncode + '/dest/' + destcode + '/date/' + ddate + '/pref/' + classcode + '/quota/' + quota + '/apikey/' + self.apikey)
        return self.checkResponse(res.text)

    def trainBetweenStations(self, stncode, destcode, ddate):
        res = requests.get('https://api.railwayapi.com/v2/between/source/'+stncode+'/dest/'+destcode+'/date/'+ddate+'/apikey/'+self.apikey)
        return self.checkResponse(res.text)

    def fareEnq(self, trainnumber, stncode, destcode, age, classcode, quota, ddate):
        res = requests.get('https://api.railwayapi.com/v2/fare/train/'+trainnumber+'/source/'+stncode+'/dest/'+destcode+'/age/'+age+'/pref/'+classcode+'/quota/'+quota+'/date/'+ddate+'/apikey/'+self.apikey)
        return self.checkResponse(res.text)

    def trainArrival(self, stncode):
        res = requests.get('https://api.railwayapi.com/v2/arrivals/station/'+stncode+'/hours/2/apikey/'+self.apikey)
        return self.checkResponse(res.text)

    def checkResponse(self, result):
        parsed_json = json.loads(result)
        if parsed_json['response_code'] == 200:
            return result
        else:
            return "{'error':'404'}"
