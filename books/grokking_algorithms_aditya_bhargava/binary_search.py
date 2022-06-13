def bin_search(lst: list, item):
    # variables `low` and `high` are stored the boundaries
    # of the part of the list where the search is performed
    low = 0
    high = len(lst) - 1

    # until this part is reduced to one element
    while low <= high:
        # check the middle element
        mid = int((low + high) / 2)
        guess = lst[mid]
        if guess == item:
            print(mid)
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
        print('Item not found!')
        return None


def main(lst: list, item):
    bin_search(lst, item)


if __name__ == '__main__':
    main([1, 20, 30, 45, 100, 320], 30)
    main([1, 20, 30, 45, 100, 320], 40)
