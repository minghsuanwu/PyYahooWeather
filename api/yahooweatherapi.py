'''
Created on 2018年1月26日

@author: Ming_Wu
'''
from weather import Weather

# Declare weather from Weather()
weather = Weather()

def reportWithWOEID(WOEID):    
    # Lookup WOEID via http://weather.yahoo.com.    
    lookup = weather.lookup(WOEID)
    condition = lookup.condition()
    print('date: '+condition.date())
    print('forecast: '+condition.text())
    print('temp: '+condition.temp())

def reportWithName(locationName):
    # Lookup via location name.    
    location = weather.lookup_by_location(locationName)
    print('location: '+locationName)
    
    condition = location.condition()
    print('date: '+condition.date())
    print('forecast: '+condition.text())
    print('temp: '+condition.temp())
    
    
def forecastWithName(locationName):
    # Get weather forecasts for the upcoming days.
    location = weather.lookup_by_location(locationName)
    print('location: '+locationName)
    
    forecasts = location.forecast()
    for forecast in forecasts:
        print('date: '+forecast.date())
        print('forecast: '+forecast.text())
        print('high: '+forecast.high())
        print('low: '+forecast.low())
        print('-----------------------------')

def main():
    locationWOEID = 2367105
    locationName = 'taipei'
    
    reportWithWOEID(locationWOEID)
    print('===============================')
    reportWithName(locationName)
    print('===============================')
    forecastWithName(locationName)
    
if __name__ == '__main__':
    main()