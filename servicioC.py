import streamlit as st
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import folium
from streamlit_folium import folium_static

# Crear una lista de tarifas de aeropuertos
tarifas_aeropuertos = {
    "LGA - LaGuardia Airport": {"Sedan": 85.00, "SUV": 120.00},
    "JFK - John F. Kennedy International Airport": {"Sedan": 110.00, "SUV": 150.00},
    "EWR - Newark Liberty International Airport": {"Sedan": 130.00, "SUV": 160.00},
    "TEB - Teterboro Airport": {"Sedan": 145.00, "SUV": 175.00},
    "HPN - Westchester County Airport": {"Sedan": 165.00, "SUV": 210.00},
    "ISP - Long Island MacArthur Airport": {"Sedan": 195.00, "SUV": 245.00},
}

# Función para enviar correo electrónico
def enviar_correo(destinatario, hora_servicio, aeropuerto, vehiculo, lugar_recogida):
    # Configurar el servidor SMTP
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_user = "luivaniri@gmail.com"
    smtp_password = "ryvk ptuq ahvh paeh"

    # Crear el mensaje de correo
    msg = MIMEMultipart()
    msg['From'] = smtp_user
    msg['To'] = destinatario
    msg['Subject'] = "Confirmación de servicio"

    # Cuerpo del mensaje
    mensaje = f"Gracias por reservar un servicio desde {lugar_recogida} hacia {aeropuerto} en un {vehiculo} a las {hora_servicio}."
    msg.attach(MIMEText(mensaje, 'plain'))

    # Iniciar conexión con el servidor SMTP y enviar el correo
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(smtp_user, destinatario, msg.as_string())
        server.quit()
        st.success("Correo electrónico enviado con éxito")
    except Exception as e:
        st.error(f"Error al enviar el correo electrónico: {str(e)}")

# Interfaz de usuario de Streamlit
st.title("Reservation of Rates for Sports Events")

# Selección de aeropuerto
aeropuerto = st.selectbox("Seleccione el aeropuerto:", list(tarifas_aeropuertos.keys()))

# Selección de vehículo
vehiculo = st.radio("Seleccione el tipo de vehículo:", ["Sedan", "SUV"])

# Campo para ingresar el lugar de recogida
lugar_recogida = st.text_input("pick up place:")

# Calcular tarifa
tarifa = tarifas_aeropuertos[aeropuerto][vehiculo]

# Mostrar la tarifa
st.write(f"Tarifa desde {aeropuerto} en {vehiculo}: ${tarifa:.2f}")

# Formulario de reserva
st.subheader("Reserva de Servicio")
email = st.text_input("Ingrese su correo electrónico:")
hora_servicio = st.time_input("Seleccione la hora del servicio:")

# Botón para enviar reserva
if st.button("Enviar reserva"):
    if email and hora_servicio and lugar_recogida:
        enviar_correo(email, hora_servicio.strftime("%H:%M"), aeropuerto, vehiculo, lugar_recogida)
        
        # Crear un mapa que muestra la ruta entre el lugar de recogida y el aeropuerto
        mapa = folium.Map(location=[40.7128, -74.0060], zoom_start=10)  # Coordenadas de Nueva York
        
        # Agregar marcadores para el lugar de recogida y el aeropuerto
        folium.Marker(location=[40.7128, -74.0060], tooltip="Aeropuerto").add_to(mapa)
        folium.Marker(location=[40.730610, -73.935242], tooltip="Lugar de recogida").add_to(mapa)
        
        # Dibujar una línea entre los dos puntos
        folium.PolyLine(locations=[[40.7128, -74.0060], [40.730610, -73.935242]], color='blue').add_to(mapa)
        
        # Mostrar el mapa en la aplicación Streamlit
        folium_static(mapa)
        
    else:
        st.warning("Por favor, complete todos los campos.")
