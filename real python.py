#CSE 112 Practical
#Pyhton sorting algorithms





'''def bubble_sort(array):

    n = len(array)


    for i in range(n):

        # Create a flag that will allow the function to

        # terminate early if there's nothing left to sort

        already_sorted = True


        # Start looking at each item of the list one by one,

        # comparing it with its adjacent value. With each

        # iteration, the portion of the array that you look at

        # shrinks because the remaining items have already been

        # sorted.

        for j in range(n - i - 1):

            if array[j] > array[j + 1]:

                # If the item you're looking at is greater than its

                # adjacent value, then swap them

                array[j], array[j + 1] = array[j + 1], array[j]


                # Since you had to swap two elements,

                # set the `already_sorted` flag to `False` so the

                # algorithm doesn't finish prematurely

                already_sorted = False


        # If there were no swaps during the last iteration,

        # the array is already sorted, and you can terminate

        if already_sorted:

            break
    return array
myArray=[3,1,4,2];
print(bubble_sort(myArray));


def insertion_sort(array):

    # Loop from the second element of the array until

    # the last element

    for i in range(1, len(array)):

        # This is the element we want to position in its

        # correct place

        key_item = array[i]


        # Initialize the variable that will be used to

        # find the correct position of the element referenced

        # by `key_item`

        j = i - 1


        # Run through the list of items (the left

        # portion of the array) and find the correct position

        # of the element referenced by `key_item`. Do this only

        # if `key_item` is smaller than its adjacent values.

        while j >= 0 and array[j] > key_item:

            # Shift the value one position to the left

            # and reposition j to point to the next element

            # (from right to left)

            array[j + 1] = array[j]

            j -= 1


        # When you finish shifting the elements, you can position

        # `key_item` in its correct location

        array[j + 1] = key_item


    return array
ourArray=[2,1,4,3];
print(insertion_sort(ourArray));


def merge(left, right):

    # If the first array is empty, then nothing needs

    # to be merged, and you can return the second array as the result

    if len(left) == 0:

        return right


    # If the second array is empty, then nothing needs

    # to be merged, and you can return the first array as the result

    if len(right) == 0:

        return left


    result = []

    index_left = index_right = 0


    # Now go through both arrays until all the elements

    # make it into the resultant array

    while len(result) < len(left) + len(right):

        # The elements need to be sorted to add them to the

        # resultant array, so you need to decide whether to get

        # the next element from the first or the second array

        if left[index_left] <= right[index_right]:

            result.append(left[index_left])

            index_left += 1

        else:

            result.append(right[index_right])

            index_right += 1


        # If you reach the end of either array, then you can

        # add the remaining elements from the other array to

        # the result and break the loop

        if index_right == len(right):

            result += left[index_left:]

            break


        if index_left == len(left):

            result += right[index_right:]

            break


    return result



def merge_sort(array):

    # If the input array contains fewer than two elements,

    # then return it as the result of the function

    if len(array) < 2:

        return array


    midpoint = len(array) // 2


    # Sort the array by recursively splitting the input

    # into two equal halves, sorting each half and merging them

    # together into the final result

    return merge(

        left=merge_sort(array[:midpoint]),

        right=merge_sort(array[midpoint:]))

yourArray=[9,10,55,12,100,-2.3,0];
print( merge_sort(yourArray));




from random import randint


def quicksort(array):

    # If the input array contains fewer than two elements,

    # then return it as the result of the function

    if len(array) < 2:

        return array


    low, same, high = [], [], []


    # Select your `pivot` element randomly

    pivot = array[randint(0, len(array) - 1)]


    for item in array:

        # Elements that are smaller than the `pivot` go to

        # the `low` list. Elements that are larger than

        # `pivot` go to the `high` list. Elements that are

        # equal to `pivot` go to the `same` list.

        if item < pivot:

            low.append(item)

        elif item == pivot:

            same.append(item)

        elif item > pivot:

            high.append(item)


    # The final result combines the sorted `low` list

    # with the `same` list and the sorted `high` list

    return quicksort(low) + same + quicksort(high)

isArray=[9,10,55,12,100,-2.3,0];
print(quicksort(isArray));





def heapify(array, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    
    if l < n and array[i] < array[l]:
        largest = l
    if r < n and array[largest] < array[r]:
        largest = r
    
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)
        
def heapSort(array):
    n = len(array)
    for i in range(n//2, -1, -1):
        heapify(array, n, i)
    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
    return array

thatArray=[9,10,55,12,100,-2.3,0];
print(heapSort(thatArray));




def shellSort(input_list):
   gap = len(input_list) // 2
   while gap > 0:
      for i in range(gap, len(input_list)):
         temp = input_list[i]
         j = i
# Sort the sub list for this gap
   while j >= gap and input_list[j - gap] > temp:
      input_list[j] = input_list[j - gap]
      j = j-gap
      input_list[j] = temp
# Reduce the gap for the next element
   gap = gap//2
list = [19,2,31,45,30,11,121,27]
shellSort(list)
print(list)


 

def selection_sort(arr, n):
	for i in range(n):

		## to store the index of the minimum element
		min_element_index = i
		for j in range(i + 1, n):
			## checking and replacing the minimum element index
			if arr[j] < arr[min_element_index]:
				min_element_index = j

		## swaping the current element with minimum element
		arr[i], arr[min_element_index] = arr[min_element_index], arr[i]

if __name__ == '__main__':
	## array initialization
	arr = [3, 4, 7, 8, 1, 9, 5, 2, 6]
	selection_sort(arr, 9)

	## printing the array
	print(str(arr))







