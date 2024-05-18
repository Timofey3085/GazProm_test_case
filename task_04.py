"""
№4
Имеется папка с файлами
Реализовать удаление файлов старше N дней
"""
import os
import shutil
import time

folder = "files"
N = 7  # число дней для удаления

os.chdir(os.path.join(os.getcwd(), folder))

list_of_files = os.listdir()

current_time = time.time()
day = 86400  # количество секунд за день

for i in list_of_files:
    file_location = os.path.join(os.getcwd(), i)
    file_time = os.stat(file_location).st_mtime

    if file_time < current_time - day * N:
        print(f"Delete: {i}")
        if os.path.isfile(file_location):
            os.remove(file_location)
        elif os.path.isdir(file_location):
            shutil.rmtree(file_location)
