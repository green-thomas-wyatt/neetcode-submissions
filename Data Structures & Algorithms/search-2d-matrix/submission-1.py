class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # Get middle array
        # Check if value is < or > or in it
        # Then repeat 

        l_index,r_index = 0, len(matrix) - 1


        while l_index <= r_index:
            mid_arr_index = (r_index + l_index) // 2
            mid_arr = matrix[mid_arr_index]

            # target is left(less) of mid array
            if mid_arr[0] > target:
                r_index = mid_arr_index - 1
                continue
            # target is right(greater) of mid array
            elif mid_arr[len(mid_arr)-1] < target:
                l_index = mid_arr_index + 1
                continue


            # We have found it
            else:
                l,r = 0, len(mid_arr) - 1
                while l <= r:
                    mid = (r+l) // 2
                    if mid_arr[mid] == target:
                        return True
                    # go right
                    elif mid_arr[mid] < target:
                        l = mid +1
                    # go left
                    elif mid_arr[mid] > target:
                        r = mid - 1
            return False
        return False