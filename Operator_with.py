# class InOutmethod:
#   def __enter__(self):
# print('Начинаем чтение')
#   def __exit__(self, exc_type, exc_val, exc_tb):
# print('Закончили чтение')
file_name = 'byron.txt'
with open(file_name, mode='r') as file:
    for line in file:
        print(line)
print(file.closed)
