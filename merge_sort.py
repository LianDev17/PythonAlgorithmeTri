liste = [22, 6, 4, 56]

#Tri fusion
def merge_sort(arr):
    #On vérifie si la liste traitée contient moins ou est égale à un seul élément
    if len(arr) <= 1:
        return arr
        
    mid = len(arr) // 2 #On coupe la liste en deux avec // pour arrondir la valeur (// => Python3)
   
    #On tri directement les côtés gauche et droite pour les utiliser déjà trié  
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])
  
    merged_arr = []
    i = j = 0 #i et j sont des positions dans les listes respectives gauche et droite

    #On vérifie que i et j sont toujours plus petit que leur liste respectif pour éviter les erreurs d'index
    while i < len(left_arr) and j < len(right_arr):
        #On vérifie si le membre de gauche est plus petit que celui de droite pour les ajouter dans l'ordre croissant dans la liste
        if left_arr[i] < right_arr[j]:
            merged_arr.append(left_arr[i])
            i += 1
        else:
            merged_arr.append(right_arr[j])       
            j += 1                    
    
    
    #On ajoute les éléments restant à la liste triée
    merged_arr.extend(left_arr[i:])
    merged_arr.extend(right_arr[j:])
    
    return merged_arr
    
#On affiche la liste triée
print(merge_sort(liste))