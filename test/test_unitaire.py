import pytest
import streamlit as st
import requests
import pydeck
from streamlit_app import request_coord, request_temp, show_city_on_map
from unittest.mock import patch

"""def test_request(mocker):
    mock_response = mocker.Mock()
    mock_response.json.return_value = {
        'city': {'coord': {'lat': 48.8566, 'lon': 2.3522}},
        'list': [{'main': {'temp': 20}}] + [{'main': {'temp': 21}}] * 8 + [{'main': {'temp': 22}}] * 8
    }
    mocker.patch.object(requests, 'get', return_value=mock_response)

    API_KEY = st.secrets["API_KEY"]
    city = "Paris"
    coords, today, tomorrow, day_after_tomorrow = (city, API_KEY)

    assert coords['lat'] == 48.8566
    assert coords['lon'] == 2.3522
    assert today == 20
    assert tomorrow == 21
    assert day_after_tomorrow == 22"""



def test_show_city_on_map(mocker):
    with patch.object(st, "session_state", create=True):
        mock_warning = mocker.patch("streamlit.warning")

        show_city_on_map("Paris", None, None)
        mock_warning.assert_called_with("Ville introuvable")

if __name__ == "__main__":
    pytest.main()
