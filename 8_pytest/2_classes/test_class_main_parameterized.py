from main import weather
import pytest

@pytest.mark.parametrize("temp,expected",[
     (-5,"It's freezing outside"),
     (10,"It's a bit chilly"),
     (20,"The weather is pleasant")
])

def test_weather_check(temp,expected):
     w= weather()
     assert w.weather_check(temp)==expected

# def test_rain_check():
#      w=weather()
#      assert w.rain_check(0.8)=="It's likely to rain"
#      assert w.rain_check(0.5)=="There is a chance of rain today"
#      assert w.rain_check(0.1)=="It's is unlikely to rain"

if __name__ == "__main__":
     test_weather_check()
     # test_rain_check()