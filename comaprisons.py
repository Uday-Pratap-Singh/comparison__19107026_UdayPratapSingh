def selectionSort(arr):
  n = len(arr)
  compsel = 0
  swpsel = 0
  for i in range(n):
    
      min_idx = i
      for j in range(i+1, n):
          compsel += 1
          if arr[min_idx] > arr[j]:
              swpsel += 1
              min_idx = j
                  
      arr[i], arr[min_idx] = arr[min_idx], arr[i]
 

  print("Selection Sorted array is:")
  printList(arr)
  print("no. of comparisons in selection sort is %d" %compsel)
  print("no. of swaps in selection sort is %d" %swpsel)
  print("\n")
  print("\n")

def bubbleSort(arr):
    n = len(arr)
    swpbubb = 0
    compbubb = 0
    for i in range(n):
        for j in range(0, n-i-1):
          compbubb += 1
          if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swpbubb += 1

    print("Bubble Sorted array is:")
    printList(arr)
    print("no. of comparisons in bubble sort is %d" %compbubb)
    print("no. of swaps in bubble sort is %d" %swpbubb)
    print("\n")
    print("\n")

def printList(arr):
	for i in range(len(arr)):
		print(arr[i], end=" ")
	print("\n")


arr = [5,1,4,2,8]
print("Given array is", end="\n")
printList(arr)
bubbleSort(arr)

arr = [5,1,4,2,8]
selectionSort(arr)
