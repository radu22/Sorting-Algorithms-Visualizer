import pygame as py
import Object as obj
import random

size = (1500, 1000)
background = (255, 255, 255)
screen = py.display.set_mode(size)
py.display.set_caption("My First Game")

test = [900, 300, 200, 100, 500, 400, 600, 700, 800]
to_order = [100, 170, 90, 130, 180, 70, 210, 110, 240, 230, 160, 190, 250, 60, 200, 50, 220, 40, 140, 150, 30, 80, 20,
            120, 10]
rect_list = []

L = list(range(100, 500, 5))
random.shuffle(L)

for index, item in enumerate(L):
    a = obj.Rectangle(item, index)
    rect_list.append(a)


def refresh(items, delay=0, merge_sort=False):
    screen.fill(background)
    draw_rectangles(items, merge_sort)
    py.display.flip()
    py.time.wait(delay)


def draw_rectangles(items, merge_sort=False):
    for index, item in enumerate(items):
        if merge_sort:
            item.draw(screen, item.counter)
        else:
            item.draw(screen, index)


def mark_done(items, merge_sort=False):
    deselect_all(items)
    refresh(items, merge_sort)

    for index, item in enumerate(items):
        item.select()
        item.draw(screen, index)
        py.display.flip()
        py.time.wait(30)
        item.deselect()
    py.time.wait(100)


def deselect_all(items):
    for item in items:
        item.deselect()


def bubble_sort(nums, delay):
    # We set swapped to True so the loop looks runs at least once
    swapped = True
    while swapped:
        swapped = False
        found = False
        for i in range(len(nums) - 1):
            if not found:
                nums[i].select()
            refresh(nums)
            if nums[i].getHeight() > nums[i + 1].getHeight():
                nums[i].select()
                # Swap the elements
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Set the flag to True so we'll loop again
                swapped = True
                found = True

                refresh(nums,delay)
            deselect_all(nums)
            # py.time.wait(delay)


def selection_sort(nums, delay, detailed=False):
    # This value of i corresponds to how many values were sorted
    for i in range(len(nums)):
        # We assume that the first item of the unsorted segment is the smallest
        lowest_value_index = i
        nums[i].select()
        # This loop iterates over the unsorted items
        for j in range(i + 1, len(nums)):
            nums[j].select()
            refresh(nums, delay)

            if nums[j].getHeight() < nums[lowest_value_index].getHeight():
                lowest_value_index = j

            nums[j].deselect()
            refresh(nums)

        if detailed:
            nums[i].lowest_value()
            nums[lowest_value_index].lowest_value()
            refresh(nums, delay * 100)

        # Swap values of the lowest unsorted element with the first unsorted
        # element
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]

        deselect_all(nums)
        refresh(nums)


def insertion_sort(nums, delay):
    # Start on the second element as we assume the first element is sorted
    for i in range(1, len(nums)):
        item_to_insert = nums[i]

        # And keep a reference of the index of the previous element
        j = i - 1
        # Move all items of the sorted segment forward if they are larger than
        # the item to insert
        while j >= 0 and nums[j].getHeight() > item_to_insert.getHeight():
            deselect_all(nums)
            nums[j].select()
            nums[j].swap_h(item_to_insert)
            refresh(nums, delay)
            item_to_insert.swap_h(nums[j])
            nums[i].select()

            nums[j + 1] = nums[j]
            j -= 1

        # Insert the item
        nums[j + 1] = item_to_insert
        refresh(nums)
        deselect_all(nums)
        refresh(nums)


def heapify(nums, heap_size, root_index):
    # Assume the index of the largest element is the root index
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    # If the left child of the root is a valid index, and the element is greater
    # than the current largest element, then update the largest element
    if left_child < heap_size and nums[left_child].getHeight() > nums[largest].getHeight():
        largest = left_child

    # Do the same for the right child of the root
    if right_child < heap_size and nums[right_child].getHeight() > nums[largest].getHeight():
        largest = right_child

    # If the largest element is no longer the root element, swap them
    if largest != root_index:
        nums[root_index].select()
        nums[largest].lowest_value()
        refresh(nums, delay)
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        deselect_all(nums)
        nums[root_index].select()
        refresh(nums, delay)
        # Heapify the new root element to ensure it's the largest
        heapify(nums, heap_size, largest)


def heap_sort(nums):
    n = len(nums)

    # Create a Max Heap from the list
    # The 2nd argument of range means we stop at the element before -1 i.e.
    # the first element of the list.
    # The 3rd argument of range means we iterate backwards, reducing the count
    # of i by 1
    for i in range(n, -1, -1):
        heapify(nums, n, i)

    # Move the root of the max heap to the end of
    for i in range(n - 1, 0, -1):
        nums[i].lowest_value()
        nums[0].select()
        refresh(nums, delay)

        nums[i], nums[0] = nums[0], nums[i]

        deselect_all(nums)
        nums[0].select()
        nums[i].lowest_value()
        refresh(nums, delay)
        heapify(nums, i, 0)


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        mergeSort(L)  # Sorting the first half
        mergeSort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i].getHeight() < R[j].getHeight():
                L[i].select()
                refresh(arr, delay, True)
                deselect_all(arr)
                arr[k] = L[i]
                i += 1
            else:
                L[i].select()
                refresh(arr, delay, True)
                deselect_all(arr)
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def partition(nums, low, high):
    # We select the middle element to be the pivot. Some implementations select
    # the first element or the last element. Sometimes the median value becomes
    # the pivot, or a random one. There are many more strategies that can be
    # chosen or created.
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i].getHeight() < pivot.getHeight():
            i += 1

        j -= 1
        while nums[j].getHeight() > pivot.getHeight():
            j -= 1

        if i >= j:
            return j

        # If an element at i (on the left of the pivot) is larger than the
        # element at j (on right right of the pivot), then swap them
        nums[i].lowest_value()
        nums[j].select()
        refresh(nums, delay)
        nums[i], nums[j] = nums[j], nums[i]

        deselect_all(nums)



def quick_sort(nums):
    # Create a helper function that will be called recursively
    def _quick_sort(items, low, high):
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)

carryOn = True
not_sorted = True
delay = 10
clock = py.time.Clock()
# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in py.event.get():
        if event.type == py.QUIT:
            carryOn = False
    if not_sorted:
        # selection_sort(rect_list, delay, False)
        bubble_sort(rect_list, delay)
        # insertion_sort(rect_list, delay)
        # heap_sort(rect_list)
        # mergeSort(rect_list)
        # quick_sort(rect_list)
        mark_done(rect_list)

        not_sorted = False

    draw_rectangles(rect_list)
    py.display.flip()
    clock.tick(60)
py.quit()
