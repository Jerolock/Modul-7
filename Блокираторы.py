import threading
from threading import Thread

class BankAccount:

    def __init__(self, schet, povtor, prihod, rashod):
        super(BankAccount, self).__init__()
        self.schet = schet
        self.povtor = povtor
        self.prihod = prihod
        self.rashod = rashod
        self.lock = threading.Lock()

    def popolnenie(self):
        for i in range(self.povtor):
            with self.lock:
                self.schet += self.prihod
                print(f'Пополнение {self.prihod} руб. Баланс Вашего счета: {self.schet} руб.')

    def spisanie(self):
        for j in range(self.povtor):
            with self.lock:
                self.schet -= self.rashod
                print(f'Списание {self.rashod} руб. Баланс Вашего счета: {self.schet} руб.')

accound_1 = BankAccount(1000, 5, 100, 150)
thread_1 = Thread(target=accound_1.popolnenie)
thread_2 = Thread(target=accound_1.spisanie)
thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()