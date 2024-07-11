import time
from threading import Thread
from datetime import datetime

def wite_words(word_count, file_name):
    with open(file_name, "w", encoding="utf-8") as file:
        for i in range(1, word_count+1):
            file.write(f" Какое-то слово № {i}\n")
            time.sleep(0.1)
        print('Завершилась запись в файл: ' + file_name)

start_time = datetime.now()

wite_words(10, "example1.txt")
wite_words(30, "example2.txt")
wite_words(200, "example3.txt")
wite_words(100, "example4.txt")

end_time = datetime.now()
res_time = end_time - start_time
print('Время записи файлов без помощи потоков: '+str(res_time))

start_time2 = datetime.now()

thr_first = Thread(target=wite_words, args=(10, "example5.txt"))
thr_second = Thread(target=wite_words, args=(30, "example6.txt"))
thr_third = Thread(target=wite_words, args=(200, "example7.txt"))
trh_fourth = Thread(target=wite_words, args=(100, "example8.txt"))

thr_first.start()
thr_second.start()
thr_third.start()
trh_fourth.start()

thr_first.join()
thr_second.join()
thr_third.join()
trh_fourth.join()

end_time2 = datetime.now()
res_time2 = end_time2 - start_time2
print('Время записи файлов с помощью потоков: '+str(res_time2))