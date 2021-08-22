from models import Attribute, DatatypeStore

class RedisStore:
    def __init__(self):
        self.data = {}
        self.datatypeStore = DatatypeStore()

    def set(self, k, values):
        attributes = self.create_attributes(values)
        self.data[k] = attributes

    def get(self, k):
        if k in self.data:
            return ", ".join([str(attr) for attr in  self.data[k]])
        return "No entry found for " + k

    def delete(self, k):
        del(self.data[k])

    def search(self, searchDict):
        presentInKeys = list()
        for k in self.data:
            for attr in self.data[k]:
                if attr.key in searchDict and  attr.value == searchDict[attr.key]:
                    presentInKeys.append(k)
                    break
        return ",".join(presentInKeys)

    def keys(self):
        return ",".join(list(self.data.keys()))

    def create_attributes(self, values):
        allAtrs = []
        for i in range(0, len(values), 2):
            allAtrs.append(Attribute(values[i], values[i + 1]))
            self.datatypeStore.addToStore(values[i], values[i + 1])
        return allAtrs