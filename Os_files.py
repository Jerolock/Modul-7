import os
import time

directory = 'D:\python\HomeWork\Modul2'

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)
        filetime = os.path.getatime(filepath)
        formatted_time = time.strftime('%d.%m.%Y %H:%M', time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        print(f'обнаружен файл: {file}, путь: {filepath}, размер: {filesize} байт, время изменения: {formatted_time}')
