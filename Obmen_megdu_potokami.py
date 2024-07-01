import threading
import time

import queue


class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False


class Customer(threading.Thread):
    def __init__(self, number, table):
        super().__init__()
        self.number = number
        self.table = table

    def run(self):
        print(f"Посетитель номер {self.number} сел за стол {self.table.number}.")
        time.sleep(5)
        print(f"Посетитель номер {self.number} покушал и ушёл.")


class Cafe:

    def __init__(self, tables):
        self.tables = tables
        self.queue = queue.Queue()
        self.customer_number = 1

    def customer_arrival(self):
        while self.customer_number <= 20:
            time.sleep(1)
            table = next((t for t in self.tables if not t.is_busy),
                         None)
            if table:
                table.is_busy = True
                customer = Customer(self.customer_number,
                                    table)
                customer.start()
                self.customer_number += 1
            else:
                print(f"Посетитель номер {self.customer_number} ожидает свободный стол.") 
                self.customer_number += 1



table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]


cafe = Cafe(tables)


customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()


customer_arrival_thread.join()
