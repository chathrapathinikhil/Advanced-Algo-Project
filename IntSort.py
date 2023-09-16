from sortingAlgorithms import InsertionSort,MergeSort,BubbleSort,HeapSort,BucketSort_090923,CountingSort_090923,QuickSort,RadixSort_090923,SelectionSort
import time



class SortInteger:

       
    #function to sort string array
    def SortInteger(UnSortedArray,sortMethod):

        #use below sorting algorithms for String Input  
        sortingmethods = {

        "InsertionSort":list(InsertionSort.insertion_sort(UnSortedArray)),
        "BubbleSort":list(BubbleSort.bubble_sort(UnSortedArray)),
        "MergeSort":list(MergeSort.merge_sort(UnSortedArray)),
        "HeapSort":list(HeapSort.heap_sort(UnSortedArray)),
        "BucketSort":list(BucketSort_090923.bucket_sort(UnSortedArray)),
        "CountingSort":list(CountingSort_090923.counting_sort(UnSortedArray)),
        "QuickSort":list(QuickSort.quick_sort(UnSortedArray, 0, len(UnSortedArray)-1)),
        "RadixSort":list(RadixSort_090923.radix_sort(UnSortedArray)),
        "SelectionSort":list(SelectionSort.SelectionSort(UnSortedArray))
        
        }
        # start timer
        start = time.time()
        print(start)
        #sort array using user inputted method

        sortedArray = sortingmethods[sortMethod]

        #end timer
        end = time.time()
        print(end)
        return sortedArray,end-start



if __name__ == '__main__':
    #replace hardcoded input with the input from  frontend
    UnSortedArray =[211,34,545,6,1,0]
    print("Unsorted array",UnSortedArray)

    sortingmethod =input("Select Sorting Mehtods:  InsertionSort BubbleSort  MergeSort HeapSort BucketSort CountingSort QuickSort RadixSort SelectionSort")
    
    sortedArray, time_consumed = SortInteger.SortInteger(UnSortedArray,sortingmethod)
    print(f"Time Consumed {time_consumed*1000000} micro seconds")
    print("Sorted array",sortedArray)

