def remove_duplicates(nums):
    return list(set(nums))
#It converts the list into a set using the set() function,
#  which automatically removes duplicate elements.

#It converts the set back to a list using the list() function
#  to maintain the original order of elements.
#The function returns the list with duplicates removed.

def selection_sort(nums): #This function implements the selection sort algorithm to sort a list nums in ascending order.
    for i in range(len(nums)):
        min_idx = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_idx]:#If an element at index j is found to be smaller than the current minimum element, it updates min_idx to j
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]

def bubble_sort(nums):
    n = len(nums)
    for i in range(n-1):
        for j in range(n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

# Get the input array from the user
input_array = list(map(int, input("Enter the integer array (comma-separated): ").split(',')))
#It reads the input as a string, splits it at commas, and maps each element to an integer using the map() function.
#It converts the mapped elements into a list and assigns it to the variable input_array.



# Remove duplicates from the array
distinct_array = remove_duplicates(input_array)
#This line calls the remove_duplicates() function with input_array as an argument.
#It assigns the returned list with duplicates removed to the variable distinct_array.




# Sort the array using selection sort
selection_sort(distinct_array)
selection_sorted_array = distinct_array.copy()

# Sort the array using bubble sort
bubble_sort(distinct_array)
bubble_sorted_array = distinct_array.copy()

print("Sorted array (Selection Sort):", selection_sorted_array)
print("Sorted array (Bubble Sort):", bubble_sorted_array)
