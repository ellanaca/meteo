import pytest
import streamlit as st
from streamlit_app import request
import requests
import pydeck
from streamlit_app.py import request_coord, request_temp


def test_request(mocker):
    mock_response = mocker.Mock()
    mock_response.json.return_value = {
        'city': {'coord': {'lat': 48.8566, 'lon': 2.3522}},
        'list': [{'main': {'temp': 20}}] + [{'main': {'temp': 21}}] * 8 + [{'main': {'temp': 22}}] * 8
    }
    mocker.patch.object(requests, 'get', return_value=mock_response)

    API_KEY = st.secrets["API_KEY"]
    city = "Paris"
    coords, today, tomorrow, day_after_tomorrow = get_weather(city, API_KEY)

    assert coords['lat'] == 48.8566
    assert coords['lon'] == 2.3522
    assert today == 20
    assert tomorrow == 21
    assert day_after_tomorrow == 22


if __name__ == "__main__":
    pytest.main()
