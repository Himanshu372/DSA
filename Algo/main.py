from Search.search import Search

if __name__ == "__main__":
    print("Started Execution")
    s = Search([0, 20, 30, 50, 60, 80, 110, 130, 140, 170])
    by_binary = s.binary_search(110)
    print(f"Index by binary search: {by_binary}")