class Matrix:
    def __init__(self, l1, m1, n1, l2, m2, n2):
        self.l1, self.m1, self.n1 = l1.copy(), m1, n1
        self.l2, self.m2, self.n2 = l2.copy(), m2, n2

    @staticmethod
    def mt_list(m, n):
        temp = []
        arr = []
        for i in range(n):
            temp.append(0)
        for i in range(m):
            arr.append(temp.copy())
        return arr

    @staticmethod
    def input(m , n):
        arr = []
        for i in range(m):
            temp = input("Enter Element in row (COMMA Saperated: )")
            l2 = temp.split(",")
            for j in range(n):
                l2[j] = int(l2[j])
            arr.append(l2[:n])
        return arr

    @staticmethod
    def display(arr):
        for i in range(len(arr)):
            print(arr[i])

    def addition(self):
        l1 = self.l1.copy()
        l2 = self.l2.copy()
        if (self.m1 == self.m2 and self.n1 == self.n2):
            add_list = Matrix.mt_list(self.m1, self.n1)
            for i in range(len(l1)):
                for j in range(len(l1[0])):
                    add_list[i][j] = l1[i][j] + l2[i][j]
            return add_list
        return 1

    def subtraction(self):
        l1 = self.l1.copy()
        l2 = self.l2.copy()
        if (self.m1 == self.m2 and self.n1 == self.n2):
            sub_list = (Matrix.mt_list(self.m1, self.n1)).copy()
            for i in range(self.m1):
                for j in range(self.n1):
                    sub_list[i][j] = l1[i][j] - l2[i][j]
            return sub_list
        return 1

    def transpose(self):
        l1 = self.l1.copy()
        l2 = self.l2.copy()
        l1_t = (Matrix.mt_list(self.n1, self.m1)).copy()
        l2_t = (Matrix.mt_list(self.n2, self.m2)).copy()
        for i in range(self.m1):
            for j in range(self.n1):
                l1_t[i][j] = l1[j][i]

        return l1_t

    def multiplication(self):
        l1 = self.l1.copy()
        l2 = self.l2.copy()
        if (self.n1 == self.m2):
            multiply = Matrix.mt_list(self.m1, self.n2)
            for i in range(self.m1):
                for j in range(self.n2):
                    for k in range(self.n1):
                        multiply[i][j] += l1[i][k] * l2[k][j]
            return multiply
        return 1



flag=1

while (1):
    print("""
    1.Addition
    2.Subtraction
    3.Transpose
    4.Multiplication
    5.Exit""")
    print()
    while (1):  # Exceptional Handling for Choices
        try:
            choice = int(input("Enter Choice between 1-5:"))
            if (choice > 0 and choice <= 5):
                break
            print("<Wrong Choice>")
            print()
        except ValueError:
            print("Enter Correct Choice in <int> again")
            print()

    print()
    if choice==1 or choice==2:
        print('''Let First Matrix be, A''')
        str1 = input("Enter The Order Of Matrix as m*n: ")
        l = str1.split("*")
        m1 = int(l[0])
        n1 = int(l[1])


        print()
        print('Let Second Matrix be B')
        str1 = input("Enter The Order Of Matrix as m*n: ")
        l = str1.split("*")
        m2 = int(l[0])
        n2 = int(l[1])
        if (m1==m2 and n1==n2):
            print("Elements Of Matrix A:")
            l1 = Matrix.input(m1, n1)

            print("Elements Of Matrix B:")
            l2= Matrix.input(m1,n1)
            A = Matrix(l1, m1, n1, l2, m2, n2)

            print("Entered Matrix Are;")
            Matrix.display(A.l1)
            print()
            Matrix.display(A.l2)
            print()
        else:
            print("Addition and Subtraction Not Possible")
            continue

    if choice == 4:
        print('''Let First Matrix be, A''')
        str1 = input("Enter The Order Of Matrix as m*n: ")
        l = str1.split("*")
        m1 = int(l[0])
        n1 = int(l[1])

        print()
        print('Let Second Matrix be B')
        str1 = input("Enter The Order Of Matrix as m*n: ")
        l = str1.split("*")
        m2 = int(l[0])
        n2 = int(l[1])
        if (n1==m2):
            print("Elements Of Matrix A:")
            l1 = Matrix.input(m1, n1)

            print("Elements Of Matrix B:")
            l2 = Matrix.input(m1, n1)
            A = Matrix(l1, m1, n1, l2, m2, n2)

            print("Entered Matrix Are;")
            Matrix.display(A.l1)
            print()
            Matrix.display(A.l2)
            print()
        else:
            print("Multiplication Not Possible")
            continue

    if choice == 1:
        if (A.addition() != 1):
            print("Addition is,")
            Matrix.display(A.addition())
        else:
            print("Addition Not Possible")
    elif choice == 2:
        if (A.addition() != 1):
            print("Subtraction is,")
            Matrix.display(A.subtraction())
        else:
            print("Subtraction Not Possible")
    elif choice == 3:
        print('''Let First Matrix be, A''')
        str1 = input("Enter The Order Of Matrix as m*n: ")
        l = str1.split("*")
        m1 = int(l[0])
        n1 = int(l[1])
        print("Elements Of Matrix A:")
        l1 = Matrix.input(m1, n1)
        print("Entered Matrix Are;")
        Matrix.display(A.l1)

        a = A.transpose()
        print("Transpose of A is,")
        Matrix.display(a)

    elif choice == 4:
        if (A.multiplication() != 1):
            print("Multiplication is,")
            Matrix.display(A.multiplication())
        else:
            print("Multiplication Not Possible")

    elif choice == 5:
        break
    print()