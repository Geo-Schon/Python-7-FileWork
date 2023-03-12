# Документ «article.txt» содержит следующий текст:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела
#
# Требуется реализовать функцию longest_words(file), которая записывает в файл result.txt слово, имеющее максимальную
# длину (или список слов, если таковых несколько).

def longest_words(file):
    with open(file, encoding='utf-8') as text:
        words = text.read().split()
        max_length = len(max(words, key=len))
        search_words = [word for word in words if len(word) == max_length]
        return search_words

print(*longest_words('article.txt'))
