class Score:
    def __init__(self,arr):
        self.arr = arr.copy()
        self.SortedArr = self.arr.copy()
        self.QuickSort(0,len(self.SortedArr) - 1)

    @staticmethod
    def ip(n):
        arr = []
        for i in range(n):
            arr.append(float(input("Enter Percentages of each Student:")))
        return arr

    def QuickSort(self, start, end):

        print()
        print("**************************************************************************************************************")
        print("*********Next Call for from start = ", start, "end = ", end,"*********")
        if (start >= end):
            print("Call Exited")
            return            #Base Condn

        print()

        print("Pivote index = {}".format(end), "pivote element is {}".format(self.SortedArr[end]))
        print()

        #Soln for 1 case
        i = start
        j = start

        while(j < end):
            print()
            print(self.SortedArr)
            print("i = {}".format(i), "j = {}".format(j),"pivote index = {}".format(end))
            if (self.SortedArr[j] < self.SortedArr[end]):
                print("Swapping {} at j = {},  {} at i = {}".format(self.SortedArr[j],j, self.SortedArr[i],i))
                self.SortedArr[j], self.SortedArr[i] = self.SortedArr[i], self.SortedArr[j]
                print(self.SortedArr)
                i += 1
                print("i=++")
            print("j++")
            print() 
            j += 1

        print("\nWhile Ended\n")
        print("Require Partition index be {}".format(i))
        print("Swapping {} at end = {},  {} at i = {}".format(self.SortedArr[end], end, self.SortedArr[i], i))
        self.SortedArr[end], self.SortedArr[i] = self.SortedArr[i], self.SortedArr[end]
        print(self.SortedArr)
        print("**************************************************************************************************************")
        print()
        print()
        part = i
        self.QuickSort(start, part - 1)
        self.QuickSort(part + 1, end)


n=int(input("Enter a Number of Students :"))
arr=Score.ip(n)
A=Score(arr)
A.QuickSort(0,n-1)
print(A.SortedArr)

print()
print()
print("TOP 5 SCORES ARE")
for i in range(5):
    print(A.SortedArr[n-1-i])
