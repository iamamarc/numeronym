from typing import List


def my_numeronym(word: str) -> str:
    if len(word) < 3:
        numeronym = word
    else:
        numeronym = f'{word[0]}{len(word) - 2}{word[-1]}'
    return numeronym


def extended_numeronym(words: List[str]) -> List[str]:
    numeronyms = []
    for word in words:
        numeronym = my_numeronym(word)
        count = 2
        while numeronym in numeronyms:
            upset = count + 1
            if len(word) - upset == 0:
                numeronym = word
            else:
                numeronym = f'{word[:count]}{len(word) - upset}{word[-1]}'
            count = count + 1
        numeronyms.append(numeronym)
    return numeronyms
