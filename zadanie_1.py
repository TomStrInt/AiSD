tablica_posortowana= [-78, 12, 34, 157, 223, 714, 890]

def znajdz_min_max(tab):
    licznik_krokow = 0  
    licznik_krokow += 1 
    min_element = tab[0]
    max_element = tab[-1]
    return min_element, max_element, licznik_krokow

print("posortowana tablica")
print("min, max, kroki") 
print(znajdz_min_max(tablica_posortowana))



tablica_nieposortowana= [411, -1221, 34, 25, 579, -2]
def znajdz_min_max_nieposort(arr):
    kroki = 0  
    min_element = float('inf')
    max_element = float('-inf')
    for num in arr:
        kroki += 1 
        if num < min_element:
            min_element = num
        if num > max_element:
            max_element = num
    return min_element, max_element, kroki
print("\nnieposortowana tablica")
print("min, max, kroki")
print(znajdz_min_max_nieposort(tablica_nieposortowana))


#drzewo binarne
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def znajdz_min(node):
    krok = 0 
    while node.left:
        krok += 1  
        node = node.left
    krok += 1 
    return node.value, krok

def znajdz_max(node):
    krok = 0  
    while node.right:
        krok += 1  
        node = node.right
    krok += 1  
    return node.value,krok

root = Node(17)
root.left = Node(5)
root.right = Node(21)
root.left.left = Node(4)
root.right.right = Node(31)

print("\n")
print("BST")
print("min, kroki")
print(znajdz_min(root))
print("max, kroki")
print(znajdz_max(root))
