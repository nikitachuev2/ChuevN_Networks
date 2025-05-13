from scapy.all import rdpcap, IP
from collections import Counter

# Чтение захваченных пакетов
packets = rdpcap("packets.pcap")

# Словарь для подсчёта протоколов
protocols = Counter()

# Словарь соответствий номеров IP-протоколов и их имён
proto_names = {
    1: "ICMP",
    2: "IGMP",
    6: "TCP",
    17: "UDP",
    41: "IPv6",
    47: "GRE",
    50: "ESP",
    51: "AH",
    58: "ICMPv6",
    89: "OSPF"
}

# Анализ каждого IP-пакета
for pkt in packets:
    if pkt.haslayer(IP):
        proto_num = pkt[IP].proto
        protocols[proto_num] += 1

print("=== 📊 Статистика по IP-протоколам ===")
total = sum(protocols.values())
print(f"Всего IP-пакетов: {total}\n")

for proto, count in protocols.items():
    name = proto_names.get(proto, f"Неизвестный протокол (#{proto})")
    percent = (count / total) * 100
    print(f"{name:<20} — {count:>4} пакетов ({percent:.1f}%)")
 
