# use of lambda functions to sort
from typing import List


def sort_words(words: List[str]) -> List[str]:
    pass

    words.sort(key=lambda word: len(word), reverse=True)

    return words


def sort_numbers(numbers: List[int]) -> List[int]:
    pass

    numbers.sort(key=lambda numbers: abs(numbers))

    return numbers
