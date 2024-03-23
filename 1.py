#A=Cricket
#B=Badminton
#C=Football

#list of student who play both Cricket and Badminton CUB
#List of student who play either C or B but not both CUB-CnB
#Number of Student who play neither C or B F-C-B
#number of student who play cricket and football but not badminton CUF-B


def set_common(a):    #remove Duplicate Entries
    result = []
    for i in range(len(a)):
        for j in result:
            if a[i] == j:
                break
        else:
            result.append(a[i])
    return result


def union_set(a , b):   #return Union of two lists
    union = []
    for i in a:
        union.append(i)
    for i in b:
        union.append(i)
    union = set_common(union)
    return union


def intersection(a , b):   #return intersection betn two lists
    result = []
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                result.append(a[i])
                break
    result = set_common(result)
    return result


def diff(a ,b):              #return difference of two sets
    inter = intersection(a , b)
    for i in inter:
        a.remove(i)
    a=set_common(a)
    return a

########################################### Data Entry Starts
c = []
b = []
f = []

l = int(input("Enter Number of Players Playing Cricket:"))
for i in range(l):
    temp=int(input("Enter the jersey number of player playing Cricket:"))
    c.append(temp)

m = int(input("Enter Number of Players Playing Badminton:"))
for i in range(m):
    temp=int(input("Enter the jersey number of player playing Badminton:"))
    b.append(temp)

n = int(input("Enter Number  of Players Playing Football:"))
for i in range(n):
    temp=int(input("Enter the jersey number of player playing Football :"))
    f.append(temp)

############################################ Data Entry Completed

print("""
Welcome to Class SE,
Here we are helping to find out the followed data using user provided data:
1.List of student who play both Cricket and Badminton CUB
2.List of student who play either Cricket or Badminton but not both CUB-CnB
3.Number of Student who play neither Cricket nor Badminton F-C-B
4.Number of student who play cricket and football but not badminton CUF-B
""")


yes=1
while(yes):
    while(1):                      # Exceptional Handling for Choices
        try:
            choice=int(input("Enter Choice between 1-4:"))
            if (choice>0 and choice<5):
                break
            print("<Wrong Choice>")
            print()
        except ValueError:
            print("Enter Correct Choice in <int> again")
            print()


    if choice==1:
        print("List of student who play both Cricket and Badminton:",union_set(c,b))
    elif choice==2:
        cub=union_set(c,b)
        cnb=intersection(c,b)
        print("List of student who play either Cricket or Badminton but not both:",diff(cub,cnb))
    elif choice==3:
        f_c=diff(f,c)
        print("List of Student who play neither Cricket nor Badminton F-C-B:", diff(f_c, b))
        print("Number of Student who play neither Cricket nor Badminton F-C-B:", len(diff(f_c, b)))
    elif choice==4:
        cuf=union_set(c,f)
        print("List of Student who play neither Cricket nor Badminton F-C-B:", diff(cuf, b))
        print("Number of student who play cricket and football but not badminton:", len(diff(cuf, b)))
    print()

    while(1):                         #Exceptional Handling for YES
        try:
            yes=int(input("""Are you Want to Continue to with this Data? Press (1/0)"""))
            if (yes==1 or yes==0):
                break
            print("Wrong Choice")
            print()
        except ValueError:
            print("Press 1/0 <int>")
            print()

    if yes==1:
        print("""
        Here we are helping to find out the followed data using user provided data:
        1.List of student who play both Cricket and Badminton CUB
        2.List of student who play either Cricket or Badminton but not both CUB-CnB
        3.Number of Student who play neither Cricket nor Badminton F-C-B
        4.Number of student who play cricket and football but not badminton CUF-B
        """)
        continue
    else:
        print("Programme Exited")
        break











#A=Cricket
#B=Badminton
#C=Football

#list of student who play both Cricket and Badminton CUB
#List of student who play either C or B but not both CUB-CnB
#Number of Student who play neither C or B F-C-B
#number of student who play cricket and football but not badminton CUF-B


def set_common(a):    #remove Duplicate Entries
    result = []
    for i in range(len(a)):
        for j in result:
            if a[i] == j:
                break
        else:
            result.append(a[i])
    return result


def union_set(a , b):   #return Union of two lists
    union = []
    for i in a:
        union.append(i)
    for i in b:
        union.append(i)
    union = set_common(union)
    return union


def intersection(a , b):   #return intersection betn two lists
    result = []
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                result.append(a[i])
                break
    result = set_common(result)
    return result


def diff(a ,b):              #return difference of two sets
    inter = intersection(a , b)
    for i in inter:
        a.remove(i)
    a=set_common(a)
    return a

