import pyowm

class WeatherFetch:
    def __init__(self):
        API_key = '23f71e4b2df6a0395cb991ef106a0f9c'
        owm = pyowm.OWM(API_key)
        observation = owm.weather_at_place('Philadelphia,us')
        self.weather = observation.get_weather()
    
    def get_temp(self):
        temp_f_arr = []
        temp_f = self.weather.get_temperature('fahrenheit')  
        temp_f_arr.append(temp_f['temp'])
        temp_f_arr.append(temp_f['temp_max'])
        temp_f_arr.append(temp_f['temp_min'])
        
        for temp in temp_f_arr:
            temp = int(temp)
        
        temp_c_arr = []
        temp_c = self.weather.get_temperature(unit='celsius')
        temp_c_arr.append(temp_c['temp'])
        temp_c_arr.append(temp_c['temp_max'])
        temp_c_arr.append(temp_c['temp_min'])
        
        for temp in temp_c_arr:
            temp = int(temp)
        
        return temp_f_arr, temp_c_arr
    
    def get_status(self):
        status = ''
        status_words = self.weather.get_detailed_status().split()
        for word in status_words:
            status += word.capitalize() + ' '
        
        return status
