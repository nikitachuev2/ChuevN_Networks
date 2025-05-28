
import heapq

class Router:
    def __init__(self, name):
        self.name = name
        self.interfaces = {}  # {Router: (cost, preference)}
        self.routing_table = {}  # {destination_name: (next_hop_name, total_cost, total_preference)}

    def connect(self, neighbor, cost, preference):
        self.interfaces[neighbor] = (cost, preference)

    def update_routing_table(self, network):
        distances = {router: (float('inf'), float('inf')) for router in network}
        previous = {}
        distances[self] = (0, 0)

        heap = [(0, 0, self)]  # (preference, cost, router)

        while heap:
            pref_so_far, cost_so_far, current = heapq.heappop(heap)

            for neighbor, (cost, pref) in current.interfaces.items():
                new_pref = pref_so_far + pref
                new_cost = cost_so_far + cost

                if (new_pref, new_cost) < distances[neighbor]:
                    distances[neighbor] = (new_pref, new_cost)
                    previous[neighbor] = current
                    heapq.heappush(heap, (new_pref, new_cost, neighbor))

        self.routing_table = {}
        for router in network:
            if router == self or router not in previous:
                continue
            next_hop = router
            while previous[next_hop] != self:
                next_hop = previous[next_hop]
            self.routing_table[router.name] = (
                next_hop.name,
                distances[router][1],
                distances[router][0]
            )

    def print_routing_table(self):
        print(f"\nТаблица маршрутизации для {self.name}:")
        print(f"{'Назначение':<12}{'След. хоп':<10}{'Стоимость':<10}{'Предпочт.':<10}")
        for dest, (next_hop, cost, pref) in sorted(self.routing_table.items()):
            print(f"{dest:<12}{next_hop:<10}{cost:<10}{pref:<10}")

    def send_packet(self, destination_name, network):
        visited = set()
        path = []
        total_cost = 0
        total_pref = 0
        current = self

        print(f"\nОтправка пакета от {self.name} до {destination_name}")

        while current.name != destination_name:
            visited.add(current.name)
            path.append(current.name)
            route = current.routing_table.get(destination_name)

            if not route:
                print(f"[{current.name}] ❌ Нет маршрута до {destination_name}")
                return

            next_hop_name, cost, pref = route
            total_cost += cost
            total_pref += pref

            print(f"[{current.name}] -> {next_hop_name} (cost: {cost}, pref: {pref})")

            for neighbor in current.interfaces:
                if neighbor.name == next_hop_name:
                    current = neighbor
                    break
            else:
                print(f"[{current.name}] ❌ Следующий хоп {next_hop_name} не найден")
                return

        path.append(destination_name)
        print(f"[{current.name}] Пакет доставлен.")
        print(f"Путь: {' -> '.join(path)}")
        print(f"Суммарная стоимость: {total_cost}, Суммарное предпочтение: {total_pref}")

        # Анализ альтернатив
        print("\nАнализ альтернативных маршрутов:")
        print(f"{'Отправитель':<12}{'След. хоп':<12}{'Предпочт.':<12}{'Стоимость':<10}")
        for router in network:
            if destination_name in router.routing_table:
                hop, cost, pref = router.routing_table[destination_name]
                print(f"{router.name:<12}{hop:<12}{pref:<12}{cost:<10}")

# Создание сети
r1 = Router("R1")
r2 = Router("R2")
r3 = Router("R3")
r4 = Router("R4")
r5 = Router("R5")
r6 = Router("R6")

# Подключения
r1.connect(r2, cost=1, preference=10)
r2.connect(r1, cost=1, preference=10)

r2.connect(r3, cost=2, preference=5)
r3.connect(r2, cost=2, preference=5)

r3.connect(r6, cost=1, preference=10)
r6.connect(r3, cost=1, preference=10)

r1.connect(r4, cost=5, preference=5)
r4.connect(r1, cost=5, preference=5)

r4.connect(r5, cost=1, preference=2)  # Изначально низкое предпочтение
r5.connect(r4, cost=1, preference=2)

r5.connect(r6, cost=2, preference=3)
r6.connect(r5, cost=2, preference=3)

network = [r1, r2, r3, r4, r5, r6]

# Обновление маршрутов
for r in network:
    r.update_routing_table(network)

print("=== Таблицы маршрутизации до изменений ===")
for r in network:
    r.print_routing_table()

print("\n=== Первая отправка пакета от R1 к R6 ===")
r1.send_packet("R6", network)

# 🔥 Изменение преференса на R4–R5 до 50
print("\n=== Изменение метрик (преференс на R4–R5 = 50) ===")
r4.interfaces[r5] = (1, 50)
r5.interfaces[r4] = (1, 50)

# Повторный перерасчёт маршрутов
for r in network:
    r.update_routing_table(network)

print("\n=== Таблицы маршрутизации после изменений ===")
for r in network:
    r.print_routing_table()

print("\n=== Повторная отправка пакета от R1 к R6 ===")
r1.send_packet("R6", network)
 