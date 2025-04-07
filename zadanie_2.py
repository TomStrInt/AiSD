import random
import string


def random_words(n, word_length=5):
    return [''.join(random.choices(string.ascii_lowercase, k=word_length)) for _ in range(n)]

def search_array(words, prefix):
    steps = 0  
    results = []
    for word in words:
        steps += 1
        if word.startswith(prefix):
            results.append(word)
    return results, steps


array = random_words(100)
prefix = "ab"
print("Tablica:", search_array(array, prefix))
for el in array:
    print(el)