import socket
from cryptography.fernet import Fernet
from datetime import datetime

# Генерация ключа (один раз сгенерируй и используй тот же)
KEY = b"ysuBSo5dt6fgcLH2ugVz922pzSoPQLldRwfNvbe-31w="
cipher = Fernet(KEY)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 5555))
server.listen(1)

print(f"[{datetime.now()}] [*] VPN-сервер запущен и слушает порт 5555...")
client_socket, addr = server.accept()
print(f"[{datetime.now()}] [+] Клиент подключился: {addr}\n")

while True:
    data = client_socket.recv(65536)
    if not data:
        print("[!] Клиент отключился.")
        break

    print(f"[{datetime.now()}] Получено {len(data)} байт данных от клиента.")
    print(f"[Encrypted]: {data[:60]}...")

    decrypted = cipher.decrypt(data).decode()
    print(f"[Decrypted]: {decrypted[:100]}{'...' if len(decrypted) > 100 else ''}")

    # Ответ: просто подтверждение
    response = f"[Сервер] Данные приняты ({len(decrypted)} байт) в {datetime.now()}."
    encrypted_response = cipher.encrypt(response.encode())
    client_socket.sendall(encrypted_response)

    print(f"[{datetime.now()}] Ответ отправлен клиенту.\n" + "-" * 60)
 
