def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:#If arr[mid] is less than the target, 
            #it updates low to mid + 1 to search in the right half of the array
            low = mid + 1
        else:
            high = mid - 1#If arr[mid] is greater than the target, 
            #it updates high to mid - 1 to search in the left half of the array.

    return -1#If the target element is not found in the array, it returns -1.

# Get the input array from the user
input_array = list(map(int, input("Enter the integer array (comma-separated): ").split(',')))
#It reads the input as a string, splits it at commas, 
# and maps each element to an integer using the map() function.
#It converts the mapped elements into a list and assigns it to the variable input_array.



# Sort the array
sorted_array = sorted(input_array)
#This line sorts the input_array using the sorted() function 
# and assigns the sorted array to the variable sorted_array.




# Get the element to search from the user
element = int(input("Enter the element to search: "))
#This line prompts the user to enter the element they want to search for in the sorted array.
#It reads the input as an integer and assigns it to the variable element.




# Perform binary search
index = binary_search(sorted_array, element)
#This line calls the binary_search() function with the sorted_array and element as arguments.

if index == -1:
    print("Element not found.")
else:
    count = 1
    # Count the number of occurrences of the element
    # towards the left of the found index
    left = index - 1
    while left >= 0 and sorted_array[left] == element:
        count += 1
        left -= 1

    # Count the number of occurrences of the element
    # towards the right of the found index
    right = index + 1
    while right < len(sorted_array) and sorted_array[right] == element:
        count += 1
        right += 1

    print("Sorted array:", sorted_array)
    print(f"Number of occurrences of element {element} is: {count}")
