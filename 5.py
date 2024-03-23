class Score:
    def __init__(self,arr):
        self.arr=arr
        self.bubble_sort=self.arr.copy()
        self.selectionArr = self.arr.copy()
        self.insertionArr = self.arr.copy()
        self.shellSort = self.arr.copy()

    @staticmethod
    def ip(n):
        arr = []
        for i in range(n):
            arr.append(int(input("Enter Element of Array:")))
        return arr


    def bubbleSort(self):
        n=len(self.arr)
        print("Original Array:",self.bubble_sort)
        print()
        swapped=0
        for i in range(n-1):
            swapped=0
            for j in range(n-1-i):
                if self.bubble_sort[j]>self.bubble_sort[j+1]:
                    self.bubble_sort[j],self.bubble_sort[j+1]=self.bubble_sort[j+1],self.bubble_sort[j]
                    swapped=1
                    print("swapped ", j , " and " , j+1," Elements",self.bubble_sort)
            print()
            print("Swapped or not:", swapped)
            if swapped:
                continue
            return
        print()
        print("DONE ",n-1," COMPARISON")
        return 0

    def selection(self):
        n=len(self.selectionArr )
        print("Original Array:", self.selectionArr)
        print()
        for i in range(0,n-1):
            print()
            print("started comparing,",i," index")
            for j in range(i+1,n):
                if self.selectionArr [i]>self.selectionArr[j]:
                    self.selectionArr[j], self.selectionArr[i] = self.selectionArr[i], self.selectionArr[j]
                    print("swapped ", i, " and ", j, " Elements", self.selectionArr)
        return 0

    def insertion(self):
        n=len(self.insertionArr)
        print("Original Array:", self.insertionArr)
        for i in range(0,n-1):
            if self.insertionArr[i]>self.insertionArr[i+1]:
                print("element ", i, " is greater than ", i + 1, " Elements", self.insertionArr)
                self.insertionArr[i], self.insertionArr[i + 1] = self.insertionArr[i + 1], self.insertionArr[i]
                print("     **  inserting ,",i+1,"th element      ** ")
                while(i>0 and self.insertionArr[i]<self.insertionArr[i-1]):
                    self.insertionArr[i], self.insertionArr[i - 1] = self.insertionArr[i - 1], self.insertionArr[i]
                    i-=1
                print()
        return 0


    def shellsort(self):
        n = len(self.arr)
        print("Length of array is,",n)
        gap=n//2
        print("Let Gap be n//2 ,",gap)
        while(gap>0):
            j=gap
            print()
            print()
            print("As gap updated so new j = gap   j=", j)
            while(j<n):
                i = j - gap
                print()
                print("As j updated so new i = j-gap   i= ",i)
                while(i>=0):
                    if self.shellSort[i]>self.shellSort[i+gap]:
                        print("Swapping ,",i,"the element with",i+gap,"Element",self.shellSort)
                        self.shellSort[i],self.shellSort[i+gap]=self.shellSort[i+gap],self.shellSort[i]
                    else:
                        print(i,"th element is smaller than ",i+gap,"Element so breaking innermost loop",self.shellSort)
                        break
                    i -= gap
                    print("As i=i-gap      i = ",i)
                j+=1
                print("As j+=1      j = ", j)
            gap//=2
            print("Updating gap by gap//2",gap)

        return 0




target=int(input("Enter a Number of elements Which have to Sorted:"))
arr=Score.ip(target)
A=Score(arr)


while(1):
    print("""
    Welcome,
    1.Bubble Sort
    2.Selection Sort
    3.Insertion Sort
    4.Shell Sort
    
    6.Exit""")
    print()
    while(1):                      # Exceptional Handling for Choices
        try:
            choice=int(input("Enter Choice between 1-6:"))
            if (choice>0 and choice<=6):
                break
            print("<Wrong Choice>")
            print()
        except ValueError:
            print("Enter Correct Choice in <int> again")
            print()

    print()
    if choice==1:
        A.bubbleSort()
        print("Sorted list by Bubble sort is:",A.bubble_sort)
    elif choice==2:
        A.selection()
        print("Sorted list by Selection sort is:",A.selectionArr)
    elif choice==3:
        A.insertion()
        print("Sorted list by Insertion sort is:",A.insertionArr)
    elif choice==4:
        A.shellsort()
        print("Sorted list by Shell sort is:", A.shellSort)

    elif choice==6:
        break
    print()

