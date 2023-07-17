class sequence_repeat:
    def __init__(self, sequence, num):
        self.sequence = sequence
        self.num = num
        self.index = - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == self.num - 1:
            raise StopIteration

        self.index += 1
        return self.sequence[self.index % len(self.sequence)]
    