import socket
from cryptography.fernet import Fernet
from datetime import datetime
import requests

# Ключ, полученный от сервера
KEY = b"ysuBSo5dt6fgcLH2ugVz922pzSoPQLldRwfNvbe-31w="
cipher = Fernet(KEY)

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, SERVER_PORT))
print(f"[+] [{datetime.now()}] Подключено к VPN-серверу {SERVER_IP}:{SERVER_PORT}\n")

while True:
    print("Выберите действие:")
    print("1. Ввести сообщение вручную")
    print("2. Получить HTML с example.com и отправить")
    print("3. Выход")
    choice = input(">>> ")

    if choice == "1":
        msg = input("[Клиент] Введите сообщение: ").strip()
        if not msg:
            continue
    elif choice == "2":
        print("[Клиент] Загружаю HTML с example.com...")
        response = requests.get("http://example.com")
        msg = response.text
        print(f"[Клиент] Получено {len(msg)} байт HTML-данных.")
    elif choice == "3":
        print("[Клиент] Завершение сеанса.")
        break
    else:
        print("[!] Неверный выбор.")
        continue

    print(f"\n[Клиент] >>> Оригинальное сообщение: {msg[:100]}{'...' if len(msg) > 100 else ''}")
    encrypted = cipher.encrypt(msg.encode())
    print(f"[Клиент] >>> Зашифрованные данные: {encrypted[:60]}... (длина {len(encrypted)} байт)")

    client.sendall(encrypted)
    print(f"[Клиент] >>> Отправлено серверу в {datetime.now()}\n")

    response = client.recv(65536)
    decrypted = cipher.decrypt(response).decode()

    print(f"[Клиент] <<< Ответ от сервера получен в {datetime.now()}")
    print(f"[Клиент] <<< Расшифрованный ответ: {decrypted}\n")
    print("-" * 60)
 
