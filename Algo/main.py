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
    sr = Sort([0, 30, 4, 78, 33, 56, 59, -110, 13, -1, 170])
    by_bubble_sort = sr.bubble_sort()
    print(f"Array after sorting by bubble sort {by_bubble_sort}")


