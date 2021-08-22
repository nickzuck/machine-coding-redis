class Attribute:
    def __init__(self, k, v):
        self.key = k
        self.value = v

    def __repr__(self):
        return self.key + ": " + self.value

class DatatypeStore:
    def __init__(self):
        self.availableAttrs = {}

    def find_primitive_type(self, value):
        if value.isdigit():
            return int
        if value.replace(".", "", 1).isdigit():
            return float
        return str

    def addToStore(self, attrKey, attrValue):
        if attrKey not in self.availableAttrs:
            self.availableAttrs[attrKey] = self.find_primitive_type(attrValue)
        elif self.find_primitive_type(attrValue) != self.availableAttrs[attrKey]:
            raise Exception("Invalid data type for attribute")