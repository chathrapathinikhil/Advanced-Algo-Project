from sortingAlgorithms import InsertionSort,MergeSort,BubbleSort,HeapSort
import time



class SortString:

       
    #function to sort string array
    def SortString(UnSortedArray,sortMethod):

        #use below sorting algorithms for String Input  
        sortingmethods = {
        "InsertionSort":InsertionSort.insertion_sort(UnSortedArray),
        "BubbleSort":BubbleSort.bubble_sort(UnSortedArray),
        "MergeSort":MergeSort.merge_sort(UnSortedArray),
        "HeapSort":HeapSort.heap_sort(UnSortedArray)



        }
        # start timer
        start = time.process_time()
        #sort array using user inputted method
        sortedArray = sortingmethods[sortMethod]
        #end timer
        end = time.process_time()
        return sortedArray,end-start




#replace hardcoded input with the input from  frontend
UnSortedArray =["California State University Fullerton", "California State University East Bay","California State University Long Beach","University Of Southern California", "Arizona State Univerity"]

print("Unsorted array")

for i in UnSortedArray:
  print(i)

sortingmethod =input("Select Sorting Mehtods:  InsertionSort BubbleSort  MergeSort HeapSort ")



sortedArray, time_consumed = SortString.SortString(UnSortedArray,sortingmethod)
print("Time Consumed " ,time_consumed)
print("Sorted array")
for i in sortedArray:
  print(i)