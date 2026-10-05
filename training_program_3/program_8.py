from collections import OrderedDict

class DataBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = OrderedDict()

    def get(self, key):
        if key in self.data:
            value = self.data.pop(key)
            self.data[key] = value
            return value

        return None

    def put(self, key, value):
        if key in self.data:
            self.data.pop(key)

        self.data[key] = value

        if len(self.data) > self.capacity:
            self.data.popitem(last=False)


buf = DataBuffer(2)

buf.put("sensor1", 24.5)
buf.put("sensor2", 28.0)

buf.get("sensor1")

buf.put("sensor3", 31.2)

print(buf.get("sensor2"))
print(buf.get("sensor1"))
print(buf.get("sensor3"))