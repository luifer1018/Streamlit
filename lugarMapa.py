import streamlit as st
import folium
from streamlit_folium import folium_static 
from geopy.geocoders import Nominatim

def main():
    st.title("Conversor de Lugar a Coordenadas")

    # Crear un campo de entrada de texto para ingresar el lugar
    lugar = st.text_input("Ingrese un lugar:")

    if lugar:
        # Crear un objeto geolocalizador
        
        geolocalizador = Nominatim(user_agent="my_geocoder", timeout=10)  # Aumentar el tiempo de espera a 10 segundos (o más si es necesario)

        try:
            # Obtener las coordenadas de latitud y longitud del lugar ingresado
            location = geolocalizador.geocode(lugar)

            if location:
                st.success(f"Las coordenadas de {lugar} son:")
                st.write(f"Latitud: {location.latitude}")
                st.write(f"Longitud: {location.longitude}")

                # Crear un mapa de folium
                m = folium.Map(location=[location.latitude, location.longitude], zoom_start=15)

                # Agregar un marcador en las coordenadas
                folium.Marker([location.latitude, location.longitude], tooltip=lugar).add_to(m)

                # Mostrar el mapa en Streamlit
                folium_static(m)
            else:
                st.error("No se encontraron coordenadas para el lugar ingresado.")
        except Exception as e:
            st.error(f"Se produjo un error: {str(e)}")

if __name__ == "__main__":
    main()
