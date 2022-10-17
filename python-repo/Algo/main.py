from Search.search import Search
from Sort.sort import Sort


if __name__ == "__main__":
    print("Started Execution")
    print("'Search' problems started")
    s = Search([0, 20, 30, 50, 60, 80, 110, 130, 140, 170])
    by_binary = s.binary_search(110)
    by_ternary = s.ternary_serach(110)
    print(f"Index by binary search: {by_binary}")
    print(f"Index by ternary search: {by_ternary}")
    print("'Search' problems end")

    print("'Sorting' problems started")
    l = [0, 30, 4, 78, 33, 56, 59, -110, 13, -1, 170]
    sr = Sort(l)
    by_bubble_sort = sr.bubble_sort()
    print(f"Array after sorting by bubble sort {by_bubble_sort}")
    by_insert_sort = sr.insertion_sort()
    print(f"Array after sorting by insertion sort {by_insert_sort}")
    by_merge_sort = sr.merge_sort()
    print(f"Array after sorting by merge sort {by_merge_sort}")
    by_quick_sort = sr.quick_sort()
    print(f"Array after sorting by quick sort {by_merge_sort}")