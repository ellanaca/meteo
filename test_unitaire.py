import pytest
import streamlit as st
from streamlit_app import get_coordinates_for_city,show_city_on_map, main
import requests
import pydeck

def test_get_coordinates_for_city():
    result = get_coordinates_for_city('Paris')
    assert result == (48.8566, 2.3522)




if __name__ == "__main__":
    pytest.main()
