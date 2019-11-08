"""
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
"""

import sys


def bad_count_th(word):
    word = list(word)
    count = 0

    def merge(left, right):
        nonlocal count
        merged = []
        while len(left) and len(right):
            if left[-1] == "t" and right[0] == "h":
                count += 1

            merged.insert(0, left.pop(-1))
            merged.append(right.pop(0))

        return merged + left + right

    def split_and_count(word):
        if len(word) <= 1:
            return word

        pivot = len(word) // 2
        left, right = word[:pivot], word[pivot:]

        left = split_and_count(left)
        right = split_and_count(right)

        return merge(left, right)

    split_and_count(word)
    return count


def old_count_th(word):
    count = 0

    def split_and_count(word):
        nonlocal count
        if len(word) <= 1:
            return
        if word == "th":
            count += 1
            return
        else:
            return
        if word[:2] == "th":
            count += 1
            split_and_count(word[2:])
        else:
            split_and_count(word[1:])

    split_and_count(word)
    return count


def count_th(word):
    count = 0
    if len(word) <= 1:
        return count
    if word[:2] == "th":
        count += count_th(word[2:]) + 1
    else:
        count += count_th(word[1:])
    return count


if __name__ == "__main__":
    if len(sys.argv) > 1:
        word = sys.argv[1]
        num = count_th(word)
        print(f"There are {num} instances of 'th' in the string {word}.")
    else:
        print("Usage: count_th.py [word]")