########################################### Data Entry Starts
c = []
b = []
f = []

l = int(input("Enter Number of Players Playing Cricket:"))
for i in range(l):
    temp=int(input("Enter the jersey number of player playing Cricket:"))
    c.append(temp)

m = int(input("Enter Number of Players Playing Badminton:"))
for i in range(m):
    temp=int(input("Enter the jersey number of player playing Badminton:"))
    b.append(temp)

n = int(input("Enter Number  of Players Playing Football:"))
for i in range(n):
    temp=int(input("Enter the jersey number of player playing Football :"))
    f.append(temp)

############################################ Data Entry Completed

print("""
Welcome to Class SE,
Here we are helping to find out the followed data using user provided data:
1.List of student who play both Cricket and Badminton CUB
2.List of student who play either Cricket or Badminton but not both CUB-CnB
3.Number of Student who play neither Cricket nor Badminton F-C-B
4.Number of student who play cricket and football but not badminton CUF-B
""")


yes=1
while(yes):
    while(1):                      # Exceptional Handling for Choices
        try:
            choice=int(input("Enter Choice between 1-4:"))
            if (choice>0 and choice<5):
                break
            print("<Wrong Choice>")
            print()
        except ValueError:
            print("Enter Correct Choice in <int> again")
            print()


    if choice==1:
        print("List of student who play both Cricket and Badminton:",union_set(c,b))
    elif choice==2:
        cub=union_set(c,b)
        cnb=intersection(c,b)
        print("List of student who play either Cricket or Badminton but not both:",diff(cub,cnb))
    elif choice==3:
        f_c=diff(f,c)
        print("List of Student who play neither Cricket nor Badminton F-C-B:", diff(f_c, b))
        print("Number of Student who play neither Cricket nor Badminton F-C-B:", len(diff(f_c, b)))
    elif choice==4:
        cuf=union_set(c,f)
        print("List of Student who play neither Cricket nor Badminton F-C-B:", diff(cuf, b))
        print("Number of student who play cricket and football but not badminton:", len(diff(cuf, b)))
    print()

    while(1):                         #Exceptional Handling for YES
        try:
            yes=int(input("""Are you Want to Continue to with this Data? Press (1/0)"""))
            if (yes==1 or yes==0):
                break
            print("Wrong Choice")
            print()
        except ValueError:
            print("Press 1/0 <int>")
            print()

    if yes==1:
        print("""
        Here we are helping to find out the followed data using user provided data:
        1.List of student who play both Cricket and Badminton CUB
        2.List of student who play either Cricket or Badminton but not both CUB-CnB
        3.Number of Student who play neither Cricket nor Badminton F-C-B
        4.Number of student who play cricket and football but not badminton CUF-B
        """)
        continue
    else:
        print("Programme Exited")
        break











#A=Cricket
#B=Badminton
#C=Football

#list of student who play both Cricket and Badminton CUB
#List of student who play either C or B but not both CUB-CnB
#Number of Student who play neither C or B F-C-B
#number of student who play cricket and football but not badminton CUF-B


def set_common(a):    #remove Duplicate Entries
    result = []
    for i in range(len(a)):
        for j in result:
            if a[i] == j:
                break
        else:
            result.append(a[i])
    return result


def union_set(a , b):   #return Union of two lists
    union = []
    for i in a:
        union.append(i)
    for i in b:
        union.append(i)
    union = set_common(union)
    return union


def intersection(a , b):   #return intersection betn two lists
    result = []
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                result.append(a[i])
                break
    result = set_common(result)
    return result


def diff(a ,b):              #return difference of two sets
    inter = intersection(a , b)
    for i in inter:
        a.remove(i)
    a=set_common(a)
    return a

########################################### Data Entry Starts
c = []
b = []
f = []

l = int(input("Enter Number of Players Playing Cricket:"))
for i in range(l):
    temp=int(input("Enter the jersey number of player playing Cricket:"))
    c.append(temp)

m = int(input("Enter Number of Players Playing Badminton:"))
for i in range(m):
    temp=int(input("Enter the jersey number of player playing Badminton:"))
    b.append(temp)

n = int(input("Enter Number  of Players Playing Football:"))
for i in range(n):
    temp=int(input("Enter the jersey number of player playing Football :"))
    f.append(temp)

############################################ Data Entry Completed

print("""
Welcome to Class SE,
Here we are helping to find out the followed data using user provided data:
1.List of student who play both Cricket and Badminton CUB
2.List of student who play either Cricket or Badminton but not both CUB-CnB
3.Number of Student who play neither Cricket nor Badminton F-C-B
4.Number of student who play cricket and football but not badminton CUF-B
""")


