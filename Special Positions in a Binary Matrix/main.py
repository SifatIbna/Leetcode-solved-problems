import numpy


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:

        def check_column(index):
            return

        array = numpy.array(mat)
        count = 0
        for i in range(array.shape[0]):
            if 1 in array[i, :]:
                index = array[i].tolist().index(1)
                if array[i, :].tolist().count(1) == 1 and array[:, index].tolist().count(1) == 1:
                    count += 1
        return count