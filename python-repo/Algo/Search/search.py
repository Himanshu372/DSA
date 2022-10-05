
class Search:
    def __init__(self, arr: list) -> None:
        self.input_arr = arr
        self.len_arr = len(arr)

    def binary_search(self, elem: int) -> int:
        index = 0
        curr_array = self.input_arr
        curr_pointer = curr_array[len(curr_array) // 2]
        while index == 0:
            if elem < curr_pointer:
                curr_array = curr_array[:(len(curr_array) // 2)]
                curr_pointer = curr_array[len(curr_array) // 2]
            elif elem > curr_pointer:
                curr_array = curr_array[(len(curr_array) // 2):]
                curr_pointer = curr_array[len(curr_array) // 2]
            else:
                index = self.input_arr.index(curr_pointer)
        return index

    def ternary_serach(self, elem: int) -> int:
        index = 0
        curr_array = self.input_arr
        curr_pointer = curr_array[len(curr_array) // 3]
        while index == 0:
            if elem < curr_pointer:
                curr_array = curr_array[:(len(curr_array) // 3)]
                curr_pointer = curr_array[len(curr_array) // 3]
            elif elem > curr_pointer:
                curr_array = curr_array[(len(curr_array) // 3):]
                curr_pointer = curr_array[len(curr_array) // 3]
            else:
                index = self.input_arr.index(curr_pointer)
        return index
