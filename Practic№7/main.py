from topology import create_bridges
from stp import run_stp

print("\n=== STP: Расчёт дерева ===")
bridges = create_bridges()
run_stp(bridges)

print("\n=== Финальное состояние ===")
for b in bridges:
    b.print_ports()
 
