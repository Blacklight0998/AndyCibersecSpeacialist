"""En este ejercicio profe agregamos secrets para poder generar de manera segura la contraseña y que no se pueda adivinar facilmente, tambien agregamos un nonce para poder cifrar la contraseña y que no se pueda descifrar facilmente, y por ultimo agregamos un tag para poder verificar la integridad de la contraseña cifrada y que no se pueda modificar facilmente."""
import secrets
import string
import time

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

usuario_correcto = "Admin"
def generar_password(longitud=12):
    # Genera una contraseña aleatoria segura utilizando caracteres alfanuméricos y símbolos especiales
    caracteres = string.ascii_letters + string.digits + "!@#$%&*"
    password = ""
    for _ in range(longitud):
        # Se utiliza secrets.choice para seleccionar caracteres de manera segura y evitar patrones predecibles
        password += secrets.choice(caracteres)
    return password
def cifrar_password(password, clave):
    # Patron de cifrado AES en modo EAX para garantizar confidencialidad e integridad del mensaje
    mensaje_bytes = password.encode("utf-8")
    cipher = AES.new(clave, AES.MODE_EAX)
    nonce = cipher.nonce
    texto_cifrado, tag = cipher.encrypt_and_digest(mensaje_bytes)
    return texto_cifrado, nonce, tag
def verificar_password(password, clave, texto_cifrado, nonce, tag):
    try:
        # Consiste en verificar la integridad del mensaje descifrado comparando el resultado con la contraseña original
        mensaje_bytes = password.encode("utf-8")
        cipher = AES.new(clave, AES.MODE_EAX, nonce=nonce)
        mensaje_recuperado = cipher.decrypt_and_verify(texto_cifrado, tag)
        return mensaje_recuperado == mensaje_bytes
    except ValueError:
        return False
def login():
    print("=" * 50)
    print(" SISTEMA DE LOGIN")
    print("=" * 50)
    usuario_correcto = "Admin"
    # Generación de contraseña aleatoria
    password_generada = generar_password()
    print("\n[!] Generando contraseña aleatoria...")
    time.sleep(1)
    print(f"[+] Usuario: {usuario_correcto}")
    print(f"[+] Contraseña generada: {password_generada}")
    # Generación de clave AES de 16 bytes
    clave = get_random_bytes(16)
    print("\n[!] Generando clave AES...")
    time.sleep(1)
    # Cifrado de la contraseña
    texto_cifrado, nonce, tag = cifrar_password(password_generada, clave)
    print("[+] Contraseña cifrada correctamente.")
    print(f"[+] Password cifrado (Hex): {texto_cifrado.hex()}")
    print(f"[+] Nonce (Hex): {nonce.hex()}")
    print(f"[+] Tag (Hex): {tag.hex()}")
    print("\n" + "=" * 50)
    print(" INICIO DE SESIÓN")
    print("=" * 50)
    usuario = input("Ingrese el usuario: ")
    password = input("Ingrese la contraseña: ")
    if usuario != usuario_correcto:
        print("\n[-] Usuario incorrecto.")
        return
    print("\n[!] Verificando contraseña...")
    time.sleep(1)
    if verificar_password(password, clave, texto_cifrado, nonce, tag):
        print("[+] ¡Login exitoso!")
        print(f"[+] Bienvenido, {usuario}.")
    else:
        print("[-] Contraseña incorrecta.")
if __name__ == "__main__":
    login()