import random
import string
#uzywam biblioteki nltk
from nltk.corpus import words
import nltk


# Pobranie angielskich słów z NLTK
nltk.download('words')
english_words = words.words()

# Generowanie 100 losowych słów angielskich
def generate_english_words(n):
    return random.sample(english_words, n)

generated_words = generate_english_words(100)
print("Wygenerowane słowa:", generated_words)

wygenerowane_slowa = generated_words
#['tondino', 'skaitbird', 'perish', 'relentlessly', 'trullo', 'bucentaur', 'netleaf', 'tannaic', 'revealable', 'elixir', 'exfodiate', 'cuffy', 'lipper', 'unrehearsing', 'urnful', 'skaff', 'parentheticality', 'Serrifera', 'Digynia', 'plottingly', 'Southronie', 'venipuncture', 'baked', 'membranology', 'scantling', 'giddyhead', 'upliftingness', 'leucocytometer', 'triplewise', 'aftergrass', 'poimenic', 'bluehearts', 'redberry', 'Ayyubid', 'pelelith', 'ligule', 'kola', 'soral', 'taximetered', 'Leo', 'devadasi', 'Teredinidae', 'dambrod', 'endamoebic', 'Grenelle', 'unerroneous', 'incurvation', 'incrossbred', 'wavement', 'diiamb', 'muscleless', 'flashiness', 'hypaethros', 'hierogrammateus', 'banksman', 'diversiflorate', 'ointment', 'nonequilateral', 'hypophyllium', 'superabsurd', 'centonism', 'athlete', 'uterovesical', 'zati', 'nonreversion', 'negotiate', 'zee', 'Clare', 'perocephalus', 'characteristic', 'relicmonger', 'pug', 'repitch', 'stuckling', 'demolitionist', 'reflourishment', 'emballonurid', 'overbitterness', 'petrolage', 'taurophile', 'unadverse', 'liberationist', 'staphylotoxin', 'lifeline', 'doorba', 'bentiness', 'Desmodus', 'bottlenest', 'paleophytic', 'antiprelate', 'sorcering', 'emptysis', 'fume', 'inunctum', 'fieldwort', 'patristics', 'impolitically', 'endothelium', 'underrooted', 'Sbaikian']

# Wyszukiwanie w tablicy
def search_array(words, prefix):
    steps = 0  # licznik kroków
    results = []
    for word in words:
        steps += 1  # krok dla każdego słowa
        if word.startswith(prefix):
            results.append(word)
    return results, steps

array = wygenerowane_slowa
prefix =  "re"
print("\n")
print("Tablica: (slowa, kroki)\n", search_array(array, prefix))
print("\n")

#złożoność czasowa: O(n*m), gdzie n to liczba słów, a m to długość prefiksu 
#złożoność pamięciowa: O(n), gdzie n to liczba słów


#TRIE
# Klasa węzła Trie
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

# Klasa drzewa Trie
class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Dodawanie słowa do drzewa
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    # Wyszukiwanie słów zaczynających się na prefiks
    def search_with_prefix(self, prefix):
        steps = 0  
        node = self.root
        results = []

        # Znajdowanie węzła końcowego prefiksu
        for char in prefix:
            steps += 1  
            if char not in node.children:
                return results, steps
            node = node.children[char]

        # Znajdowanie wszystkich słów zaczynających się od prefiksu
        def dfs(current_node, current_prefix):
            nonlocal steps
            steps += 1  
            if current_node.is_end_of_word:
                results.append(current_prefix)
            for char, child_node in current_node.children.items():
                dfs(child_node, current_prefix + char)

        dfs(node, prefix)
        return results, steps


words = wygenerowane_slowa
prefix = "re"
trie = Trie()
for word in words:
    trie.insert(word)

print("Trie: (slowa, kroki) \n", trie.search_with_prefix(prefix))
#Złożoność czasowa: O(m+k), gdzie m to długość prefiksu, a k to liczba znalezionych słów
#Złożoność pamięciowa: O(n*l), gdzie n to liczba słów, a l to ich średnia długość