import copy
from random import randint

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

    def selection_sort(self):
        steps = 0
        l = copy.copy(self.arr)
        n = self.len_arr
        for i in range(self.n):
            m = min(self.arr[i:n])
            #print(m)
            temp = l[i]
            l[l.index(m)] = temp
            #print(l)
            l[i] = m
            #print(l)
            # steps += 1
            # if steps == s:
            #     print(' '.join(str(k) for k in l))
            #     break
        return l

    def insertion_sort(self):
        l = copy.copy(self.arr)
        n = self.len_arr
        for i in range(1, n):
            for j in range(i - 1, 0, -1):
                if l[j] < l[j - 1]:
                    temp = l[j - 1]
                    l[j - 1] = l[j]
                    l[j] = temp
        return l


    def merge_sort(self):
        l = copy.copy(self.arr)
        return self.recursive_merge(l)

    def recursive_merge(self, l):
        if len(l) <= 1:
            return l
        left, right = self.recursive_merge(l[:len(l) // 2]), self.recursive_merge(l[len(l) // 2:])
        return self.merge(left, right)

    @staticmethod
    def merge(l, r):
        left_ind = right_ind = 0
        p = []
        while left_ind != len(l) and right_ind != len(r):
            if l[left_ind] < r[right_ind]:
                p.append(l[left_ind])
                left_ind += 1
            elif r[right_ind] < l[left_ind]:
                p.append(r[right_ind])
                right_ind += 1
            else:
                p.append(l[left_ind])
                left_ind += 1
                right_ind += 1
        if left_ind == len(l):
            p.extend(r[right_ind:])
        elif right_ind == len(r):
            p.extend(l[left_ind:])
        return p

    #Chose a pivot for each subarray and arrange elements according to that pivot
    #O(NlogN)
    def quick_sort(self):
        return self.recursive_merge(self.arr)

    def recursive_quick_sort(self, a):
        if len(a) <= 1:
            return a
        piv = randint(0, (len(a) - 1))
        left, center, right = [], [], []
        for i in a:
            if i < a[piv]:
                left.append(i)
            elif i == a[piv]:
                center.append(i)
            else:
                right.append(i)
        return self.recursive_quick_sort(left) + center + self.recursive_quick_sort(right)

