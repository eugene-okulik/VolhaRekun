# Напишите программу, которая добавляет ‘ing’ в конец слов (к каждому слову) в тексте
# “Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at,
# dignissim vitae libero” и после этого выводит получившийся текст на экран.
# Знаки препинания не должны оказаться внутри слова. Если после слова идет запятая или точка, знак препинания должен
# идти после того же слова, но уже преобразованного.

text = '''Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl,
facilisis vitae semper at, dignissim vitae libero'''

words = text.replace("\n", " ").split()
words_updated = []

for word in words:
    if word[-1].lower() in "abcdefghijklmnopqrstuvwxyz":
        words_updated.append(f"{word}ing")
    else:
        words_updated.append(f"{word[:-1]}ing{word[-1]}")

text_ing = " ".join(words_updated)

print(words_updated)
print(text_ing)
