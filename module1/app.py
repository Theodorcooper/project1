import time
import os


str1 = """привет

"""

str2 = """
******Заметки лесника******
пока...
"""

str3 = """
******Заметки лесника******

Ну какой лесник, о чем вы
"""

str4 = """
******Заметки лесника******

         КОНЕЦ

****************************
"""

# очищаем окно терминала
os.system('cls')
# выводим сообщение
print(str1, end='\r')
# засыпаем на 1 секунду
time.sleep(1)

# повторяем операцию для остальных строк
os.system('clear')
print(str2, end='\r')
time.sleep(1)



