# Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
# последовательности из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:

# (1 ФАЙЛ)
# Содержимое первого файла:

# Отрицательные элементы:

# Количество отрицательных элементов:

# Среднее арифметическое:

# (2 ФАЙЛ)
# Содержимое второго файла:

# Положительные элементы:

# Количество положительных элементов:

# Сумма положительных элементов:

import random

a = random.sample(range(-100, 101), 50)
b = random.choices(range(1, 101), k=50)
def grisha(amogus):
    negative_numbers = [num for num in amogus if num < 0]
    positive_numbers = [num for num in amogus if num > 0]
    negative_otvet = len(negative_numbers)
    positive_otvet = len(positive_numbers)
    negative_avg = sum(negative_numbers) / negative_otvet if negative_otvet > 0 else 0
    positive_summa = sum(positive_numbers)
    return negative_numbers, negative_otvet, negative_avg, positive_numbers, positive_otvet, positive_summa

negative_numbers1, negative_otvet, negative_avg1, positive_numbers1, positive_count1, positive_sum1 = grisha(a)
negative_numbers2, negative_count2, negative_avg2, positive_numbers2, positive_count2, positive_summa2 = grisha(b)


with open("file1.txt", "w") as file:
    file.write("Отрицательные элементы:\n")
    file.write(" ".join(map(str, negative_numbers1)) + "\n")
    file.write("Количество отрицательных элементов: " + str(negative_otvet) + "\n")
    file.write("Среднее арифметическое: " + str(negative_avg1) + "\n")

with open("file2.txt", "w") as file:
    file.write("Положительные элементы:\n")
    file.write(" ".join(map(str, positive_numbers2)) + "\n")
    file.write("Количество положительных элементов: " + str(positive_count2) + "\n")
    file.write("Сумма положительных элементов: " + str(positive_summa2) + "\n")
