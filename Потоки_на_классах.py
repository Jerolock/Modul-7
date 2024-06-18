import time
from threading import Thread

class Voin(Thread):

    def __init__(self, name, sila, vragi):
        super(Voin, self).__init__()
        self.name = name
        self.sila = sila
        self.vragi = vragi

    def run(self):
        if self.vragi > 0:
            print(f'{self.name}, на нас напали! ')
            print(f'К бою, {self.name}')
            vremya = 0
            for i in range(self.vragi-self.sila, -self.sila, -self.sila):
                vremya += 1
                print(f'{self.name} сражается {vremya} (дня) дней, осталось {i} врагов! ')
                time.sleep(1)
            print(f'Битва закончена! {self.name} победил за {vremya} дней! ')

voin_1 = Voin(name='Сэр Ланселот', sila=20, vragi=100)
voin_2 = Voin(name='Сэр Галахад', sila=10, vragi=100)

voin_1.start()
voin_2.start()
voin_1.join()
voin_2.join()
print('Война окончена! Наши победили!')