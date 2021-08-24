class Attribute:
    def __init__(self, k, v):
        self.key = k
        self.value = v

    def __repr__(self):
        return self.key + ": " + self.value