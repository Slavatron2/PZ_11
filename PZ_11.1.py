#Из предложенного текстового файла (text18-21.txt) вывести на экран его содержимое,
#количество знаков препинания. Сформировать новый файл, в который поместить текст в
#стихотворной форме.


content2 ="Текст (от лат. textus — ткань; сплетение, сочетание,) — зафиксированная, на каком-либо материальном носителе"
"Существуют две основные трактовки понятия «текст»: имманентная. (расширенная, философски нагруженная) и репрезентати."

content = "Виктор Кайханиди, ИС-27, жёсткий парень, учился хорошо, ищет второго Виктора."

with open('filename.txt', "w") as file1:
    file1.write(content)

print(f"Файл '{file1}' успешно создан и содержит текст.")


filename = "text18-21.txt"

with open('filename.txt', "r") as file2:
    content1 = file2.read().split()
    punctuation_count = sum([1 for char in content if char in ['.', ',', ';', '!', '?']])

with open("aboba.txt", "r") as file:
    lines = file.readlines()
    reversed_lines = lines[::-1]


with open("aboba.txt", "w") as file:
    file.writelines(reversed_lines)





print(f"Содержимое первого файла: {content}")

print(f'количество символов: {punctuation_count}')

print(f"Содержимое второго файла: {content2}")
