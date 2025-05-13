from scapy.all import sniff, wrpcap

print("⏳ Начинается захват трафика на 60 секунд...")

# Захват трафика с любого интерфейса (можно указать iface="Wi-Fi" при необходимости)
packets = sniff(timeout=60)

# Сохраняем в pcap-файл
wrpcap("packets.pcap", packets)

print(f"✅ Захват завершён. Количество захваченных пакетов: {len(packets)}")
print("📁 Файл сохранён как: packets.pcap")
