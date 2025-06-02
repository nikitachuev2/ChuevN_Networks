
from scapy.all import *
from collections import defaultdict
from datetime import datetime

# Настройки
watched_domains = {
    "example.local": "127.0.0.1",
    # Можно добавить другие: "google.com": "8.8.8.8"
}
domain_ip_history = defaultdict(set)
last_alerted = defaultdict(str)

def process_packet(packet):
    if packet.haslayer(DNSRR) and packet.haslayer(DNSQR):
        qname = packet[DNSQR].qname.decode().rstrip(".")
        rdata = str(packet[DNSRR].rdata)
        ttl = packet[DNSRR].ttl if hasattr(packet[DNSRR], 'ttl') else "?"

        if qname in watched_domains:
            expected_ip = watched_domains[qname]
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Логирование общего ответа
            print(f"\n[{timestamp}] DNS-ответ:")
            print(f"  • Домен : {qname}")
            print(f"  • IP     : {rdata}")
            print(f"  • TTL    : {ttl}")

            # История IP-адресов
            domain_ip_history[qname].add(rdata)
            print(f"  • Ранее замеченные IP: {', '.join(domain_ip_history[qname])}")

            # Обнаружение spoofing
            if rdata != expected_ip:
                if last_alerted[qname] != rdata:
                    print(f"\n[!!!] Подозрение на DNS Spoofing:")
                    print(f"  Ожидалось: {expected_ip}")
                    print(f"  Получено : {rdata}")
                    last_alerted[qname] = rdata

print("[*] Запуск сниффера DNS на интерфейсе Loopback...")

sniff(
    iface="\\Device\\NPF_Loopback",
    filter="udp port 53",
    prn=process_packet,
    store=0
)