yes=1
while(yes):
    while(1):                      # Exceptional Handling for Choices
        try:
            choice=int(input("Enter Choice between 1-4:"))
            if (choice>0 and choice<5):
                break
            print("<Wrong Choice>")
            print()
        except ValueError:
            print("Enter Correct Choice in <int> again")
            print()


    if choice==1:
        print("List of student who play both Cricket and Badminton:",union_set(c,b))
    elif choice==2:
        cub=union_set(c,b)
        cnb=intersection(c,b)
        print("List of student who play either Cricket or Badminton but not both:",diff(cub,cnb))
    elif choice==3:
        f_c=diff(f,c)
        print("List of Student who play neither Cricket nor Badminton F-C-B:", diff(f_c, b))
        print("Number of Student who play neither Cricket nor Badminton F-C-B:", len(diff(f_c, b)))
    elif choice==4:
        cuf=union_set(c,f)
        print("List of Student who play neither Cricket nor Badminton F-C-B:", diff(cuf, b))
        print("Number of student who play cricket and football but not badminton:", len(diff(cuf, b)))
    print()

    while(1):                         #Exceptional Handling for YES
        try:
            yes=int(input("""Are you Want to Continue to with this Data? Press (1/0)"""))
            if (yes==1 or yes==0):
                break
            print("Wrong Choice")
            print()
        except ValueError:
            print("Press 1/0 <int>")
            print()

    if yes==1:
        print("""
        Here we are helping to find out the followed data using user provided data:
        1.List of student who play both Cricket and Badminton CUB
        2.List of student who play either Cricket or Badminton but not both CUB-CnB
        3.Number of Student who play neither Cricket nor Badminton F-C-B
        4.Number of student who play cricket and football but not badminton CUF-B
        """)
        continue
    else:
        print("Programme Exited")
        break











#A=Cricket
#B=Badminton
#C=Football

#list of student who play both Cricket and Badminton CUB
#List of student who play either C or B but not both CUB-CnB
#Number of Student who play neither C or B F-C-B
#number of student who play cricket and football but not badminton CUF-B


def set_common(a):    #remove Duplicate Entries
    result = []
    for i in range(len(a)):
        for j in result:
            if a[i] == j:
                break
        else:
            result.append(a[i])
    return result


def union_set(a , b):   #return Union of two lists
    union = []
    for i in a:
        union.append(i)
    for i in b:
        union.append(i)
    union = set_common(union)
    return union


def intersection(a , b):   #return intersection betn two lists
    result = []
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                result.append(a[i])
                break
    result = set_common(result)
    return result


def diff(a ,b):              #return difference of two sets
    inter = intersection(a , b)
    for i in inter:
        a.remove(i)
    a=set_common(a)
    return a

########################################### Data Entry Starts
c = []
b = []
f = []

l = int(input("Enter Number of Players Playing Cricket:"))
for i in range(l):
    temp=int(input("Enter the jersey number of player playing Cricket:"))
    c.append(temp)

m = int(input("Enter Number of Players Playing Badminton:"))
for i in range(m):
    temp=int(input("Enter the jersey number of player playing Badminton:"))
    b.append(temp)

n = int(input("Enter Number  of Players Playing Football:"))
for i in range(n):
    temp=int(input("Enter the jersey number of player playing Football :"))
    f.append(temp)

############################################ Data Entry Completed

print("""
Welcome to Class SE,
Here we are helping to find out the followed data using user provided data:
1.List of student who play both Cricket and Badminton CUB
2.List of student who play either Cricket or Badminton but not both CUB-CnB
3.Number of Student who play neither Cricket nor Badminton F-C-B
4.Number of student who play cricket and football but not badminton CUF-B
""")


