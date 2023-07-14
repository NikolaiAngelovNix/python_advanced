class vowels:
    def __init__(self, text):
        self.text = text
        self.all_vowels = ["a", "i", "e", "u", "o", "y"]
        self.current_index = - 1
        self.end_index = len(self.text) - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.current_index += 1
        if self.current_index > self.end_index:
            raise StopIteration
        if self.text[self.current_index].lower() in self.all_vowels:
            return self.text[self.current_index]
        return self.__next__()
    