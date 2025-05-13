# Практическая работа № 2

**Выполнил:** Чуев Никита Сергеевич  
**Группа:** P4150  
**Преподаватель:** Васильев Дмитрий Евгеньевич  
**Дата выполнения задания:** 13.05.2025  
**Название дисциплины:** "Сети и протоколы"  

## Задание
1. Провести анализ пакетов в целом, определить, какие имеются в вашей сети, и вывести статистику.
2. Выбрать один протокол, собрать о нём данные, вывести его «внутренности» и разобрать с точки зрения содержимого пакета (что там есть, какие данные пакет хранит и передаёт).
3. Написать отчёт о проделанной работе.

## Введение

Данная практическая работа будет выполняться двумя способами. 

1. С использованием tshark
2. С использованием библиотеки scapy в Python

## Задание 1

### Сбор и анализ сетевого трафика

Сбор сетевого трафика будет проходить в течение 60 секунд с использованием tshark.

#Выполним следующую команду:

"C:\Program Files\Wireshark\tshark.exe" -i 4 -a duration:60 -w output.pcapng

## Разбор компонентов команды:

### 1. Исполняемый файл
- "C:\Program Files\Wireshark\tshark.exe"  
  - Указывает путь к программе tshark, которая является командной строкой версии программы Wireshark для захвата и анализа сетевого трафика.

### 2. Параметры запуска

#### -i 4
- Описание: Указывает интерфейс для захвата данных.

#### -a duration:60
- Описание: Автоматически останавливает захват через указанный промежуток времени.
- Значение 60: захват продолжится 60 секунд (1 минуту).

#### -w output.pcapng
- Описание: Записывает захваченный сетевой трафик в указанный файл.
- Формат файла .pcapng: формат для хранения сетевых пакетов, используемый большинством сетевых инструментов.

###Результаты захвата будут в : output.pcapng

#Вывод захвата:

"C:\Program Files\Wireshark\tshark.exe" -i 4 -a duration:60

Microsoft Windows [Version 10.0.26100.3775]
(c) Корпорация Майкрософт (Microsoft Corporation). Все права защищены.