yes=1
while(yes):
    while(1):                      # Exceptional Handling for Choices
        try:
            choice=int(input("Enter Choice between 1-4:"))
            if (choice>0 and choice<5):
                break
            print("<Wrong Choice>")
            print()
        except ValueError:
            print("Enter Correct Choice in <int> again")
            print()


    if choice==1:
        print("List of student who play both Cricket and Badminton:",union_set(c,b))
    elif choice==2:
        cub=union_set(c,b)
        cnb=intersection(c,b)
        print("List of student who play either Cricket or Badminton but not both:",diff(cub,cnb))
    elif choice==3:
        f_c=diff(f,c)
        print("List of Student who play neither Cricket nor Badminton F-C-B:", diff(f_c, b))
        print("Number of Student who play neither Cricket nor Badminton F-C-B:", len(diff(f_c, b)))
    elif choice==4:
        cuf=union_set(c,f)
        print("List of Student who play neither Cricket nor Badminton F-C-B:", diff(cuf, b))
        print("Number of student who play cricket and football but not badminton:", len(diff(cuf, b)))
    print()

    while(1):                         #Exceptional Handling for YES
        try:
            yes=int(input("""Are you Want to Continue to with this Data? Press (1/0)"""))
            if (yes==1 or yes==0):
                break
            print("Wrong Choice")
            print()
        except ValueError:
            print("Press 1/0 <int>")
            print()

    if yes==1:
        print("""
        Here we are helping to find out the followed data using user provided data:
        1.List of student who play both Cricket and Badminton CUB
        2.List of student who play either Cricket or Badminton but not both CUB-CnB
        3.Number of Student who play neither Cricket nor Badminton F-C-B
        4.Number of student who play cricket and football but not badminton CUF-B
        """)
        continue
    else:
        print("Programme Exited")
        break











#A=Cricket
#B=Badminton
#C=Football

#list of student who play both Cricket and Badminton CUB
#List of student who play either C or B but not both CUB-CnB
#Number of Student who play neither C or B F-C-B
#number of student who play cricket and football but not badminton CUF-B


def set_common(a):    #remove Duplicate Entries
    result = []
    for i in range(len(a)):
        for j in result:
            if a[i] == j:
                break
        else:
            result.append(a[i])
    return result


def union_set(a , b):   #return Union of two lists
    union = []
    for i in a:
        union.append(i)
    for i in b:
        union.append(i)
    union = set_common(union)
    return union


def intersection(a , b):   #return intersection betn two lists
    result = []
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                result.append(a[i])
                break
    result = set_common(result)
    return result


def diff(a ,b):              #return difference of two sets
    inter = intersection(a , b)
    for i in inter:
        a.remove(i)
    a=set_common(a)
    return a

########################################### Data Entry Starts
c = []
b = []
f = []

l = int(input("Enter Number of Players Playing Cricket:"))
for i in range(l):
    temp=int(input("Enter the jersey number of player playing Cricket:"))
    c.append(temp)

m = int(input("Enter Number of Players Playing Badminton:"))
for i in range(m):
    temp=int(input("Enter the jersey number of player playing Badminton:"))
    b.append(temp)

n = int(input("Enter Number  of Players Playing Football:"))
for i in range(n):
    temp=int(input("Enter the jersey number of player playing Football :"))
    f.append(temp)

############################################ Data Entry Completed

print("""
Welcome to Class SE,
Here we are helping to find out the followed data using user provided data:
1.List of student who play both Cricket and Badminton CUB
2.List of student who play either Cricket or Badminton but not both CUB-CnB
3.Number of Student who play neither Cricket nor Badminton F-C-B
4.Number of student who play cricket and football but not badminton CUF-B
""")


yes=1
while(yes):
    while(1):                      # Exceptional Handling for Choices
        try:
            choice=int(input("Enter Choice between 1-4:"))
            if (choice>0 and choice<5):
                break
            print("<Wrong Choice>")
            print()
        except ValueError:
            print("Enter Correct Choice in <int> again")
            print()


    if choice==1:
        print("List of student who play both Cricket and Badminton:",union_set(c,b))
    elif choice==2:
        cub=union_set(c,b)
        cnb=intersection(c,b)
        print("List of student who play either Cricket or Badminton but not both:",diff(cub,cnb))
    elif choice==3:
        f_c=diff(f,c)
        print("List of Student who play neither Cricket nor Badminton F-C-B:", diff(f_c, b))
        print("Number of Student who play neither Cricket nor Badminton F-C-B:", len(diff(f_c, b)))
    elif choice==4:
        cuf=union_set(c,f)
        print("List of Student who play neither Cricket nor Badminton F-C-B:", diff(cuf, b))
        print("Number of student who play cricket and football but not badminton:", len(diff(cuf, b)))
    print()

    while(1):                         #Exceptional Handling for YES
        try:
            yes=int(input("""Are you Want to Continue to with this Data? Press (1/0)"""))
            if (yes==1 or yes==0):
                break
            print("Wrong Choice")
            print()
        except ValueError:
            print("Press 1/0 <int>")
            print()

    if yes==1:
        print("""
        Here we are helping to find out the followed data using user provided data:
        1.List of student who play both Cricket and Badminton CUB
        2.List of student who play either Cricket or Badminton but not both CUB-CnB
        3.Number of Student who play neither Cricket nor Badminton F-C-B
        4.Number of student who play cricket and football but not badminton CUF-B
        """)
        continue
    else:
        print("Programme Exited")
        break











