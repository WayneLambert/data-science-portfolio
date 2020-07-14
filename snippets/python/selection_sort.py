# Selection sort algorithm
""" The code is purposefully not written using Pythonic idioms """

def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array


if __name__ == '__main__':
    unsorted_square_nums = [49, 81, 1, 9, 36, 64, 81, 100, 4, 16, 25]

    sorted_square_nums = selection_sort(unsorted_square_nums)
    print(f"The sorted square numbers list is {sorted_square_nums}")
