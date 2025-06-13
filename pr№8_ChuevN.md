# Практическая работа № 8

**Выполнил:** Чуев Никита Сергеевич  
**Группа:** P4150  
**Преподаватель:** Васильев Дмитрий Евгеньевич  
**Дата выполнения задания:** 12.06.2025  
**Название дисциплины:** "Сети и протоколы"  

## Задание
Практическое задание:

Последнее практическое задание до 16 июня 16:00

Поднять собственный ВПН между устройствами. Нельзя использовать готовые решения, наподобие протокола vless, outline и так далее. 

Сеть должна быть рабочей, должен проходить пинг между узлами. 

Результат создания каналов и проверка работоспособности — это ваш отчет по работе.

### Результат выполнения работы:

##ОС: Windows 11

 ##Установка необходимых компонентов

scapy — работа с сетевыми пакетами

pycryptodome — симметричное шифрование

python-dotenv — работа с переменными окружения

pip install scapy pycryptodome python-dotenv

Установлен и настроен TAP-Windows драйвер, с официального сайта

Путь установки: C:\Program Files\TAP-Windows\

Установка TAP-адаптера:
C:\Program Files\TAP-Windows\bin\tapinstall.exe" install "C:\Program Files\TAP-Windows\driver\OemVista.inf" tap0901
 

Установлен Npcap для захвата и инжекции трафика:

Установлен с поддержкой WinPcap API

Структура проекта

vpn_project/
│
├── .env                      # Файл с переменными окружения (ключ шифрования)
├── vpn_server.py            # Серверная часть
├── vpn_client.py            # Клиентская часть
├── scapy_ping.py            # Проверка соединения через ICMP
└── Содержимое .env


VPN_KEY=Nikita_ITMO_2025
 
## Настройка TAP-интерфейсов
Запуск через PowerShell от имени администратора:

Get-NetIPAddress | Where-Object { $_.IPAddress -like "169.254.*" } | Remove-NetIPAddress -Confirm:$false

netsh interface ip set address name="Подключение по локальной сети" static 10.8.0.1 255.255.255.0
netsh interface ip set address name="Подключение по локальной сети 2" static 10.8.0.2 255.255.255.0
 
 
## Шифрование канала

Используется симметричное шифрование AES в режиме CTR.

Ключ загружается из .env

Для каждого пакета генерируется уникальный nonce, который передаётся вместе с шифртекстом.

Используется модуль Crypto.Cipher.AES.
 
## Логика взаимодействия

Сервер и клиент обмениваются шифрованными IP-пакетами.

Пакеты считываются с TAP-интерфейса, шифруются и пересылаются по TCP-соединению.

После расшифровки, пакеты возвращаются обратно в TAP-интерфейс ОС, что позволяет ОС видеть эти пакеты как реальные.
 
# Запуск сервера

python vpn_server.py

## логи сервера:

[SERVER] TAP interface initialized
[SERVER] Waiting for connection...
[SERVER] Connected by ('192.168.1.10', 55555)

--- [SERVER] Packet received from TAP ---
###[ IP ]###
  src = 10.8.0.2
  dst = 10.8.0.1
  proto = icmp

[SERVER] Encrypted and sent to client (nonce + ciphertext)
 
## Запуск клиента

python vpn_client.py

## логи клиента:

[CLIENT] Connected to server
[CLIENT] Packet received from server
[CLIENT] Decrypted IP packet:
###[ IP ]###
  src = 10.8.0.2
  dst = 10.8.0.1

[CLIENT] Injected decrypted packet into TAP
 
## Проверка соединения: ICMP-пинг через туннель

python scapy_ping.py
Содержимое scapy_ping.py:

from scapy.all import *

send(IP(src="10.8.0.2", dst="10.8.0.1")/ICMP(), iface="Подключение по локальной сети 2")
 
## Проверка туннеля: системный пинг
ping 10.8.0.1 -S 10.8.0.2
Результат:

Pinging 10.8.0.1 from 10.8.0.2 with 32 bytes of data:
Reply from 10.8.0.1: bytes=32 time<1ms TTL=64
Reply from 10.8.0.1: bytes=32 time<1ms TTL=64
Reply from 10.8.0.1: bytes=32 time<1ms TTL=64
Reply from 10.8.0.1: bytes=32 time<1ms TTL=64

Ping statistics for 10.8.0.1:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
 
Подтверждение двухстороннего канала

Ответные ICMP-пакеты проходят в обратном направлении по тому же VPN-каналу.

Лог клиента:

[CLIENT] Received ICMP reply from 10.8.0.1
[CLIENT] Decrypted and injected into TAP

Лог сервера:

[SERVER] Received ICMP echo-request
[SERVER] Forwarded to TAP interface (10.8.0.1)
 