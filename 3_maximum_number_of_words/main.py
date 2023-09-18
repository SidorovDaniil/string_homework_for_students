"""
Вам дан список предложений.
Предложения содержат только слова, которые разделены единичными пробелами.
Необходимо вернуть максимальное количество слов, которое содержится в одном предложении.
sentences[i] - это одно предложение.
Если ни одно из предложений не содержит слов, то нужно вернуть 0
Проверка:
pytest ./3_maximum_number_of_words/test.py
"""


def get_max_number_of_words_from_sentences(sentences: list[str]) -> int:
    answer = 0
    for sentence in sentences:
        words = sentence.split(" ")
        if (len(words) >= answer) & ("" not in words):
            answer = len(words)

    return answer
