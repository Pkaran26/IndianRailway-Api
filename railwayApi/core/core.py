import requests
class RailwayApi:

    apikey = "26jsavkcor"
    
    def stationSuggest(self, search):
        res = requests.get('https://api.railwayapi.com/v2/suggest-station/name/'+search+'/apikey/'+self.apikey)
        if res.status_code == requests.codes.ok:
            return res.text
        else:
            return res.status_code

    def liveTrainStatus(self, trainnumber, depdate):
        res = requests.get('https://api.railwayapi.com/v2/live/train/'+trainnumber+'/date/'+depdate+'/apikey/'+self.apikey)
        if res.status_code == requests.codes.ok:
            return res.text
        else:
            return res.status_code

    def pnrStatus(self, pnr):
        res = requests.get('https://api.railwayapi.com/v2/pnr-status/pnr/'+pnr+'/apikey'+self.apikey)
        if res.status_code == requests.codes.ok:
            return res.text
        else:
            return res.status_code

    def trainRoute(self, trainnumber):
        res = requests.get('https://api.railwayapi.com/v2/route/train/'+trainnumber+'/apikey'+self.apikey)
        if res.status_code == requests.codes.ok:
            return res.text
        else:
            return res.status_code

    def checkSeat(self, trainnumber, stncode, destcode, ddate):
        res = requests.get('https://api.railwayapi.com/v2/check-seat/train/' + trainnumber + '/source/' + stncode + '/dest/' + destcode + '/date/' + ddate + '/pref/' + classcode + '/quota/' + quota + '/apikey/' + self.apikey)
        if res.status_code == requests.codes.ok:
            return res.text
        else:
            return res.status_code

    def trainBetweenStations(self, stncode, destcode, ddate):
        res = requests.get('https://api.railwayapi.com/v2/between/source/'+stncode+'/dest/'+destcode+'/date/'+ddate+'/apikey/'+self.apikey)
        if res.status_code == requests.codes.ok:
            return res.text
        else:
            return res.status_code

    def fareEnq(self, trainnumber, stncode, destcode, age, classcode, quota, ddate):
        res = requests.get('https://api.railwayapi.com/v2/fare/train/'+trainnumber+'/source/'+stncode+'/dest/'+destcode+'/age/'+age+'/pref/'+classcode+'/quota/'+quota+'/date/'+ddate+'/apikey/'+self.apikey)
        if res.status_code == requests.codes.ok:
            return res.text
        else:
            return res.status_code

    def trainArrival(self, stncode):
        res = requests.get('https://api.railwayapi.com/v2/arrivals/station/'+stncode+'/hours/2/apikey/'+self.apikey)
        if res.status_code == requests.codes.ok:
            return res.text
        else:
            return res.status_code