#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number < 0:
        return number * -1


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    liste_nom = []
    for c in prefixes:
        liste_nom.append(c + suffixe)
    return liste_nom



def prime_integer_summation() -> int:
    sum = 2
    nb_de_premier = 1
    i = 3
    while nb_de_premier < 100:
        for j in range(2, i):
            if i % j == 0:
                break
            elif j > i**0.5:
                sum += i
                nb_de_premier +=1
                break
        i += 2


    return sum




def factorial(number: int) -> int:
    for i in range (number - 1, 1, -1):
        number *= i
    return number


def use_continue() -> None:
    for i in range(1, 11):
        if i == 5:
            continue
        else:
            print(i)



def verify_ages(groups: List[List[int]]) -> List[bool]:
    acceptance = []
    for i in range(len(groups)):
        acceptance.insert(i, [])
        x = len(groups[i])
        if not(3 < len(groups[i]) < 10):
            acceptance[i] = False
        else:
            for j in range(len(groups[i])):
                if groups[i][j] == 25:
                    acceptance[i] = True
                    break
                elif groups[i][j] < 18:
                    acceptance[i] = False
                elif groups[i][j] == 50:
                    for j in range(len(groups[i])):
                        if groups[i][j] > 70:
                            acceptance[i] = False
                elif j == len(groups[i]) - 1 and acceptance[i] == []:
                    acceptance[i] = True
    print(len(groups[3]))
    return acceptance






def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
