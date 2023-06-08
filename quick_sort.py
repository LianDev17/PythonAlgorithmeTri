liste = [22, -2, 6, -1, 4, 3]

#Tri fusion
def quick_sort(arr):  
    #Si la liste est vide
    if not arr:
        return arr
    
    pivot = arr[-1] # définition du pivot (-1 = dernier élément de la liste)
    left_arr = [val for val in arr if val < pivot] #On récupère tous les éléments inférieur au pivot
    right_arr = [val for val in arr[:-1] if val >= pivot] #On prends tous les éléments de la liste sauf le pivot. Puis on récupère tous les éléments supérieur au pivot                      
    
    #On fusionne le côté gauche, le pivot et le côté droit
    return quick_sort(left_arr) + [pivot] + quick_sort(right_arr)
    
#On affiche la liste triée
print(quick_sort(liste))