import threading
import time
import queue

class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False

class Cafe: # Класс Cafe- класс для симуляции процессов в кафе/содержит атрибуты:
    def __init__(self, tables):
        self.tables = tables # tables (список столов)/ Атрибут tables список столов (поступает из вне)
        self.queue = queue.Queue() # queue (очередь посетителей) Атрибут queue - очередь посетителей (создаётся внутри init)

    def customer_arrival(self):
        customer_number = 1
        while customer_number <= 20:  # Limit the number of customers to 20 for demonstration
            print(f"Посетитель номер {customer_number} прибыл")
            customer = Customer(customer_number, self)
            customer_number += 1
            customer.start()
            time.sleep(1)

    def serve_customer(self, customer):
        for table in self.tables:
            if not table.is_busy:
                table.is_busy = True
                print(f"Посетитель номер {customer.customer_number} сел за стол {table.number} (начало обслуживания)")
                time.sleep(5)  # Time to serve the customer
                print(f"Посетитель номер {customer.customer_number} покушал и ушёл (конец обслуживания)")
                table.is_busy = False
                self.check_queue()
                break
        else:
            self.queue.put(customer)
            print(f"Посетитель номер {customer.customer_number} ожидает свободный стол (помещение в очередь)")

    def check_queue(self):
        if not self.queue.empty():
            customer = self.queue.get()
            self.serve_customer(customer)

class Customer(threading.Thread): # Класс Customer наследуется от threading.Thread/ класс (поток) посетителя.
#                                   Запускается, если есть свободные столы.и содержит атрибуты:
    def __init__(self, customer_number, cafe):
        super().__init__()
        self.customer_number = customer_number # customer_number (номер посетителя)
        self.cafe = cafe

    def run(self):  # Метод run запускается при запуске потока и моделирует приход посетителя,
#                                     # прием пищи и уход.
        self.cafe.serve_customer(self)

# Создаем столики в кафе
table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

# Инициализируем кафе
cafe = Cafe(tables)

# Запускаем поток для прибытия посетителей
customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

# Ожидаем завершения работы прибытия посетителей
customer_arrival_thread.join()
