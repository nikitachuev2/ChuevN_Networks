class Port:
    def __init__(self, port_id, cost=4):
        self.port_id = port_id
        self.cost = cost
        self.connected_to = None  # Другой порт
        self.role = "Unknown"

    def __repr__(self):
        return f"Port {self.port_id} (Cost={self.cost}, Role={self.role})"


class Bridge:
    def __init__(self, bridge_id, priority=32768):
        self.bridge_id = bridge_id
        self.priority = priority
        self.mac = bridge_id
        self.ports = []
        self.root_id = self.get_bid()
        self.root_port = None
        self.path_cost = 0

    def get_bid(self):
        return (self.priority << 48) + self.mac

    def add_port(self, port: Port):
        self.ports.append(port)

    def print_ports(self):
        print(f"\nBridge {self.bridge_id}")
        print(f"  BID: {self.get_bid()}")
        print(f"  Root ID: {self.root_id}")
        print(f"  Path Cost: {self.path_cost}")
        if self.root_port:
            print(f"  Root Port: Port {self.root_port.port_id}")
        for port in self.ports:
            print(f"  {port}")
 
