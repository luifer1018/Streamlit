import smtplib

message = 'Hola, ¿cómo estás?'
subject = 'Prueba'

# Formatea el mensaje con el asunto
message = 'Subject: {}\n\n{}'.format(subject, message)

# Crea una conexión segura con el servidor de Gmail
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

# Inicia sesión en tu cuenta de Gmail
server.login('luivaniri@gmail.com', 'ifx181306')  # Reemplaza con tu correo y contraseña reales

# Envía el correo desde tu dirección de correo a la misma dirección (en este ejemplo)
server.sendmail('luivaniri@gmail.com', 'luivaniri@gmail.com', message)

# Cierra la conexión con el servidor
server.quit()

print('Correo enviado')
