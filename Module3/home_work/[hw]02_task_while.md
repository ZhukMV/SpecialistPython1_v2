## "Потерянная карточка"

### Задание

Для настольной игры используются карточки с номерами от 1 до n. Одна карточка потерялась. \
Найдите ее, зная номера оставшихся карточек. 

Вводится число n - количество карточек, затем n−1 чисел: номера оставшихся карточек (различные числа от 1 до n). \
Программа должна вывести номер потерянной карточки.

### Формат входных данных

Дано целое число n - количество карточек \
И еще n-1 целых чисел: номера оставшихся карточек.

### Формат выходных данных

Выведите номер потерянной карточки.

### Решение задачи

```python
n = int(input("Количество карточек: "))
# Цикл, который выполнится n-1 раз
while ...:
    card_number = int(input("Номер карточки: "))
    ...

print("Номер потерянной карточки:", ...)
```