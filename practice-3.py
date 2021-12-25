class Ser_Algo:

    # Linear Search Algorithm
    def lin_ser(self, arr, elem):
        if elem not in arr:
            return "Not Found"
        for i in range(len(arr)):
            if elem == arr[i]:
                return i+1

    # Improved Linear Search Algorithm
    def imp_lin_ser(self, arr, elem):
        if elem not in arr:
            return "Not Found"
        left = 0
        right = len(arr)-1
        while left <= right:
            if arr[left] == elem:
                return left+1
            if arr[right] == elem:
                return right+1
            left += 1
            right -= 1

    # Binary Search Algorithm
    def bin_ser(self, arr, elem, start, end):
        mid = int((start+end)/2)
        if start <= end:
            if arr[mid] == elem:
                return mid+1        
            elif arr[mid] > elem:
                return self.bin_ser(arr, elem, start, mid-1)
            elif arr[mid] < elem:
                return self.bin_ser(arr, elem, mid+1, end)
        else:
            return "Not Found"

if __name__ == '__main__':
    arr = [1,2,3,4,5,6]
    elem = 5
    algo = Ser_Algo()
    ind = algo.bin_ser(arr, elem, 0, len(arr)-1)
    print(f"Element found at {ind}")