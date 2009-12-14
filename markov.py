
from collections import defaultdict
from random import choice

class Markov(object):
    def __init__(self, length=3):
        self._length = length
        self._db = defaultdict(lambda: [])
        self._starters = []

    def pick_next_word(self, pre):
        next = []
        next = self._db[tuple(pre)]
        while next == []:
            next = choice(self._db.values())
        return choice(next)

    def add_text(self, text):
        split_text = text.split()
        ch = split_text[:self._length]
        for word in split_text[self._length:]:
            self._db[tuple(ch)].append(word)
            if ch[0][0].isupper():
                self._starters.append(list(ch))
            ch.pop(0)
            ch.append(word)

    def build_chain(self, length):
        chain = choice(self._starters)
        for i in xrange(0, length):
            chain.append(self.pick_next_word(chain[-self._length:]))
        return ' '.join(chain)

    def read_file(self, filename):
        f = file(filename)
        self.add_text(f.read())

