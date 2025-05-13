from scapy.all import rdpcap, TCP, IP

# Загружаем пакеты из файла
packets = rdpcap("packets.pcap")

print("=== 🧩 Анализ TCP-пакетов ===\n")

# Счётчик для вывода только первых N TCP-пакетов
count = 0
max_packets = 5  # можно увеличить

for pkt in packets:
    if pkt.haslayer(IP) and pkt.haslayer(TCP):
        ip = pkt[IP]
        tcp = pkt[TCP]

        print(f"Пакет #{count + 1}")
        print(f"IP-адрес отправителя     : {ip.src}")
        print(f"IP-адрес получателя      : {ip.dst}")
        print(f"Порт отправителя         : {tcp.sport}")
        print(f"Порт получателя          : {tcp.dport}")
        print(f"Флаги TCP                : {tcp.flags}")
        print(f"Номер последовательности : {tcp.seq}")
        print(f"Номер подтверждения      : {tcp.ack}")
        print(f"Размер TCP-пакета        : {len(tcp)} байт")
        print("-" * 50)

        count += 1
        if count >= max_packets:
            break
 