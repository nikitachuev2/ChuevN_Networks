class Port:
    def __init__(self, port_id, cost, connected_bridge=None, priority=128):
        self.port_id = port_id  # Уникальный ID порта (int)
        self.cost = cost  # Стоимость канала
        self.priority = priority  # Приоритет порта
        self.connected_bridge = connected_bridge  # К какому мосту он подключен

        self.state = "BLOCKING"  # По умолчанию BLOCKING
        self.role = None  # RP, DP, ALT и т.д.

    @property
    def pid(self):
        # PID = (Port Priority << 12) | Port Number
        return (self.priority << 12) | self.port_id

    def __str__(self):
        return f"Port-{self.port_id}(Cost={self.cost}, PID={self.pid}, State={self.state}, Role={self.role})"
 
