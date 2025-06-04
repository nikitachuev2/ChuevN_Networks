def run_stp(bridges):
    print("\n=== ЭТАП 1: Выбор Root Bridge ===")
    root_bridge = min(bridges, key=lambda b: b.get_bid())
    for b in bridges:
        print(f"Bridge {b.bridge_id} с BID {b.get_bid()}")
    print(f"=> Root Bridge: Bridge {root_bridge.bridge_id} (BID={root_bridge.get_bid()})")

    for b in bridges:
        b.root_id = root_bridge.get_bid()
        if b == root_bridge:
            b.path_cost = 0
            b.root_port = None
        else:
            b.path_cost = float('inf')

    print("\n=== ЭТАП 2: Выбор Root Port (RP) ===")
    for b in bridges:
        if b == root_bridge:
            print(f"Bridge {b.bridge_id} - Root Bridge, пропускаем выбор RP")
            continue

        best = None
        for port in b.ports:
            if not port.connected_to:
                continue

            neighbor = next(br for br in bridges if port.connected_to in br.ports)
            total_cost = port.cost + neighbor.path_cost

            print(f"Порт {port.port_id} соединен с Bridge {neighbor.bridge_id}:")
            print(f"  → Стоимость пути через этот порт: {neighbor.path_cost} (до соседа) + {port.cost} (стоимость порта) = {total_cost}")
            print(f"  → Сравниваем BID соседа: {neighbor.get_bid()}")

            if not best:
                best = (port, total_cost, neighbor.get_bid(), port.port_id)
                continue

            _, best_cost, best_bid, best_pid = best
            if (total_cost < best_cost or
                (total_cost == best_cost and neighbor.get_bid() < best_bid) or
                (total_cost == best_cost and neighbor.get_bid() == best_bid and port.port_id < best_pid)):
                best = (port, total_cost, neighbor.get_bid(), port.port_id)

        if best:
            port, cost, _, _ = best
            b.root_port = port
            b.path_cost = cost
            port.role = "Root Port"
            print(f"=> Выбран Root Port для Bridge {b.bridge_id}: Port {port.port_id} с path cost {cost}")

    print("\n=== ЭТАП 3: Выбор Designated Ports (DP) ===")
    all_links = set()

    for b in bridges:
        for p in b.ports:
            if p.connected_to:
                link = tuple(sorted([id(p), id(p.connected_to)]))
                if link in all_links:
                    continue
                all_links.add(link)

                b1 = b
                b2 = next(br for br in bridges if p.connected_to in br.ports)
                p1 = p
                p2 = p.connected_to

                cost1 = b1.path_cost + p1.cost
                cost2 = b2.path_cost + p2.cost

                print(f"\nСравнение каналов между Bridge {b1.bridge_id} и Bridge {b2.bridge_id}:")
                print(f"  → Bridge {b1.bridge_id}: cost = {b1.path_cost} + {p1.cost} = {cost1}")
                print(f"  → Bridge {b2.bridge_id}: cost = {b2.path_cost} + {p2.cost} = {cost2}")

                if (cost1 < cost2 or
                    (cost1 == cost2 and b1.get_bid() < b2.get_bid()) or
                    (cost1 == cost2 and b1.get_bid() == b2.get_bid() and p1.port_id < p2.port_id)):
                    p1.role = "Designated Port"
                    print(f"=> Port {p1.port_id} на Bridge {b1.bridge_id} выбран как Designated Port")
                else:
                    p2.role = "Designated Port"
                    print(f"=> Port {p2.port_id} на Bridge {b2.bridge_id} выбран как Designated Port")

    print("\n=== ЭТАП 4: Блокировка остальных портов ===")
    for b in bridges:
        for p in b.ports:
            if p.role not in ["Root Port", "Designated Port"]:
                p.role = "Blocked"
                print(f"Bridge {b.bridge_id}: Port {p.port_id} -> Blocked")
 
