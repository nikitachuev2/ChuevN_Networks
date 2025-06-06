# Практическая работа № 7

**Выполнил:** Чуев Никита Сергеевич  
**Группа:** P4150  
**Преподаватель:** Васильев Дмитрий Евгеньевич  
**Дата выполнения задания:** 02.06.2025  
**Название дисциплины:** "Сети и протоколы"  

## Задание
Практическое задание:

Реализовать поведение алгоритма STP в Python (можете за основу брать уже разработанную модель при маршрутизации (только помним, что STP применяется на втором уровне)

### Решение: 

Practic№7/ main.py

## Вывод терминала

Microsoft Windows [Version 10.0.26100.4061]
(c) Корпорация Майкрософт (Microsoft Corporation). Все права защищены.

C:\Users\NikitaShuyiv\Desktop\ITNO\2_семестр\сети и протоколы\ChuevN_Networks\Practic№7>cmd
Microsoft Windows [Version 10.0.26100.4061]
(c) Корпорация Майкрософт (Microsoft Corporation). Все права защищены.

C:\Users\NikitaShuyiv\Desktop\ITNO\2_семестр\сети и протоколы\ChuevN_Networks\Practic№7>python main.py

=== STP: Расчёт дерева ===

=== ЭТАП 1: Выбор Root Bridge ===
Bridge 1 с BID 9223372036854775809
Bridge 2 с BID 9223372036854775810
Bridge 3 с BID 9223372036854775811
=> Root Bridge: Bridge 1 (BID=9223372036854775809)

=== ЭТАП 2: Выбор Root Port (RP) ===
Bridge 1 - Root Bridge, пропускаем выбор RP
Порт 3 соединен с Bridge 1:
  → Стоимость пути через этот порт: 0 (до соседа) + 4 (стоимость порта) = 4
  → Сравниваем BID соседа: 9223372036854775809
Порт 4 соединен с Bridge 3:
  → Стоимость пути через этот порт: inf (до соседа) + 4 (стоимость порта) = inf
  → Сравниваем BID соседа: 9223372036854775811
=> Выбран Root Port для Bridge 2: Port 3 с path cost 4
Порт 5 соединен с Bridge 1:
  → Стоимость пути через этот порт: 0 (до соседа) + 4 (стоимость порта) = 4
  → Сравниваем BID соседа: 9223372036854775809
Порт 6 соединен с Bridge 2:
  → Стоимость пути через этот порт: 4 (до соседа) + 4 (стоимость порта) = 8
  → Сравниваем BID соседа: 9223372036854775810
=> Выбран Root Port для Bridge 3: Port 5 с path cost 4

=== ЭТАП 3: Выбор Designated Ports (DP) ===

Сравнение каналов между Bridge 1 и Bridge 2:
  → Bridge 1: cost = 0 + 4 = 4
  → Bridge 2: cost = 4 + 4 = 8
=> Port 1 на Bridge 1 выбран как Designated Port

Сравнение каналов между Bridge 1 и Bridge 3:
  → Bridge 1: cost = 0 + 4 = 4
  → Bridge 3: cost = 4 + 4 = 8
=> Port 2 на Bridge 1 выбран как Designated Port

Сравнение каналов между Bridge 2 и Bridge 3:
  → Bridge 2: cost = 4 + 4 = 8
  → Bridge 3: cost = 4 + 4 = 8
=> Port 4 на Bridge 2 выбран как Designated Port

=== ЭТАП 4: Блокировка остальных портов ===
Bridge 3: Port 6 -> Blocked

=== Финальное состояние ===

Bridge 1
  BID: 9223372036854775809
  Root ID: 9223372036854775809
  Path Cost: 0
  Port 1 (Cost=4, Role=Designated Port)
  Port 2 (Cost=4, Role=Designated Port)

Bridge 2
  BID: 9223372036854775810
  Root ID: 9223372036854775809
  Path Cost: 4
  Root Port: Port 3
  Port 3 (Cost=4, Role=Root Port)
  Port 4 (Cost=4, Role=Designated Port)

Bridge 3
  BID: 9223372036854775811
  Root ID: 9223372036854775809
  Path Cost: 4
  Root Port: Port 5
  Port 5 (Cost=4, Role=Root Port)
  Port 6 (Cost=4, Role=Blocked)

C:\Users\NikitaShuyiv\Desktop\ITNO\2_семестр\сети и протоколы\ChuevN_Networks\Practic№7>


### Выводы по проделанной работе

В ходе выполнения практического задания была успешно реализована алгоритмика Spanning Tree Protocol (STP) на языке Python. Алгоритм корректно определяет корневой мост (Root Bridge) на основе минимального значения Bridge ID (BID). Реализован правильный выбор Root Ports для всех мостов, кроме корневого, с учетом стоимости портов и путей. Алгоритм также правильно назначает Designated Ports, основываясь на стоимости маршрутов между мостами. Дополнительно обеспечивается блокировка портов, не используемых в текущей топологии, что предотвращает возникновение петель в сети. Вывод данных в консоль организован, что позволяет отслеживать промежуточные результаты и финальное состояние сети.

Структура проекта включает несколько файлов, каждый из которых выполняет свою функцию. В файле main.py находится основной код, который запускает программу и выводит результаты работы STP. Файл stp.py содержит реализацию алгоритма, включая выбор корневого моста, Root Ports, Designated Ports и блокировку ненужных портов. В bridge.py описана структура класса для мостов с соответствующими атрибутами и методами. Файл port.py отвечает за описание классов для портов, включая атрибуты, такие как port_id и роль порта. Наконец, topology.py содержит функции для создания сети, создавая мосты и устанавливая между ними соединения.
