import re	# el módulo regex para la validacion
# expresion regular para validar e-mail
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
# Expresión regular para validar contraseñas
PASSWORD_REGEX = re.compile(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')
# Expresión regular para validar números de teléfono en formato internacional de Paraguay (+595)
PHONE_NUMBER_REGEX = re.compile(r'^\+595\d{9}$')
#validar el dato de la bodega
BODEGA_REGEX = re.compile(r'^[A-Z][a-zA-Z ]{9,}$')
