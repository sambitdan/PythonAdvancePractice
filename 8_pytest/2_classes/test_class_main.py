from main import weather


def test_weather_check():
     w = weather() # creating object from weather class
     assert w.weather_check(-5)== "It's freezing outside"
     assert w.weather_check(10)== "It's a bit chilly"
     assert w.weather_check(20)=="The weather is pleasant"

def test_rain_check():
     w=weather()
     assert w.rain_check(0.8)=="It's likely to rain"
     assert w.rain_check(0.5)=="There is a chance of rain today"
     assert w.rain_check(0.1)=="It's is unlikely to rain"

if __name__ == "__main__":
     test_weather_check()
     test_rain_check()