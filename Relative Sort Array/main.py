from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        if len(arr1) == 0 :
            return arr1
        if len(arr2) == 0 :
            arr1.sort()
            return arr1
        
        counter = [0]*1001
        for i in range(len(arr1)) :
            counter[arr1[i]] += 1
        
        res = []
        not_sorted = []
        for elem in arr2 :
            if elem in arr1 :
                res += [elem]*counter[elem]

        for elem in arr1 :
            if elem not in res :
                not_sorted.append(elem)
        
        not_sorted.sort()
        res += not_sorted
        return res