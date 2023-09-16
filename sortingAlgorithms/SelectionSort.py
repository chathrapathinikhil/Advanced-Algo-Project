def SelectionSort(unsortedArray):
    # Traverse through array
        for i in range(len(unsortedArray)):
        
        # Find the minimum element in unsorted array
            min_idx = i
            for j in range(i+1, len(unsortedArray)):
                if unsortedArray[min_idx] > unsortedArray[j]:
                    min_idx = j
                
             # Swap  minimum element with the first element	
            unsortedArray[i], unsortedArray[min_idx] = unsortedArray[min_idx], unsortedArray[i]
            return unsortedArray

    
