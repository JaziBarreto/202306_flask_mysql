import re #Lo que permite que se haga la validacion
# Validacion del email
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
# Validacion de la contraseña
PASSWORD_REGEX = re.compile(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')
# Validacion números de teléfono en formato internacional de Paraguay (+595)
PHONE_NUMBER_REGEX = re.compile(r'^\+595\d{9}$')
#validar el dato de lo que es de mi interés
#BODEGA_REGEX = re.compile(r'^[A-Z][a-zA-Z ]{9,}$')