class uQueue:
    def __init__(self, name):
        self._queue = []
        self.name=name

    def appendlast(self, packet):
        self._queue.append(packet)

    def appendfirst(self, packet):
        self._queue.insert(0, packet)

    def poplast(self):
        return self._queue.pop()

    def popfirst(self):
        return self._queue.pop(0)

    def removedata(self, packet):
        try:
            self._queue.remove(packet)
        except ValueError:
            print("Queue removedata: No data in",name)

    def clear(self):
        self._queue.clear()

    def __len__(self):
        return len(self._queue)

    def __getitem__(self, i):
        return self._queue[i]
