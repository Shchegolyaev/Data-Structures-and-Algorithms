
### Поиск в сломанном массиве


Алла ошиблась при копировании из одной структуры данных в другую. Она хранила массив чисел в кольцевом буфере. Массив был отсортирован по возрастанию, и в нём можно было найти элемент за логарифмическое время. Алла скопировала данные из кольцевого буфера в обычный массив, но сдвинула данные исходной отсортированной последовательности. Теперь массив не является отсортированным. Тем не менее, нужно обеспечить возможность находить в нем элемент за O(logn).
Можно предполагать, что в массиве только уникальные элементы.

#### Формат ввода
Функция принимает массив натуральных чисел и искомое число k. Длина массива не превосходит 10 000. Элементы массива и число k не превосходят по значению 10 000.
В примерах:
В первой строке записано число 
n –— длина массива.
Во второй строке записано положительное число 
k –— искомый элемент. 
Далее в строку через пробел записано n натуральных чисел, каждое из которых не превосходит 200 000.

#### Формат вывода
Для отсортированного списка участников выведите по порядку их логины по одному в строке.