C:\Users\NikitaShuyiv\Desktop\ITNO\2_семестр\сети и протоколы\pr2>"C:\Program Files\Wireshark\tshark.exe" -i 4 -a duration:60
Capturing on 'Беспроводная сеть'
    1   0.000000 113.30.190.46 → 192.168.0.101 TCP 54 20175 → 62306 [ACK] Seq=1 Ack=1 Win=489 Len=0
    2   0.000038 192.168.0.101 → 113.30.190.46 TCP 54 [TCP ACKed unseen segment] 62306 → 20175 [ACK] Seq=1 Ack=2 Win=252 Len=0
    3   1.279694 113.30.190.46 → 192.168.0.101 TCP 54 20175 → 51081 [ACK] Seq=1 Ack=1 Win=83 Len=0
    4   1.279735 192.168.0.101 → 113.30.190.46 TCP 54 [TCP ACKed unseen segment] 51081 → 20175 [ACK] Seq=1 Ack=2 Win=255 Len=0
    5   1.536736 113.30.190.46 → 192.168.0.101 TCP 54 20175 → 62308 [ACK] Seq=1 Ack=1 Win=83 Len=0
    6   1.536781 192.168.0.101 → 113.30.190.46 TCP 54 [TCP ACKed unseen segment] 62308 → 20175 [ACK] Seq=1 Ack=2 Win=250 Len=0
    7   2.464558 113.30.190.46 → 192.168.0.101 TCP 54 20175 → 62338 [ACK] Seq=1 Ack=1 Win=83 Len=0
    8   2.464636 192.168.0.101 → 113.30.190.46 TCP 54 [TCP ACKed unseen segment] 62338 → 20175 [ACK] Seq=1 Ack=2 Win=255 Len=0
    9   3.588257 113.30.190.46 → 192.168.0.101 TCP 54 20175 → 61094 [ACK] Seq=1 Ack=1 Win=83 Len=0
   10   3.588300 192.168.0.101 → 113.30.190.46 TCP 54 [TCP ACKed unseen segment] 61094 → 20175 [ACK] Seq=1 Ack=2 Win=252 Len=0
   11   6.401060 113.30.190.46 → 192.168.0.101 TCP 54 20175 → 62248 [ACK] Seq=1 Ack=1 Win=83 Len=0
   12   6.401100 192.168.0.101 → 113.30.190.46 TCP 54 [TCP ACKed unseen segment] 62248 → 20175 [ACK] Seq=1 Ack=2 Win=255 Len=0
   13   7.178582 TPLink_36:2b:c3 → Broadcast    ARP 42 Who has 192.168.0.106? Tell 192.168.0.1
   14   7.548561 192.168.0.101 → 192.168.0.110 TCP 66 62339 → 7680 [SYN] Seq=0 Win=65535 Len=0 MSS=1460 WS=256 SACK_PERM
   15   7.551615 192.168.0.110 → 192.168.0.101 TCP 66 7680 → 62339 [SYN, ACK] Seq=0 Ack=1 Win=65535 Len=0 MSS=1460 WS=256 SACK_PERM
   16   7.551707 192.168.0.101 → 192.168.0.110 TCP 54 62339 → 7680 [ACK] Seq=1 Ack=1 Win=65280 Len=0
   17   7.552097 192.168.0.101 → 192.168.0.110 MS-DO 129 Handshake Message (Request)
   18   7.555357 192.168.0.110 → 192.168.0.101 MS-DO 129 Handshake Message (Reply)
   19   7.555571 192.168.0.101 → 192.168.0.110 MS-DO 75 BitField Message (has 43 of 128 pieces)
   20   7.558572 192.168.0.110 → 192.168.0.101 MS-DO 75 BitField Message (has 42 of 128 pieces)
   21   7.558572 192.168.0.110 → 192.168.0.101 TCP 54 7680 → 62339 [FIN, ACK] Seq=97 Ack=97 Win=65280 Len=0
   22   7.558634 192.168.0.101 → 192.168.0.110 TCP 54 62339 → 7680 [ACK] Seq=97 Ack=98 Win=65280 Len=0
   23   7.559239 192.168.0.101 → 192.168.0.110 TCP 54 62339 → 7680 [FIN, ACK] Seq=97 Ack=98 Win=65280 Len=0
   24   7.561932 192.168.0.110 → 192.168.0.101 TCP 54 7680 → 62339 [ACK] Seq=98 Ack=98 Win=65280 Len=0
   25   8.202695 TPLink_36:2b:c3 → Broadcast    ARP 42 Who has 192.168.0.108? Tell 192.168.0.1
   26   8.202750 TPLink_36:2b:c3 → Broadcast    ARP 42 Who has 192.168.0.105? Tell 192.168.0.1
   27   8.960601 113.30.190.46 → 192.168.0.101 TCP 54 20175 → 51223 [ACK] Seq=1 Ack=1 Win=83 Len=0
   28   8.960678 192.168.0.101 → 113.30.190.46 TCP 54 [TCP ACKed unseen segment] 51223 → 20175 [ACK] Seq=1 Ack=2 Win=252 Len=0
   29   9.125084 TPLink_36:2b:c3 → Broadcast    ARP 42 Who has 192.168.0.108? Tell 192.168.0.1
   30  10.230231 192.168.0.101 → 192.168.0.110 TCP 66 62340 → 7680 [SYN] Seq=0 Win=65535 Len=0 MSS=1460 WS=256 SACK_PERM
   31  10.233886 192.168.0.110 → 192.168.0.101 TCP 66 7680 → 62340 [SYN, ACK] Seq=0 Ack=1 Win=65535 Len=0 MSS=1460 WS=256 SACK_PERM
   32  10.234009 192.168.0.101 → 192.168.0.110 TCP 54 62340 → 7680 [ACK] Seq=1 Ack=1 Win=65280 Len=0
   33  10.234144 192.168.0.101 → 192.168.0.110 MS-DO 129 Handshake Message (Request)
   34  10.237783 192.168.0.110 → 192.168.0.101 MS-DO 129 Handshake Message (Reply)
   35  10.237783 192.168.0.110 → 192.168.0.101 TCP 54 7680 → 62340 [FIN, ACK] Seq=76 Ack=76 Win=65280 Len=0
   36  10.237883 192.168.0.101 → 192.168.0.110 TCP 54 62340 → 7680 [ACK] Seq=76 Ack=77 Win=65280 Len=0
   37  10.238042 192.168.0.101 → 192.168.0.110 TCP 54 62340 → 7680 [FIN, ACK] Seq=76 Ack=77 Win=65280 Len=0
   38  10.241732 192.168.0.110 → 192.168.0.101 TCP 54 7680 → 62340 [ACK] Seq=77 Ack=77 Win=65280 Len=0
   39  11.777165 113.30.190.46 → 192.168.0.101 TCP 54 20175 → 61099 [ACK] Seq=1 Ack=1 Win=528 Len=0
   40  11.777241 192.168.0.101 → 113.30.190.46 TCP 54 [TCP ACKed unseen segment] 61099 → 20175 [ACK] Seq=1 Ack=2 Win=251 Len=0
   41  13.313661 113.30.190.46 → 192.168.0.101 TCP 54 20175 → 62316 [ACK] Seq=1 Ack=1 Win=286 Len=0
   42  13.313744 192.168.0.101 → 113.30.190.46 TCP 54 [TCP ACKed unseen segment] 62316 → 20175 [ACK] Seq=1 Ack=2 Win=252 Len=0
   43  13.324081  192.168.0.1 → 192.168.0.255 UDP 370 25669 → 20002 Len=328
   44  13.825245 113.30.190.46 → 192.168.0.101 TCP 54 20175 → 60898 [ACK] Seq=1 Ack=1 Win=83 Len=0
   45  13.825292 192.168.0.101 → 113.30.190.46 TCP 54 [TCP ACKed unseen segment] 60898 → 20175 [ACK] Seq=1 Ack=2 Win=253 Len=0
   46  14.142169 TPLink_36:2b:c3 → Broadcast    ARP 42 Who has 192.168.0.102? Tell 192.168.0.1
   47  15.104693 113.30.190.46 → 192.168.0.101 TCP 54 [TCP Dup ACK 1#1] 20175 → 62306 [ACK] Seq=1 Ack=1 Win=489 Len=0
   48  15.104729 192.168.0.101 → 113.30.190.46 TCP 54 [TCP Dup ACK 2#1] 62306 → 20175 [ACK] Seq=1 Ack=2 Win=252 Len=0
   49  15.166805 TPLink_36:2b:c3 → Broadcast    ARP 42 Who has 192.168.0.102? Tell 192.168.0.1
   50  16.191048 TPLink_36:2b:c3 → Broadcast    ARP 42 Who has 192.168.0.102? Tell 192.168.0.1
   51  16.384974 113.30.190.46 → 192.168.0.101 TCP 54 [TCP Dup ACK 3#1] 20175 → 51081 [ACK] Seq=1 Ack=1 Win=83 Len=0
   52  16.385018 192.168.0.101 → 113.30.190.46 TCP 54 [TCP Dup ACK 4#1] 51081 → 20175 [ACK] Seq=1 Ack=2 Win=255 Len=0
   53  16.641240 113.30.190.46 → 192.168.0.101 TCP 54 [TCP Dup ACK 5#1] 20175 → 62308 [ACK] Seq=1 Ack=1 Win=83 Len=0
   54  16.641281 192.168.0.101 → 113.30.190.46 TCP 54 [TCP Dup ACK 6#1] 62308 → 20175 [ACK] Seq=1 Ack=2 Win=250 Len=0
   55  17.665995 113.30.190.46 → 192.168.0.101 TCP 54 [TCP Dup ACK 7#1] 20175 → 62338 [ACK] Seq=1 Ack=1 Win=83 Len=0
   56  17.666034 192.168.0.101 → 113.30.190.46 TCP 54 [TCP Dup ACK 8#1] 62338 → 20175 [ACK] Seq=1 Ack=2 Win=255 Len=0
   57  18.689920 113.30.190.46 → 192.168.0.101 TCP 54 [TCP Dup ACK 9#1] 20175 → 61094 [ACK] Seq=1 Ack=1 Win=83 Len=0
   58  18.690002 192.168.0.101 → 113.30.190.46 TCP 54 [TCP Dup ACK 10#1] 61094 → 20175 [ACK] Seq=1 Ack=2 Win=252 Len=0
   59  19.160266 TPLink_36:2b:c3 → Broadcast    ARP 42 Who has 192.168.0.106? Tell 192.168.0.1
   60  20.492058  192.168.0.1 → 224.0.0.252  IGMPv3 50 Membership Query, specific for group 224.0.0.252
   61  20.709343 192.168.0.101 → 224.0.0.22   IGMPv3 54 Membership Report / Join group 224.0.0.252 for any sources
   62  20.901468 192.168.0.110 → 224.0.0.22   IGMPv3 54 Membership Report / Join group 224.0.0.252 for any sources
   63  21.506233 113.30.190.46 → 192.168.0.101 TCP 54 [TCP Dup ACK 11#1] 20175 → 62248 [ACK] Seq=1 Ack=1 Win=83 Len=0
   64  21.506308 192.168.0.101 → 113.30.190.46 TCP 54 [TCP Dup ACK 12#1] 62248 → 20175 [ACK] Seq=1 Ack=2 Win=255 Len=0
   65  24.065919 113.30.190.46 → 192.168.0.101 TCP 54 [TCP Dup ACK 27#1] 20175 → 51223 [ACK] Seq=1 Ack=1 Win=83 Len=0
   66  24.066002 192.168.0.101 → 113.30.190.46 TCP 54 [TCP Dup ACK 28#1] 51223 → 20175 [ACK] Seq=1 Ack=2 Win=252 Len=0
   67  26.881959 113.30.190.46 → 192.168.0.101 TCP 54 [TCP Dup ACK 39#1] 20175 → 61099 [ACK] Seq=1 Ack=1 Win=528 Len=0
   68  26.881997 192.168.0.101 → 113.30.190.46 TCP 54 [TCP Dup ACK 40#1] 61099 → 20175 [ACK] Seq=1 Ack=2 Win=251 Len=0
   69  28.172726 TPLink_36:2b:c3 → Broadcast    ARP 42 Who has 192.168.0.105? Tell 192.168.0.1
   70  28.333060 113.30.190.46 → 192.168.0.101 TCP 170 [TCP Previous segment not captured] 20175 → 60898 [PSH, ACK] Seq=2 Ack=1 Win=83 Len=116
   71  28.384300 192.168.0.101 → 113.30.190.46 TCP 54 60898 → 20175 [ACK] Seq=1 Ack=118 Win=253 Len=0
   72  28.418851 113.30.190.46 → 192.168.0.101 TCP 54 [TCP Dup ACK 41#1] 20175 → 62316 [ACK] Seq=1 Ack=1 Win=286 Len=0
   73  28.418900 192.168.0.101 → 113.30.190.46 TCP 54 [TCP Dup ACK 42#1] 62316 → 20175 [ACK] Seq=1 Ack=2 Win=252 Len=0
   74  29.034568 192.168.0.110 → 192.168.0.101 TCP 66 6058 → 7680 [SYN] Seq=0 Win=65535 Len=0 MSS=1460 WS=256 SACK_PERM
   75  29.034823 192.168.0.101 → 192.168.0.110 TCP 66 7680 → 6058 [SYN, ACK] Seq=0 Ack=1 Win=65535 Len=0 MSS=1460 WS=256 SACK_PERM
   76  29.038160 192.168.0.110 → 192.168.0.101 TCP 54 6058 → 7680 [ACK] Seq=1 Ack=1 Win=65280 Len=0
   77  29.038160 192.168.0.110 → 192.168.0.101 MS-DO 129 Handshake Message (Request)
   78  29.038935 192.168.0.101 → 192.168.0.110 MS-DO 129 Handshake Message (Reply)
   79  29.039008 192.168.0.101 → 192.168.0.110 TCP 54 7680 → 6058 [FIN, ACK] Seq=76 Ack=76 Win=65280 Len=0
   80  29.042063 192.168.0.110 → 192.168.0.101 TCP 54 6058 → 7680 [FIN, ACK] Seq=76 Ack=76 Win=65280 Len=0
   81  29.042063 192.168.0.110 → 192.168.0.101 TCP 54 6058 → 7680 [ACK] Seq=77 Ack=77 Win=65280 Len=0
   82  29.355213 192.168.0.110 → 192.168.0.101 TCP 54 [TCP Retransmission] 6058 → 7680 [FIN, ACK] Seq=76 Ack=77 Win=65280 Len=0
   83  29.355295 192.168.0.101 → 192.168.0.110 TCP 54 [TCP ZeroWindow] 7680 → 6058 [ACK] Seq=77 Ack=77 Win=0 Len=0
   84  29.618161 192.168.0.101 → 113.30.190.46 TCP 189 51081 → 20175 [PSH, ACK] Seq=1 Ack=2 Win=255 Len=135
   85  29.653549 113.30.190.46 → 192.168.0.101 TCP 54 [TCP Previous segment not captured] 20175 → 51081 [ACK] Seq=2 Ack=136 Win=83 Len=0
   86  29.663710 113.30.190.46 → 192.168.0.101 TCP 259 20175 → 51081 [PSH, ACK] Seq=2 Ack=136 Win=83 Len=205
   87  29.711066 192.168.0.101 → 113.30.190.46 TCP 54 51081 → 20175 [ACK] Seq=136 Ack=207 Win=255 Len=0
   88  30.210045 113.30.190.46 → 192.168.0.101 TCP 54 [TCP Dup ACK 1#2] 20175 → 62306 [ACK] Seq=1 Ack=1 Win=489 Len=0
   89  30.210119 192.168.0.101 → 113.30.190.46 TCP 54 [TCP Dup ACK 2#2] 62306 → 20175 [ACK] Seq=1 Ack=2 Win=252 Len=0
   90  31.142448 TPLink_36:2b:c3 → Broadcast    ARP 42 Who has 192.168.0.106? Tell 192.168.0.1
   91  31.746825 113.30.190.46 → 192.168.0.101 TCP 54 [TCP Dup ACK 5#2] 20175 → 62308 [ACK] Seq=1 Ack=1 Win=83 Len=0
   92  31.746902 192.168.0.101 → 113.30.190.46 TCP 54 [TCP Dup ACK 6#2] 62308 → 20175 [ACK] Seq=1 Ack=2 Win=250 Len=0
   93  31.757992 192.168.0.110 → 224.0.0.251  MDNS 696 Standard query response 0x0000 PTR DESKTOP-HD37S09._dosvc._tcp.local SRV 0 0 7680 DESKTOP-HD37S09.local TXT
   94  31.758218 fe80::ef4:6af6:a5ca:deb5 → ff02::fb     MDNS 716 Standard query response 0x0000 PTR DESKTOP-HD37S09._dosvc._tcp.local SRV 0 0 7680 DESKTOP-HD37S09.local TXT
   95  31.758368 192.168.0.110 → 224.0.0.251  MDNS 93 Standard query 0x0000 ANY DESKTOP-HD37S09._dosvc._tcp.local, "QM" question
   96  31.859112 fe80::ef4:6af6:a5ca:deb5 → ff02::fb     MDNS 113 Standard query 0x0000 ANY DESKTOP-HD37S09._dosvc._tcp.local, "QM" question
   97  32.064187 192.168.0.110 → 224.0.0.251  MDNS 93 Standard query 0x0000 ANY DESKTOP-HD37S09._dosvc._tcp.local, "QM" question
   98  32.064497 fe80::ef4:6af6:a5ca:deb5 → ff02::fb     MDNS 113 Standard query 0x0000 ANY DESKTOP-HD37S09._dosvc._tcp.local, "QM" question
   99  32.268465 192.168.0.110 → 224.0.0.251  MDNS 93 Standard query 0x0000 ANY DESKTOP-HD37S09._dosvc._tcp.local, "QM" question
  100  32.268632 fe80::ef4:6af6:a5ca:deb5 → ff02::fb     MDNS 113 Standard query 0x0000 ANY DESKTOP-HD37S09._dosvc._tcp.local, "QM" question
  101  32.577210 192.168.0.110 → 224.0.0.251  MDNS 761 Standard query response 0x0000 PTR, cache flush DESKTOP-HD37S09._dosvc._tcp.local SRV, cache flush 0 0 7680 DESKTOP-HD37S09.local TXT, cache flush A, cache flush 192.168.0.110 AAAA, cache flush fe80::ef4:6af6:a5ca:deb5
  102  32.577546 fe80::ef4:6af6:a5ca:deb5 → ff02::fb     MDNS 781 Standard query response 0x0000 PTR, cache flush DESKTOP-HD37S09._dosvc._tcp.local SRV, cache flush 0 0 7680 DESKTOP-HD37S09.local TXT, cache flush A, cache flush 192.168.0.110 AAAA, cache flush fe80::ef4:6af6:a5ca:deb5
  103  32.579679 192.168.0.110 → 224.0.0.251  MDNS 697 Standard query response 0x0000 SRV, cache flush 0 0 7680 DESKTOP-HD37S09.local TXT, cache flush A, cache flush 192.168.0.110 AAAA, cache flush fe80::ef4:6af6:a5ca:deb5
  104  32.679486 fe80::ef4:6af6:a5ca:deb5 → ff02::fb     MDNS 717 Standard query response 0x0000 SRV, cache flush 0 0 7680 DESKTOP-HD37S09.local TXT, cache flush A, cache flush 192.168.0.110 AAAA, cache flush fe80::ef4:6af6:a5ca:deb5
  105  32.770154 113.30.190.46 → 192.168.0.101 TCP 54 [TCP Dup ACK 7#2] 20175 → 62338 [ACK] Seq=1 Ack=1 Win=83 Len=0
  106  32.770196 192.168.0.101 → 113.30.190.46 TCP 54 [TCP Dup ACK 8#2] 62338 → 20175 [ACK] Seq=1 Ack=2 Win=255 Len=0
  107  33.190806 TPLink_36:2b:c3 → Broadcast    ARP 42 Who has 192.168.0.102? Tell 192.168.0.1
  108  33.198685 CloudNetwork_ed:85:59 → TPLink_36:2b:c3 ARP 42 Who has 192.168.0.1? Tell 192.168.0.101
  109  33.201353 TPLink_36:2b:c3 → CloudNetwork_ed:85:59 ARP 42 192.168.0.1 is at 5c:e9:31:36:2b:c3
  110  33.794817 113.30.190.46 → 192.168.0.101 TCP 54 [TCP Dup ACK 9#2] 20175 → 61094 [ACK] Seq=1 Ack=1 Win=83 Len=0
  111  33.794889 192.168.0.101 → 113.30.190.46 TCP 54 [TCP Dup ACK 10#2] 61094 → 20175 [ACK] Seq=1 Ack=2 Win=252 Len=0
  112  36.610805 113.30.190.46 → 192.168.0.101 TCP 54 [TCP Dup ACK 11#2] 20175 → 62248 [ACK] Seq=1 Ack=1 Win=83 Len=0
  113  36.610843 192.168.0.101 → 113.30.190.46 TCP 54 [TCP Dup ACK 12#2] 62248 → 20175 [ACK] Seq=1 Ack=2 Win=255 Len=0
  114  38.688635 113.30.190.46 → 192.168.0.101 TCP 170 [TCP Previous segment not captured] 20175 → 51223 [PSH, ACK] Seq=2 Ack=1 Win=83 Len=116
  115  38.740174 192.168.0.101 → 113.30.190.46 TCP 54 51223 → 20175 [ACK] Seq=1 Ack=118 Win=252 Len=0
  116  39.130806 TPLink_36:2b:c3 → Broadcast    ARP 42 Who has 192.168.0.107? Tell 192.168.0.1
  117  41.987054 113.30.190.46 → 192.168.0.101 TCP 54 [TCP Dup ACK 39#2] 20175 → 61099 [ACK] Seq=1 Ack=1 Win=528 Len=0
  118  41.987135 192.168.0.101 → 113.30.190.46 TCP 54 [TCP Dup ACK 40#2] 61099 → 20175 [ACK] Seq=1 Ack=2 Win=251 Len=0
  119  43.124180 TPLink_36:2b:c3 → Broadcast    ARP 42 Who has 192.168.0.106? Tell 192.168.0.1
  120  43.328997  192.168.0.1 → 192.168.0.255 UDP 370 38593 → 20002 Len=328
  121  43.522762 113.30.190.46 → 192.168.0.101 TCP 54 [TCP Keep-Alive] 20175 → 60898 [ACK] Seq=117 Ack=1 Win=83 Len=0
  122  43.522762 113.30.190.46 → 192.168.0.101 TCP 54 [TCP Dup ACK 41#2] 20175 → 62316 [ACK] Seq=1 Ack=1 Win=286 Len=0
  123  43.522844 192.168.0.101 → 113.30.190.46 TCP 54 [TCP Keep-Alive ACK] 60898 → 20175 [ACK] Seq=1 Ack=118 Win=253 Len=0
  124  43.523018 192.168.0.101 → 113.30.190.46 TCP 54 [TCP Dup ACK 42#2] 62316 → 20175 [ACK] Seq=1 Ack=2 Win=252 Len=0
  125  44.803173 113.30.190.46 → 192.168.0.101 TCP 54 [TCP Keep-Alive] 20175 → 51081 [ACK] Seq=206 Ack=136 Win=83 Len=0
  126  44.803252 192.168.0.101 → 113.30.190.46 TCP 54 [TCP Keep-Alive ACK] 51081 → 20175 [ACK] Seq=136 Ack=207 Win=255 Len=0
  127  45.174306 TPLink_36:2b:c3 → Broadcast    ARP 42 Who has 192.168.0.102? Tell 192.168.0.1
  128  45.315433 113.30.190.46 → 192.168.0.101 TCP 54 [TCP Dup ACK 1#3] 20175 → 62306 [ACK] Seq=1 Ack=1 Win=489 Len=0
  129  45.315510 192.168.0.101 → 113.30.190.46 TCP 54 [TCP Dup ACK 2#3] 62306 → 20175 [ACK] Seq=1 Ack=2 Win=252 Len=0
  130  46.851501 113.30.190.46 → 192.168.0.101 TCP 54 [TCP Dup ACK 5#3] 20175 → 62308 [ACK] Seq=1 Ack=1 Win=83 Len=0
  131  46.851577 192.168.0.101 → 113.30.190.46 TCP 54 [TCP Dup ACK 6#3] 62308 → 20175 [ACK] Seq=1 Ack=2 Win=250 Len=0
  132  47.563278 192.168.0.101 → 192.168.0.110 TCP 66 62341 → 7680 [SYN] Seq=0 Win=65535 Len=0 MSS=1460 WS=256 SACK_PERM
  133  47.566234 192.168.0.110 → 192.168.0.101 TCP 66 7680 → 62341 [SYN, ACK] Seq=0 Ack=1 Win=65535 Len=0 MSS=1460 WS=256 SACK_PERM
  134  47.566318 192.168.0.101 → 192.168.0.110 TCP 54 62341 → 7680 [ACK] Seq=1 Ack=1 Win=65280 Len=0
  135  47.566677 192.168.0.101 → 192.168.0.110 MS-DO 129 Handshake Message (Request)
  136  47.569997 192.168.0.110 → 192.168.0.101 MS-DO 129 Handshake Message (Reply)
  137  47.570141 192.168.0.101 → 192.168.0.110 MS-DO 75 BitField Message (has 43 of 128 pieces)
  138  47.572849 192.168.0.110 → 192.168.0.101 MS-DO 75 BitField Message (has 42 of 128 pieces)
  139  47.572849 192.168.0.110 → 192.168.0.101 TCP 54 7680 → 62341 [FIN, ACK] Seq=97 Ack=97 Win=65280 Len=0
  140  47.572892 192.168.0.101 → 192.168.0.110 TCP 54 62341 → 7680 [ACK] Seq=97 Ack=98 Win=65280 Len=0
  141  47.573105 192.168.0.101 → 192.168.0.110 TCP 54 62341 → 7680 [FIN, ACK] Seq=97 Ack=98 Win=65280 Len=0
  142  47.575892 192.168.0.110 → 192.168.0.101 TCP 54 7680 → 62341 [ACK] Seq=98 Ack=98 Win=65280 Len=0
  143  47.875390 113.30.190.46 → 192.168.0.101 TCP 54 [TCP Dup ACK 7#3] 20175 → 62338 [ACK] Seq=1 Ack=1 Win=83 Len=0
  144  47.875434 192.168.0.101 → 113.30.190.46 TCP 54 [TCP Dup ACK 8#3] 62338 → 20175 [ACK] Seq=1 Ack=2 Win=255 Len=0
  145  48.899906 113.30.190.46 → 192.168.0.101 TCP 54 [TCP Dup ACK 9#3] 20175 → 61094 [ACK] Seq=1 Ack=1 Win=83 Len=0
  146  48.900011 192.168.0.101 → 113.30.190.46 TCP 54 [TCP Dup ACK 10#3] 61094 → 20175 [ACK] Seq=1 Ack=2 Win=252 Len=0
  147  48.928930 113.30.190.46 → 192.168.0.101 TCP 196 [TCP Previous segment not captured] 20175 → 61099 [PSH, ACK] Seq=2 Ack=1 Win=528 Len=142
  148  48.971327 192.168.0.101 → 113.30.190.46 TCP 54 61099 → 20175 [ACK] Seq=1 Ack=144 Win=251 Len=0
  149  50.413915 192.168.0.101 → 192.168.0.110 TCP 66 62342 → 7680 [SYN] Seq=0 Win=65535 Len=0 MSS=1460 WS=256 SACK_PERM
  150  50.417344 192.168.0.110 → 192.168.0.101 TCP 66 7680 → 62342 [SYN, ACK] Seq=0 Ack=1 Win=65535 Len=0 MSS=1460 WS=256 SACK_PERM
  151  50.417465 192.168.0.101 → 192.168.0.110 TCP 54 62342 → 7680 [ACK] Seq=1 Ack=1 Win=65280 Len=0
  152  50.417595 192.168.0.101 → 192.168.0.110 MS-DO 129 Handshake Message (Request)
  153  50.421238 192.168.0.110 → 192.168.0.101 MS-DO 129 Handshake Message (Reply)
  154  50.421238 192.168.0.110 → 192.168.0.101 TCP 54 7680 → 62342 [FIN, ACK] Seq=76 Ack=76 Win=65280 Len=0
  155  50.421326 192.168.0.101 → 192.168.0.110 TCP 54 62342 → 7680 [ACK] Seq=76 Ack=77 Win=65280 Len=0
  156  50.421435 192.168.0.101 → 192.168.0.110 TCP 54 62342 → 7680 [FIN, ACK] Seq=76 Ack=77 Win=65280 Len=0
  157  50.424805 192.168.0.110 → 192.168.0.101 TCP 54 7680 → 62342 [ACK] Seq=77 Ack=77 Win=65280 Len=0
  158  51.418861  192.168.0.1 → 239.255.255.250 IGMPv3 50 Membership Query, specific for group 239.255.255.250
  159  51.703741 192.168.0.101 → 224.0.0.22   IGMPv3 54 Membership Report / Join group 239.255.255.250 for any sources
  160  51.715790 113.30.190.46 → 192.168.0.101 TCP 54 [TCP Dup ACK 11#3] 20175 → 62248 [ACK] Seq=1 Ack=1 Win=83 Len=0
  161  51.715823 192.168.0.101 → 113.30.190.46 TCP 54 [TCP Dup ACK 12#3] 62248 → 20175 [ACK] Seq=1 Ack=2 Win=255 Len=0
  162  51.930795 192.168.0.110 → 224.0.0.22   IGMPv3 54 Membership Report / Join group 239.255.255.250 for any sources
  163  53.159999 TPLink_36:2b:c3 → Broadcast    ARP 42 Who has 192.168.0.105? Tell 192.168.0.1
  164  54.020338 113.30.190.46 → 192.168.0.101 TCP 54 [TCP Keep-Alive] 20175 → 51223 [ACK] Seq=117 Ack=1 Win=83 Len=0
  165  54.020411 192.168.0.101 → 113.30.190.46 TCP 54 [TCP Keep-Alive ACK] 51223 → 20175 [ACK] Seq=1 Ack=118 Win=252 Len=0
  166  55.207868 TPLink_36:2b:c3 → Broadcast    ARP 42 Who has 192.168.0.106? Tell 192.168.0.1
  167  57.153638 TPLink_36:2b:c3 → Broadcast    ARP 42 Who has 192.168.0.102? Tell 192.168.0.1
  168  58.628307 113.30.190.46 → 192.168.0.101 TCP 54 [TCP Keep-Alive] 20175 → 60898 [ACK] Seq=117 Ack=1 Win=83 Len=0
  169  58.628307 113.30.190.46 → 192.168.0.101 TCP 54 [TCP Dup ACK 41#3] 20175 → 62316 [ACK] Seq=1 Ack=1 Win=286 Len=0
  170  58.628396 192.168.0.101 → 113.30.190.46 TCP 54 [TCP Keep-Alive ACK] 60898 → 20175 [ACK] Seq=1 Ack=118 Win=253 Len=0
  171  58.628480 192.168.0.101 → 113.30.190.46 TCP 54 [TCP Dup ACK 42#3] 62316 → 20175 [ACK] Seq=1 Ack=2 Win=252 Len=0
  172  59.202085 TPLink_36:2b:c3 → Broadcast    ARP 42 Who has 192.168.0.107? Tell 192.168.0.1
172 packets captured

C:\Users\NikitaShuyiv\Desktop\ITNO\2_семестр\сети и протоколы\pr2>

##Краткие выводы:

### Основные наблюдения:
- Захваченный трафик состоял в основном из TCP-пакетов, что свидетельствует о сетевой активности между адресами 192.168.0.101 и 113.30.190.46.
- Во время захвата наблюдались различные состояния TCP-соединений, включая:
  - Отправка и получение ACK (подтверждений) на разные порты.
  - Заметные SYN и SYN-ACK пакеты, свидетельствующие о процессе установления соединения.
- Также был зафиксирован ARP-трафик от устройства TPLink, что подтверждает активное исследование сети для определения IP-адресов устройств.
- В конце захвата, TCP-соединения были корректно завершены с использованием FIN и ACK пакетов, что говорит о корректном завершении коммуникации.

### Статистика по протоколам

 Выполним для файла output.pcapng   команду:

 "C:\Program Files\Wireshark\tshark.exe" -r output.pcapng -q -z io,phs

- tshark.exe — командная версия Wireshark для анализа сетевого трафика.
- -r output.pcapng — читает данные из ранее сохранённого файла захвата output.pcapng.
- -q — тихий режим, отключает вывод подробных данных пакетов, чтобы показывать только итоговую статистику.
- -z io,phs — выводит статистику ввода-вывода, представляющую информацию о пакетах и байтах по времени (Protocol Hierarchy Statistics), то есть показывает распределение протоколов и их активность.

 Вывод:

 Microsoft Windows [Version 10.0.26100.3775]
(c) Корпорация Майкрософт (Microsoft Corporation). Все права защищены.

C:\Users\NikitaShuyiv\Desktop\ITNO\2_семестр\сети и протоколы\pr2>"C:\Program Files\Wireshark\tshark.exe" -r output.pcapng -q -z io,phs

===================================================================
Protocol Hierarchy Statistics
Filter:

eth                                      frames:596 bytes:646260
  ip                                     frames:565 bytes:641937
    tcp                                  frames:501 bytes:632132
      data                               frames:201 bytes:614658
      msdo                               frames:12 bytes:1298
      hipercontracer                     frames:1 bytes:270
    udp                                  frames:30 bytes:8085
      data                               frames:6 bytes:1338
      mdns                               frames:14 bytes:3233
      ssdp                               frames:10 bytes:3514
    igmp                                 frames:34 bytes:1720
  arp                                    frames:15 bytes:630
  ipv6                                   frames:16 bytes:3693
    udp                                  frames:14 bytes:3513
      mdns                               frames:14 bytes:3513
    icmpv6                               frames:2 bytes:180
===================================================================

C:\Users\NikitaShuyiv\Desktop\ITNO\2_семестр\сети и протоколы\pr2>


## Краткий вывод

Большая часть трафика приходится на протокол IP и TCP, с преобладанием данных и управляющих сообщений. Также видно активность UDP (в том числе mDNS, SSDP) и немного трафика IPv6 и ICMPv6. Это указывает на разнообразие протоколов в сети, доминирующими являются обычные IP- и TCP-соединения с некоторой дополнительной сетевой активностью.

##Выполним с помощью Python:

Запустим файл  capture.py для сбора трафика в течении 60 секунд
Результат  сбора будет в  файле packets.pcap
Проведем анализ полученого с помощью скрипта  analyze.py

Вывод:

Microsoft Windows [Version 10.0.26100.3775]
(c) Корпорация Майкрософт (Microsoft Corporation). Все права защищены.

C:\Users\NikitaShuyiv\Desktop\ITNO\2_семестр\сети и протоколы\pr2>python analyze.py
=== 📊 Статистика по IP-протоколам ===
Всего IP-пакетов: 171

UDP                  —   24 пакетов (14.0%)
TCP                  —  137 пакетов (80.1%)
IGMP                 —   10 пакетов (5.8%)

C:\Users\NikitaShuyiv\Desktop\ITNO\2_семестр\сети и протоколы\pr2>

## Краткий вывод

В сети зафиксировано всего 171 IP-пакет. Основную часть составляют TCP-пакеты (80.1%), далее идут UDP (14.0%) и IGMP (5.8%). Это свидетельствует о доминировании TCP-соединений, что характерно для большинства приложений, использующих надежную передачу данных, а также наличию активности внутри сетевой инфраструктуры через UDP и IGMP.

Вывод по заданию № 1:
В сети выявлены активные протоколы: TCP, UDP, IGMP, ARP и IPv6. Доминируют TCP и IP-пакеты, что указывает на широкое использование надежных соединений. Также наблюдается активность UDP (в том числе mDNS и SSDP) для локальных сервисов и устройств. Анализ показывает разнообразие протоколов и характерную сетевую активность.


### Задание 2 
 #Анализ протокола.
Разбор TCP пакета
Посмотреть "внутренности" одного TCP-пакета
Выполним команду:

"C:\Program Files\Wireshark\tshark.exe" -r output.pcapng -Y "tcp" -V > tcp_details.txt

- -r output.pcapng — читает пакеты из файла захвата output.pcapng.
- -Y "tcp" — применяет фильтр вывода, показывая только TCP-пакеты.
- -V — выводит подробную информацию о каждом пакете.
- > tcp_details.txt — перенаправляет подробный вывод в файл tcp_details.txt.
Вывод в файле tcp_details.txt

Выполним аналогично для вывода в командную строку для наглядности в отчете. в реальном времени 


Команда:

"C:\Program Files\Wireshark\tshark.exe" -i 4 -a duration:1 -f "tcp" -V" 

- -i 4 — захватывает трафик с интерфейса номер 4.
- -a duration:1 — ограничивает захват одним минутным интервалом (или, в некоторых случаях, сообщением о продолжительности, если задано в минутах).
- -f "tcp" — фильтрует трафик, собирая только TCP-пакеты в процессе захвата.
- -V — выводит подробную информацию о каждом захваченном пакете.

Вывод:

Microsoft Windows [Version 10.0.26100.3775]
(c) Корпорация Майкрософт (Microsoft Corporation). Все права защищены.

C:\Users\NikitaShuyiv\Desktop\ITNO\2_семестр\сети и протоколы\ChuevN_Networks\Practic№2>"C:\Program Files\Wireshark\tshark.exe" -i 4 -a duration:1 -f "tcp" -V"
Capturing on 'Беспроводная сеть'
0 packets captured

C:\Users\NikitaShuyiv\Desktop\ITNO\2_семестр\сети и протоколы\ChuevN_Networks\Practic№2>"C:\Program Files\Wireshark\tshark.exe" -i 4 -a duration:1 -f "tcp" -V"
Capturing on 'Беспроводная сеть'
Frame 1: 196 bytes on wire (1568 bits), 196 bytes captured (1568 bits) on interface \Device\NPF_{788C51AF-3B1E-48D0-B065-B13BF31D419A}, id 0
    Section number: 1
    Interface id: 0 (\Device\NPF_{788C51AF-3B1E-48D0-B065-B13BF31D419A})
        Interface name: \Device\NPF_{788C51AF-3B1E-48D0-B065-B13BF31D419A}
        Interface description: Беспроводная сеть
    Encapsulation type: Ethernet (1)
    Arrival Time: May 13, 2025 14:08:41.982300000 RTZ 2 (зима)
    UTC Arrival Time: May 13, 2025 11:08:41.982300000 UTC
    Epoch Arrival Time: 1747134521.982300000
    [Time shift for this packet: 0.000000000 seconds]
    [Time delta from previous captured frame: 0.000000000 seconds]
    [Time delta from previous displayed frame: 0.000000000 seconds]
    [Time since reference or first frame: 0.000000000 seconds]
    Frame Number: 1
    Frame Length: 196 bytes (1568 bits)
    Capture Length: 196 bytes (1568 bits)
    [Frame is marked: False]
    [Frame is ignored: False]
    [Protocols in frame: eth:ethertype:ip:tcp:data]
Ethernet II, Src: TPLink_36:2b:c3 (5c:e9:31:36:2b:c3), Dst: CloudNetwork_ed:85:59 (2c:9c:58:ed:85:59)
    Destination: CloudNetwork_ed:85:59 (2c:9c:58:ed:85:59)
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
    Source: TPLink_36:2b:c3 (5c:e9:31:36:2b:c3)
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
    Type: IPv4 (0x0800)
    [Stream index: 0]
Internet Protocol Version 4, Src: 113.30.190.46, Dst: 192.168.0.101
    0100 .... = Version: 4
    .... 0101 = Header Length: 20 bytes (5)
    Differentiated Services Field: 0x00 (DSCP: CS0, ECN: Not-ECT)
        0000 00.. = Differentiated Services Codepoint: Default (0)
        .... ..00 = Explicit Congestion Notification: Not ECN-Capable Transport (0)
    Total Length: 182
    Identification: 0x7096 (28822)
    010. .... = Flags: 0x2, Don't fragment
        0... .... = Reserved bit: Not set
        .1.. .... = Don't fragment: Set
        ..0. .... = More fragments: Not set
    ...0 0000 0000 0000 = Fragment Offset: 0
    Time to Live: 55
    Protocol: TCP (6)
    Header Checksum: 0xe251 [validation disabled]
    [Header checksum status: Unverified]
    Source Address: 113.30.190.46
    Destination Address: 192.168.0.101
    [Stream index: 0]
Transmission Control Protocol, Src Port: 20175, Dst Port: 58342, Seq: 1, Ack: 1, Len: 142
    Source Port: 20175
    Destination Port: 58342
    [Stream index: 0]
    [Stream Packet Number: 1]
    [Conversation completeness: Incomplete (0)]
        ..0. .... = RST: Absent
        ...0 .... = FIN: Absent
        .... 0... = Data: Absent
        .... .0.. = ACK: Absent
        .... ..0. = SYN-ACK: Absent
        .... ...0 = SYN: Absent
        [Completeness Flags: [ Null ]]
    [TCP Segment Len: 142]
    Sequence Number: 1    (relative sequence number)
    Sequence Number (raw): 2508105969
    [Next Sequence Number: 143    (relative sequence number)]
    Acknowledgment Number: 1    (relative ack number)
    Acknowledgment number (raw): 2243821671
    0101 .... = Header Length: 20 bytes (5)
    Flags: 0x018 (PSH, ACK)
        000. .... .... = Reserved: Not set
        ...0 .... .... = Accurate ECN: Not set
        .... 0... .... = Congestion Window Reduced: Not set
        .... .0.. .... = ECN-Echo: Not set
        .... ..0. .... = Urgent: Not set
        .... ...1 .... = Acknowledgment: Set
        .... .... 1... = Push: Set
        .... .... .0.. = Reset: Not set
        .... .... ..0. = Syn: Not set
        .... .... ...0 = Fin: Not set
        [TCP Flags: ·······AP···]
    Window: 83
    [Calculated window size: 83]
    [Window size scaling factor: -1 (unknown)]
    Checksum: 0xaea0 [unverified]
    [Checksum Status: Unverified]
    Urgent Pointer: 0
    [Timestamps]
        [Time since first frame in this TCP stream: 0.000000000 seconds]
        [Time since previous frame in this TCP stream: 0.000000000 seconds]
    [SEQ/ACK analysis]
        [Bytes in flight: 142]
        [Bytes sent since last PSH flag: 142]
    TCP payload (142 bytes)
Data (142 bytes)

0000  10 16 00 1c 07 0c 5a d5 a4 f5 3c 23 6c b6 ea 70   ......Z...<#l..p
0010  a7 f1 34 5e d6 f7 b9 c1 ba bc 64 95 70 81 51 0a   ..4^......d.p.Q.
0020  bd 5d 05 8d 71 15 56 24 bf ae 46 e3 82 b0 e2 3a   .]..q.V$..F....:
0030  5f e5 24 dd cd c9 d5 96 10 20 24 1e 38 81 16 83   _.$...... $.8...
0040  d0 3c 63 19 a4 eb f2 74 79 95 74 35 47 b9 95 06   .<c....ty.t5G...
0050  fe 8a c0 a8 bb cc b8 8e 00 42 3e a2 18 1c b6 23   .........B>....#
0060  71 07 b0 fc 94 b4 ae 30 3e bc d7 62 bb 08 9e 06   q......0>..b....
0070  9a c9 89 78 1b 58 85 09 65 83 da 86 b8 e5 c5 99   ...x.X..e.......
0080  17 87 1d 63 af eb 41 72 2f 19 47 b0 b5 16         ...c..Ar/.G...
    Data […]: 1016001c070c5ad5a4f53c236cb6ea70a7f1345ed6f7b9c1babc64957081510abd5d058d71155624bfae46e382b0e23a5fe524ddcdc9d5961020241e38811683d03c6319a4ebf2747995743547b99506fe8ac0a8bbccb88e00423ea2181cb6237107b0fc94b4ae303ebcd762bb089e069ac
    [Length: 142]

Frame 2: 54 bytes on wire (432 bits), 54 bytes captured (432 bits) on interface \Device\NPF_{788C51AF-3B1E-48D0-B065-B13BF31D419A}, id 0
    Section number: 1
    Interface id: 0 (\Device\NPF_{788C51AF-3B1E-48D0-B065-B13BF31D419A})
        Interface name: \Device\NPF_{788C51AF-3B1E-48D0-B065-B13BF31D419A}
        Interface description: Беспроводная сеть
    Encapsulation type: Ethernet (1)
    Arrival Time: May 13, 2025 14:08:42.027078000 RTZ 2 (зима)
    UTC Arrival Time: May 13, 2025 11:08:42.027078000 UTC
    Epoch Arrival Time: 1747134522.027078000
    [Time shift for this packet: 0.000000000 seconds]
    [Time delta from previous captured frame: 0.044778000 seconds]
    [Time delta from previous displayed frame: 0.044778000 seconds]
    [Time since reference or first frame: 0.044778000 seconds]
    Frame Number: 2
    Frame Length: 54 bytes (432 bits)
    Capture Length: 54 bytes (432 bits)
    [Frame is marked: False]
    [Frame is ignored: False]
    [Protocols in frame: eth:ethertype:ip:tcp]
Ethernet II, Src: CloudNetwork_ed:85:59 (2c:9c:58:ed:85:59), Dst: TPLink_36:2b:c3 (5c:e9:31:36:2b:c3)
    Destination: TPLink_36:2b:c3 (5c:e9:31:36:2b:c3)
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
    Source: CloudNetwork_ed:85:59 (2c:9c:58:ed:85:59)
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
    Type: IPv4 (0x0800)
    [Stream index: 0]
Internet Protocol Version 4, Src: 192.168.0.101, Dst: 113.30.190.46
    0100 .... = Version: 4
    .... 0101 = Header Length: 20 bytes (5)
    Differentiated Services Field: 0x00 (DSCP: CS0, ECN: Not-ECT)
        0000 00.. = Differentiated Services Codepoint: Default (0)
        .... ..00 = Explicit Congestion Notification: Not ECN-Capable Transport (0)
    Total Length: 40
    Identification: 0xad7c (44412)
    010. .... = Flags: 0x2, Don't fragment
        0... .... = Reserved bit: Not set
        .1.. .... = Don't fragment: Set
        ..0. .... = More fragments: Not set
    ...0 0000 0000 0000 = Fragment Offset: 0
    Time to Live: 128
    Protocol: TCP (6)
    Header Checksum: 0x5cf9 [validation disabled]
    [Header checksum status: Unverified]
    Source Address: 192.168.0.101
    Destination Address: 113.30.190.46
    [Stream index: 0]
Transmission Control Protocol, Src Port: 58342, Dst Port: 20175, Seq: 1, Ack: 143, Len: 0
    Source Port: 58342
    Destination Port: 20175
    [Stream index: 0]
    [Stream Packet Number: 2]
    [Conversation completeness: Incomplete (8)]
        ..0. .... = RST: Absent
        ...0 .... = FIN: Absent
        .... 1... = Data: Present
        .... .0.. = ACK: Absent
        .... ..0. = SYN-ACK: Absent
        .... ...0 = SYN: Absent
        [Completeness Flags: ··D···]
    [TCP Segment Len: 0]
    Sequence Number: 1    (relative sequence number)
    Sequence Number (raw): 2243821671
    [Next Sequence Number: 1    (relative sequence number)]
    Acknowledgment Number: 143    (relative ack number)
    Acknowledgment number (raw): 2508106111
    0101 .... = Header Length: 20 bytes (5)
    Flags: 0x010 (ACK)
        000. .... .... = Reserved: Not set
        ...0 .... .... = Accurate ECN: Not set
        .... 0... .... = Congestion Window Reduced: Not set
        .... .0.. .... = ECN-Echo: Not set
        .... ..0. .... = Urgent: Not set
        .... ...1 .... = Acknowledgment: Set
        .... .... 0... = Push: Not set
        .... .... .0.. = Reset: Not set
        .... .... ..0. = Syn: Not set
        .... .... ...0 = Fin: Not set
        [TCP Flags: ·······A····]
    Window: 253
    [Calculated window size: 253]
    [Window size scaling factor: -1 (unknown)]
    Checksum: 0xc6a3 [unverified]
    [Checksum Status: Unverified]
    Urgent Pointer: 0
    [Timestamps]
        [Time since first frame in this TCP stream: 0.044778000 seconds]
        [Time since previous frame in this TCP stream: 0.044778000 seconds]
    [SEQ/ACK analysis]
        [This is an ACK to the segment in frame: 1]
        [The RTT to ACK the segment was: 0.044778000 seconds]

Frame 3: 54 bytes on wire (432 bits), 54 bytes captured (432 bits) on interface \Device\NPF_{788C51AF-3B1E-48D0-B065-B13BF31D419A}, id 0
    Section number: 1
    Interface id: 0 (\Device\NPF_{788C51AF-3B1E-48D0-B065-B13BF31D419A})
        Interface name: \Device\NPF_{788C51AF-3B1E-48D0-B065-B13BF31D419A}
        Interface description: Беспроводная сеть
    Encapsulation type: Ethernet (1)
    Arrival Time: May 13, 2025 14:08:42.261158000 RTZ 2 (зима)
    UTC Arrival Time: May 13, 2025 11:08:42.261158000 UTC
    Epoch Arrival Time: 1747134522.261158000
    [Time shift for this packet: 0.000000000 seconds]
    [Time delta from previous captured frame: 0.234080000 seconds]
    [Time delta from previous displayed frame: 0.234080000 seconds]
    [Time since reference or first frame: 0.278858000 seconds]
    Frame Number: 3
    Frame Length: 54 bytes (432 bits)
    Capture Length: 54 bytes (432 bits)
    [Frame is marked: False]
    [Frame is ignored: False]
    [Protocols in frame: eth:ethertype:ip:tcp]
Ethernet II, Src: TPLink_36:2b:c3 (5c:e9:31:36:2b:c3), Dst: CloudNetwork_ed:85:59 (2c:9c:58:ed:85:59)
    Destination: CloudNetwork_ed:85:59 (2c:9c:58:ed:85:59)
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
    Source: TPLink_36:2b:c3 (5c:e9:31:36:2b:c3)
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
    Type: IPv4 (0x0800)
    [Stream index: 0]
Internet Protocol Version 4, Src: 113.30.190.46, Dst: 192.168.0.101
    0100 .... = Version: 4
    .... 0101 = Header Length: 20 bytes (5)
    Differentiated Services Field: 0x00 (DSCP: CS0, ECN: Not-ECT)
        0000 00.. = Differentiated Services Codepoint: Default (0)
        .... ..00 = Explicit Congestion Notification: Not ECN-Capable Transport (0)
    Total Length: 40
    Identification: 0x7d4c (32076)
    010. .... = Flags: 0x2, Don't fragment
        0... .... = Reserved bit: Not set
        .1.. .... = Don't fragment: Set
        ..0. .... = More fragments: Not set
    ...0 0000 0000 0000 = Fragment Offset: 0
    Time to Live: 55
    Protocol: TCP (6)
    Header Checksum: 0xd629 [validation disabled]
    [Header checksum status: Unverified]
    Source Address: 113.30.190.46
    Destination Address: 192.168.0.101
    [Stream index: 0]
Transmission Control Protocol, Src Port: 20175, Dst Port: 63125, Seq: 1, Ack: 1, Len: 0
    Source Port: 20175
    Destination Port: 63125
    [Stream index: 1]
    [Stream Packet Number: 1]
    [Conversation completeness: Incomplete (0)]
        ..0. .... = RST: Absent
        ...0 .... = FIN: Absent
        .... 0... = Data: Absent
        .... .0.. = ACK: Absent
        .... ..0. = SYN-ACK: Absent
        .... ...0 = SYN: Absent
        [Completeness Flags: [ Null ]]
    [TCP Segment Len: 0]
    Sequence Number: 1    (relative sequence number)
    Sequence Number (raw): 48611788
    [Next Sequence Number: 1    (relative sequence number)]
    Acknowledgment Number: 1    (relative ack number)
    Acknowledgment number (raw): 3973970233
    0101 .... = Header Length: 20 bytes (5)
    Flags: 0x010 (ACK)
        000. .... .... = Reserved: Not set
        ...0 .... .... = Accurate ECN: Not set
        .... 0... .... = Congestion Window Reduced: Not set
        .... .0.. .... = ECN-Echo: Not set
        .... ..0. .... = Urgent: Not set
        .... ...1 .... = Acknowledgment: Set
        .... .... 0... = Push: Not set
        .... .... .0.. = Reset: Not set
        .... .... ..0. = Syn: Not set
        .... .... ...0 = Fin: Not set
        [TCP Flags: ·······A····]
    Window: 83
    [Calculated window size: 83]
    [Window size scaling factor: -1 (unknown)]
    Checksum: 0xcef8 [unverified]
    [Checksum Status: Unverified]
    Urgent Pointer: 0
    [Timestamps]
        [Time since first frame in this TCP stream: 0.000000000 seconds]
        [Time since previous frame in this TCP stream: 0.000000000 seconds]

Frame 4: 54 bytes on wire (432 bits), 54 bytes captured (432 bits) on interface \Device\NPF_{788C51AF-3B1E-48D0-B065-B13BF31D419A}, id 0
    Section number: 1
    Interface id: 0 (\Device\NPF_{788C51AF-3B1E-48D0-B065-B13BF31D419A})
        Interface name: \Device\NPF_{788C51AF-3B1E-48D0-B065-B13BF31D419A}
        Interface description: Беспроводная сеть
    Encapsulation type: Ethernet (1)
    Arrival Time: May 13, 2025 14:08:42.261250000 RTZ 2 (зима)
    UTC Arrival Time: May 13, 2025 11:08:42.261250000 UTC
    Epoch Arrival Time: 1747134522.261250000
    [Time shift for this packet: 0.000000000 seconds]
    [Time delta from previous captured frame: 0.000092000 seconds]
    [Time delta from previous displayed frame: 0.000092000 seconds]
    [Time since reference or first frame: 0.278950000 seconds]
    Frame Number: 4
    Frame Length: 54 bytes (432 bits)
    Capture Length: 54 bytes (432 bits)
    [Frame is marked: False]
    [Frame is ignored: False]
    [Protocols in frame: eth:ethertype:ip:tcp]
Ethernet II, Src: CloudNetwork_ed:85:59 (2c:9c:58:ed:85:59), Dst: TPLink_36:2b:c3 (5c:e9:31:36:2b:c3)
    Destination: TPLink_36:2b:c3 (5c:e9:31:36:2b:c3)
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
    Source: CloudNetwork_ed:85:59 (2c:9c:58:ed:85:59)
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
    Type: IPv4 (0x0800)
    [Stream index: 0]
Internet Protocol Version 4, Src: 192.168.0.101, Dst: 113.30.190.46
    0100 .... = Version: 4
    .... 0101 = Header Length: 20 bytes (5)
    Differentiated Services Field: 0x00 (DSCP: CS0, ECN: Not-ECT)
        0000 00.. = Differentiated Services Codepoint: Default (0)
        .... ..00 = Explicit Congestion Notification: Not ECN-Capable Transport (0)
    Total Length: 40
    Identification: 0xad7d (44413)
    010. .... = Flags: 0x2, Don't fragment
        0... .... = Reserved bit: Not set
        .1.. .... = Don't fragment: Set
        ..0. .... = More fragments: Not set
    ...0 0000 0000 0000 = Fragment Offset: 0
    Time to Live: 128
    Protocol: TCP (6)
    Header Checksum: 0x5cf8 [validation disabled]
    [Header checksum status: Unverified]
    Source Address: 192.168.0.101
    Destination Address: 113.30.190.46
    [Stream index: 0]
Transmission Control Protocol, Src Port: 63125, Dst Port: 20175, Seq: 1, Ack: 2, Len: 0
    Source Port: 63125
    Destination Port: 20175
    [Stream index: 1]
    [Stream Packet Number: 2]
    [Conversation completeness: Incomplete (4)]
        ..0. .... = RST: Absent
        ...0 .... = FIN: Absent
        .... 0... = Data: Absent
        .... .1.. = ACK: Present
        .... ..0. = SYN-ACK: Absent
        .... ...0 = SYN: Absent
        [Completeness Flags: ···A··]
    [TCP Segment Len: 0]
    Sequence Number: 1    (relative sequence number)
    Sequence Number (raw): 3973970233
    [Next Sequence Number: 1    (relative sequence number)]
    Acknowledgment Number: 2    (relative ack number)
    Acknowledgment number (raw): 48611789
    0101 .... = Header Length: 20 bytes (5)
    Flags: 0x010 (ACK)
        000. .... .... = Reserved: Not set
        ...0 .... .... = Accurate ECN: Not set
        .... 0... .... = Congestion Window Reduced: Not set
        .... .0.. .... = ECN-Echo: Not set
        .... ..0. .... = Urgent: Not set
        .... ...1 .... = Acknowledgment: Set
        .... .... 0... = Push: Not set
        .... .... .0.. = Reset: Not set
        .... .... ..0. = Syn: Not set
        .... .... ...0 = Fin: Not set
        [TCP Flags: ·······A····]
    Window: 255
    [Calculated window size: 255]
    [Window size scaling factor: -1 (unknown)]
    Checksum: 0xce4b [unverified]
    [Checksum Status: Unverified]
    Urgent Pointer: 0
    [Timestamps]
        [Time since first frame in this TCP stream: 0.000092000 seconds]
        [Time since previous frame in this TCP stream: 0.000092000 seconds]
    [SEQ/ACK analysis]
        [TCP Analysis Flags]
            [Expert Info (Warning/Sequence): ACKed segment that wasn't captured (common at capture start)]
                [ACKed segment that wasn't captured (common at capture start)]
                [Severity level: Warning]
                [Group: Sequence]

4 packets captured

C:\Users\NikitaShuyiv\Desktop\ITNO\2_семестр\сети и протоколы\ChuevN_Networks\Practic№2>

##Краткий вывод

Зафиксировано два TCP-пакета, передававшихся в течение очень короткого времени. Первый пакет содержит данные (142 байта), идет от IP 113.30.190.46 к 192.168.0.101 и использует исходный порт 20175. Второй — ответный пакет, размером 54 байта, идет от IP 192.168.0.101 к тому же IP-адресу, с исходным портом 58342 и целевым 20175, подтверждая активное TCP-соединение.

Выполним  с помощью python , для этого был реализован скрипт в файле  tcp_details.py

Вывод:

Microsoft Windows [Version 10.0.26100.3775]
(c) Корпорация Майкрософт (Microsoft Corporation). Все права защищены.

C:\Users\NikitaShuyiv\Desktop\ITNO\2_семестр\сети и протоколы\pr2>python tcp_details.py
=== 🧩 Анализ TCP-пакетов ===

Пакет #1
IP-адрес отправителя     : 192.168.0.101
IP-адрес получателя      : 192.168.0.110
Порт отправителя         : 61579
Порт получателя          : 7680
Флаги TCP                : S
Номер последовательности : 3058236283
Номер подтверждения      : 0
Размер TCP-пакета        : 32 байт
--------------------------------------------------
Пакет #2
IP-адрес отправителя     : 192.168.0.110
IP-адрес получателя      : 192.168.0.101
Порт отправителя         : 7680
Порт получателя          : 61579
Флаги TCP                : SA
Номер последовательности : 1648387817
Номер подтверждения      : 3058236284
Размер TCP-пакета        : 32 байт
--------------------------------------------------
Пакет #3
IP-адрес отправителя     : 192.168.0.101
IP-адрес получателя      : 192.168.0.110
Порт отправителя         : 61579
Порт получателя          : 7680
Флаги TCP                : A
Номер последовательности : 3058236284
Номер подтверждения      : 1648387818
Размер TCP-пакета        : 20 байт
--------------------------------------------------
Пакет #4
IP-адрес отправителя     : 192.168.0.101
IP-адрес получателя      : 192.168.0.110
Порт отправителя         : 61579
Порт получателя          : 7680
Флаги TCP                : PA
Номер последовательности : 3058236284
Номер подтверждения      : 1648387818
Размер TCP-пакета        : 95 байт
--------------------------------------------------
Пакет #5
IP-адрес отправителя     : 192.168.0.110
IP-адрес получателя      : 192.168.0.101
Порт отправителя         : 7680
Порт получателя          : 61579
Флаги TCP                : PA
Номер последовательности : 1648387818
Номер подтверждения      : 3058236359
Размер TCP-пакета        : 95 байт
--------------------------------------------------

C:\Users\NikitaShuyiv\Desktop\ITNO\2_семестр\сети и протоколы\pr2>

###Выводы по работе:

В ходе работы я провел анализ сетевых пакетов и выяснил, какие протоколы используются в сети. Затем выбрал протокол TCP для более детального изучения. С помощью специальных инструментов я собрал информацию о TCP-пакетах, посмотрел, какие данные они содержат, и разобрал основные поля внутри пакета, например адреса, порты и управляющие флаги. Это помогло понять, как происходит установление соединения и передача данных в сети. 