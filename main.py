import time
import random

L = random.sample(range(1, 100001), 100000)
print(L)
#search_number = random.randint(1, len(L))
search_number = random.randint(1, len(L))

def research_linear(L, numero):
    for _ in range(len(L)):
        #print(L[_])
        if L[_] == numero:
            return print(f"Le nombre {numero} est dans la liste")
    return print(f"Le nombre {numero} n'est pas dans la liste")

def research_dichotomique(L, numero):
    order_list = sorted(L)
    start = 0
    end = len(order_list) - 1    
    for _ in range(len(order_list)):
        if start <= end:
            #print(order_list[start:end])
            mid = (start + end) // 2
            if order_list[mid] == numero:
                return print(f"Le nombre {numero} est dans la liste")
            elif order_list[mid] < numero:
                start = mid + 1
            else:
                end = mid - 1
        else:
            return print(f"Le nombre {numero} n'est pas dans la liste")


def timer(function, L, search_number):
    start = time.perf_counter()
    function(L, search_number)
    end = time.perf_counter()
    return print(f"Temps d'exécution : {end - start:.6f} secondes")

timer(research_linear, L, search_number)
timer(research_dichotomique, L, search_number)