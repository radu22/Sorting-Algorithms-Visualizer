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


def refresh(items, delay=0):
    screen.fill(background)
    draw_rectangles(items)
    py.display.flip()
    py.time.wait(delay)


def draw_rectangles(items):
    for index, item in enumerate(items):
        item.draw(screen, index)


def mark_done(items):
    deselect_all(items)
    refresh(items)

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

                refresh(nums)
            deselect_all(nums)
            py.time.wait(delay)
    mark_done(nums)


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
        refresh(nums, delay)
    mark_done(nums)


def insertion_sort(nums, delay):
    # Start on the second element as we assume the first element is sorted
    for i in range(1, len(nums)):
        item_to_insert = nums[i]

        # nums[i].select()
        refresh(nums, delay)
        # And keep a reference of the index of the previous element
        j = i - 1
        # Move all items of the sorted segment forward if they are larger than
        # the item to insert
        while j >= 0 and nums[j].getHeight() > item_to_insert.getHeight():
            # nums[j].select()
            aux = nums[j+1].getHeight()

            nums[j].lowest_value()
            nums[j+1].select()

            nums[j+1].change_h(item_to_insert.getHeight())
            nums[j+2].to_be_inserted()
            refresh(nums, delay * 10)
            deselect_all(nums)

            nums[j+1].change_h(aux)
            # nums[j].to_be_inserted()
            nums[j + 1] = nums[j]
            nums[i].select()

            j -= 1

        # Insert the item
        nums[j + 1] = item_to_insert
        # nums[j+1].select()
        refresh(nums, delay)
        deselect_all(nums)
        refresh(nums, delay)
    mark_done(nums)


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
        # bubble_sort(rect_list, delay)
        insertion_sort(rect_list, delay)
        not_sorted = False
    draw_rectangles(rect_list)
    py.display.flip()
    clock.tick(60)
py.quit()
