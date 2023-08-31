import pytest
import streamlit as st
from streamlit_app import get_coordinates_for_city,show_city_on_map, main
from unittest.mock import Mock, patch
import requests
import pydeck

def test_get_coordinates_for_city():
    result = get_coordinates_for_city('Paris')
    assert result == (48.8566, 2.3522)

@pytest.fixture
def mock_get_coordinates(monkeypatch):
    mock_response = [{"lat": "48.8566", "lon": "2.3522"}]
    mock_json = Mock(return_value=mock_response)
    mock_get = Mock(return_value=Mock(json=mock_json))
    monkeypatch.setattr(requests, "get", mock_get)

def test_show_city_on_map(monkeypatch, mock_get_coordinates, mocker):
    mocker.patch("pydeck.Deck")
    mocker.patch("pydeck.Layer")

    city = "Paris"
    show_city_on_map(city)

    assert requests.get.called_with("https://nominatim.openstreetmap.org/search", params={"q": city, "format": "json"})
    assert pydeck.Deck.called
    assert pydeck.Layer.called

def test_main(mocker):
    mocker.patch("streamlit.text_input", return_value="Paris")
    mocker.patch("streamlit.button", return_value=True)
    mocker.patch("app.show_city_on_map")

    main()

    assert st.text_input.called
    assert st.button.called
    assert show_city_on_map.called



if __name__ == "__main__":
    pytest.main()
