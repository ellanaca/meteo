import streamlit as st
import pydeck as pdk
import requests



def main():
    st.title('Météo :sun_with_face:')

    col1, col2 = st.columns([5, 1])

    with col1:
        city = st.text_input('', value='Ville...')

    with col2:
        st.title('')
        if st.button('Rechercher'):
            show_city_on_map(city)

    st.write('')
    if 'map' not in st.session_state:
        default_latitude = 48.8566
        default_longitude = 2.3522

        default_layer = pdk.Layer(
            'ScatterplotLayer',
            data=[{'position': [default_longitude, default_latitude], 'tooltip': 'Emplacement par défaut'}],
            get_position='position',
            get_radius=100,
            get_fill_color=[255, 0, 0],
            pickable=True,
        )

        default_view_state = pdk.ViewState(latitude=default_latitude, longitude=default_longitude, zoom=10)
        default_map_pydeck = pdk.Deck(layers=[default_layer], initial_view_state=default_view_state)

        st.session_state.map = default_map_pydeck


    st.pydeck_chart(st.session_state.map)

def get_coordinates_for_city(city):
    base_url = "https://nominatim.openstreetmap.org/search"
    params = {
        'q': 'city',
        'format': 'json',
    }
    response = requests.get(base_url, params=params)
    data = response.json()

    if data:
        latitude = float(data[0]['lat'])
        longitude = float(data[0]['lon'])
        return latitude, longitude
    else:
        return None, None

def show_city_on_map(city):
    latitude, longitude = get_coordinates_for_city(city)

    if latitude is not None and longitude is not None:
        layer = pdk.Layer(
            'ScatterplotLayer',
            data=[{'position': [longitude, latitude], 'tooltip': city}],
            get_position='position',
            get_radius=100,
            get_fill_color=[255, 0, 0],
            pickable=True,
        )

        view_state = pdk.ViewState(latitude=latitude, longitude=longitude, zoom=10)
        map_pydeck = pdk.Deck(layers=[layer], initial_view_state=view_state)

        st.session_state.map = map_pydeck
    else:
        st.warning('Ville introuvable')

if __name__ == "__main__":
    main()
