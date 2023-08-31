import streamlit as st
import pydeck as pdk
import requests

#Clé API dans secrets
key = st.secrets["API_KEY"]

def request_coord(city,key) :

    #Encodage (on retire les espaces)
    city_encoded = city.replace(" ", "%20")

    #requète pour obtenir les coordonnées de la ville
    get_loc = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_encoded},FRA&limit=1&appid={key}').json()
    lat = get_loc[0]["lat"]
    lon = get_loc[0]["lon"]
    return lat, lon

def request_temp(lat,lon, key):
    #requète pour obtenir les informations météorologiques de la ville
    use_loc = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={key}').json()
    temp = use_loc['main']['temp']
    return temp

def main():


    st.title('Météo :sun_with_face:')

    col1, col2 = st.columns([5, 1])

    with col1:
        city = st.text_input('', value='Ville...')

    lat, lon = request_coord(city,key)
    temp = request_temp(lat,lon,key)

    with col2:
        st.title('')
        if st.button('Rechercher'):
            show_city_on_map(city,lat,lon)

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


def show_city_on_map(city,lat,lon):

    if lat is not None and lon is not None:
        layer = pdk.Layer(
            'ScatterplotLayer',
            data=[{'position': [lon, lat], 'tooltip': city}],
            get_position='position',
            get_radius=100,
            get_fill_color=[255, 0, 0],
            pickable=True,
        )

        view_state = pdk.ViewState(latitude=lat, longitude=lon, zoom=10)
        map_pydeck = pdk.Deck(layers=[layer], initial_view_state=view_state)

        st.session_state.map = map_pydeck
    else:
        st.warning('Ville introuvable')

if __name__ == "__main__":
    main()
