import requests
import pytest
from unittest.mock import Mock, patch

def fetch_data_from_api(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

@pytest.mark.parametrize(
        "status_code, expected_result", [
            (200, {"data": "mocked data"}),
            (404, None)
            # ,(200, {"data": "incorrect data"})
            ])
def test_fetch_data_from_api(status_code, expected_result):
    # Create a mock object for requests.get
    mock_get = Mock()
    mock_get.return_value.status_code = status_code
    mock_get.return_value.json.return_value = {"data": "mocked data"}

    # Replace requests.get with the mock object
    with patch('requests.get', mock_get):
        result = fetch_data_from_api("http://example.com/api")

    assert result == expected_result