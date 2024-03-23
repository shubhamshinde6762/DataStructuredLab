class Student:
    def __init__(self,arr=0):
        if arr==0:
            arr=Student.ip(int(input("Enter Number Of Elements in Array:")))
        self.arr=arr.copy()
        arr.sort()
        self.arrSorted = arr.copy()
    @staticmethod
    def ip(n):
        arr=[]
        for i in range(n):
            arr.append(int(input("Enter Element of Array:")))
        return arr

    def linear(self,target):
        print("Target = ", target)
        for i in range(len(self.arr)):
            print("element at", i, "is", self.arr[i])
            if self.arr[i]==target:
                return i
        else:
            return -1

    def sentinel(self,target):
        i=0
        print("Target = ", target)
        self.arr.append(target)
        print("element appended to last index ", self.arr[len(self.arr) - 1])
        while self.arr[i]!=target:
            i+=1
        self.arr.pop()
        if (i<len(self.arr)):
            return i
        return -1

    def binarySearch(self,target):
        print("Sorted Array is,",self.arrSorted)
        start=0
        end=len(self.arrSorted)-1
        mid=(int)(start+(end-start)/2)

        while(start<=end):
            if self.arrSorted[mid]==target:
                return mid
            elif self.arrSorted[mid]<target:
                #Right Search
                start=mid+1
            else:
                #Left Search
                end=mid-1
            mid=(int)(start+(end-start)/2)

        return -1
    def binaryRecur(self,target,start=0,end=0,mid=0):
        if end==0:
            end=len(self.arrSorted)
            mid=(int)((start+end)/2)
        if start>end:
            return -1
        if self.arrSorted[mid] == target:
            return mid
        elif self.arrSorted[mid] < target:
            # Right Search
            start = mid + 1
            mid = (int)(start + (end - start) / 2)
            return self.binarySearch(target,start,end,mid)
        else:
            # Left Search
            end = mid - 1
            mid = (int)(start + (end - start) / 2)
            return self.binarySearch(target, start, end, mid)





A=Student()
target=int(input("Enter a Number Which have to Search:"))

print("Index Returned From Linear Search is,",A.linear(target))
print("Index Returned From Sentinel Search is,",A.sentinel(target))
print("Index of Sorted Array Returned From Binary Search is,",A.binarySearch(target))
