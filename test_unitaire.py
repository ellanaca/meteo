import pytest
from streamlit_app import get_coordinates_for_city

def test_get_coordinates_for_city():
    result = get_coordinates_for_city("Paris")
    assert result == (48.8566, 2.3522)

def test_show_city_on_map():
    pass

def test_main():
    pass



if __name__ == "__main__":
    pytest.main()
