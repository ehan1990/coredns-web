
class Zone:

    def __init__(self, zone_name, owner):
        self.zone_name = zone_name
        self.owner = owner


class Record:

    def __init__(self, record_name, zone_name, record_type, record_value, owner, ttl=60):
        self.record_name = record_name
        self.zone_name = zone_name
        self.record_type = record_type
        self.record_value = record_value
        self.ttl = ttl
        self.owner = owner
