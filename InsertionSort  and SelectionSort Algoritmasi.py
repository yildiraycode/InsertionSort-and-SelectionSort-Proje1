#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Insertion Sort(ekleme sıralama algoritması)-(python programlama dilinde)
 
# insertion sort fonksiyonu
def insertionSort(arr):
 
    # 1'den len(arr) kadar gezin
    for i in range(1, len(arr)):
 
        key = arr[i]
 
        # key'den daha büyük olan arr[0..i-1] elemanlarını,
        # şu anki konumlarının bir ilerisine taşı
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
 
 
# sıralanacak array
arr = [22, 27, 16, 2, 18,6]
insertionSort(arr)
for i in range(len(arr)):
    print ("% d" % arr[i],end=" , ")

    
#Time Complexity:Big-O gösterimi:O(N^2)
#18 sayısı arıyorsak ortaya yakın bulunduğundan Average Case dir.


# In[2]:


# Selection Sort(seçim sıralama algoritması)-(python programlama dilinde)
# Sort 
import sys 
A = [7, 3, 5, 8, 2, 9, 4, 15, 6] 
  
# Tüm dizi elemanları üzerinde gezin
for i in range(len(A)): 
      
    # Kalan sırasız dizide minimum elemanı bul 
    min_idx = i 
    for j in range(i+1, len(A)): 
        if A[min_idx] > A[j]: 
            min_idx = j 
              
    # Bulunan minimum elemanı ilk eleman ile değiştir        
    A[i], A[min_idx] = A[min_idx], A[i] 
  
#sıralanacak array
for i in range(len(A)): 
    print("%d" %A[i],end=" , ") 
    
#Time Complexity:Big-O gösterimi:O(N^2)

