from main import api_call
import pytest

# mocker is a built-in fixture available in pytest to simulate the api response
def test_api_call(mocker):
    mock_get = mocker.patch("main.requests.get") # passing the function
    mock_get.return_value.json.return_value = {"main":{"key":"value"}}

    result = api_call(url="https://jsonplaceholder.typicode.com/posts")

    assert result == {"data":{"main":{"key":"value"}}}



