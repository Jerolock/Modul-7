class EvenNumber:
    def __init__(self, s, e):
        self.s = s
        self.e = e
        self.i = 20

    def __iter__(self):
        return self

    def __next__(self):
        print('Чётные числа в диапазане', self.s, self.e)
        for o in range(self.s, self.e):
            if o % 2 == 0:
                print(o)
        raise StopIteration


en = EvenNumber(10, 25)
for i in en:
    print(i)
