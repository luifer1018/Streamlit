import streamlit as st
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Crear un diccionario de tarifas desde los eventos deportivos
tarifas_eventos = {
    "Flushing Stadium (Mets or Tennis)": {"Sedan": 90.00, "SUV": 130.00},
    "Yankee Stadium": {"Sedan": 110.00, "SUV": 140.00},
    "Barclays Center": {"Sedan": 90.00, "SUV": 145.00},
    "Meadowlands": {"Sedan": 130.00, "SUV": 160.00},
    "Prudential Center": {"Sedan": 130.00, "SUV": 160.00},
    "Atlantic City": {"Sedan": 460.00, "SUV": 535.00},
}

# Función para enviar correo electrónico
def enviar_correo(destinatario, hora_servicio, evento, vehiculo):
    # Configurar el servidor SMTP
    smtp_server = "smtp.example.com"
    smtp_port = 587
    smtp_user = "tu_correo@example.com"
    smtp_password = "tu_contraseña"

    # Crear el mensaje de correo
    msg = MIMEMultipart()
    msg['From'] = smtp_user
    msg['To'] = destinatario
    msg['Subject'] = "Confirmación de servicio"

    # Cuerpo del mensaje
    mensaje = f"Gracias por reservar un servicio para el evento en {evento} en un {vehiculo} a las {hora_servicio}."
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
st.title("Airport Fare Reservation(including tolls)")

# Selección de evento deportivo
evento = st.selectbox("Seleccione el evento deportivo:", list(tarifas_eventos.keys()))

# Selección de vehículo
vehiculo = st.radio("Seleccione el tipo de vehículo:", ["Sedan", "SUV"])

# Calcular tarifa
tarifa = tarifas_eventos[evento][vehiculo]

# Mostrar la tarifa
st.write(f"Rate for the event in {evento} in {vehiculo}: ${tarifa:.2f}")

# Formulario de reserva
st.subheader("Reserva de Servicio")
email = st.text_input("Ingrese su correo electrónico:")
hora_servicio = st.time_input("Seleccione la hora del servicio:")

# Botón para enviar reserva
if st.button("Enviar reserva"):
    if email and hora_servicio:
        enviar_correo(email, hora_servicio.strftime("%H:%M"), evento, vehiculo)
    else:
        st.warning("Por favor, complete todos los campos.")
