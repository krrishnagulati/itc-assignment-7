def merge_sort(arr):
    if len(arr) <= 1: #If the length of arr is 1 or less,
        # it means the array is already sorted, so it returns the array as is
        return arr
    
    mid = len(arr) // 2 #It calculates the middle index of the array using len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    #It recursively calls merge_sort() on left_half and right_half to sort them separately.
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    while i < len(left):
        merged.append(left[i])
        i += 1
    
    while j < len(right):
        merged.append(right[j])
        j += 1
    
    return merged

# Get the number of students from the user
n = int(input("Enter the number of students: "))
#This line prompts the user to enter the number of students and reads 
# the input as an integer, storing it in the variable n.

# Get the marks for each student
marks = [] #This line initializes an empty list called marks to store the marks of the students
for i in range(n):
    mark = int(input(f"Enter the mark for student {i+1}: "))
    marks.append(mark)

# Sort the marks using merge sort
sorted_marks = merge_sort(marks)
#This line calls the merge_sort() function with the marks list as the input.
#It assigns the returned sorted list to the variable sorted_marks.

# Print the sorted list
print("List after sorting is:", sorted_marks)
