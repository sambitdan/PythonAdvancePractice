from main import weather_check
# import Pytest

# Test cases for weather check

def test_weather_check():
    assert weather_check(-5) == "It's freezing outside"
    assert weather_check(10) == "It's bit chilly"
    assert weather_check(20) == "The weather is pleasant"

# it shows only run the above function when running this file
if __name__ == "__main__":
    test_weather_check()
