import copy


class Sort:
    def __init__(self, arr):
        self.arr = arr
        self.len_arr = len(arr)

    def bubble_sort(self):
        swap = 0
        shallow_arr = copy.copy(self.arr)
        for i in range(self.len_arr):
            for k in range(self.len_arr - i - 1):
                if shallow_arr[k] > shallow_arr[k + 1]:
                    swap += 1
                    temp = shallow_arr[k]
                    shallow_arr[k] = shallow_arr[k + 1]
                    shallow_arr[k + 1] = temp
        return shallow_arr






