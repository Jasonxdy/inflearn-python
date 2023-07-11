class iteration_test:
    def __init__(self, words) -> None:
        self._words = words.split()
    
    def __iter__(self):
        for word in self._words:
            yield word


words = "this is a sentence"
c = iteration_test(words)
print(hasattr(c, '__iter__'))

it = (word for word in words.split())

next(it)
next(it)
next(it)
next(it)
next(it)
next(it)
for word in it:
    print(word)