class String:
    def __init__(self,s):
        self.string=s
        self.len=0
        self.wd_list=[]
        self.wd_list_len=0
        self.occur_list=[]
        self.long_wd=[]
        self.substring_index=0
        self.length()
        self.str_word()
        self.occur()

    def length(self):
        str1=self.string
        while(1):
            if str1=="":
                return
            else:
                str1=str1[1:]
                self.len+=1

    def str_word(self):
        wd = ""
        cnt=0
        temp=0
        for i in range(self.len):
            if self.string[i]==" " or i==self.len-1:
                if i==self.len-1:
                    wd+=self.string[i]
                    temp+=1
                if wd==" ":
                    wd=""
                    temp=0
                    continue
                self.wd_list.append(wd)
                if (cnt<=temp):
                    if cnt!=temp:
                        self.long_wd.clear()
                    if wd not in self.long_wd:
                        self.long_wd.append(wd)
                    cnt=temp
                self.wd_list_len+=1
                wd=""
                temp=0
            else:
                wd+=self.string[i]
                temp+=1
        return 0


    def occur(self):
        temp=self.wd_list.copy()
        l1=[]
        cnt=0
        for i in range(self.wd_list_len):
            if temp[i]=="":
                continue
            l1.append(temp[i])
            print(temp[i])
            cnt=0
            for j in range(self.wd_list_len):
                if temp[i]==temp[j]:
                    cnt+=1
                    if i!=j:
                        temp[j]=""
            else:
                l1.append(cnt)
                self.occur_list.append(l1)
                l1=[]
        return 0

    def palindrome(self):
        i=0
        j=self.len-1
        while(i<=j):
            if self.string[i]==self.string[j]:
                i+=1
                j-=1
                continue
            else:
                return 0
        return 1

    def substring(self,sub):
        for i in range(self.len):
            if self.len-i<String.length_static(sub):
                self.substring_index = -1
                return
            if self.string[i:i+String.length_static(sub)]==sub:
                self.substring_index= i
                return

    def char_occur(self,char):
        cnt=0
        for i in self.string:
            if i==char:
                cnt+=1
        else:
            return cnt

    @staticmethod
    def length_static(string):
        str1 = string
        len=0
        while (1):
            if str1 == "":
                return len
            else:
                str1 = str1[1:]
                len += 1


str1=String(input("Enter the String:"))

while(1):
    print("""
    Welcome,
    1.To display word with the longest length 
    2.To determines the frequency of occurrence of particular character in the String
    3.To check whether given string is palindrome or not 
    4.To display index of first appearance of the substring
    5.To count the occurrences of each word in a given string
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
        print("List of words with Longest Length:",str1.long_wd)
    elif choice==2:
        c=input("Enter The Character :")
        print("Frequency of occurrence of particular character in the:",str1.char_occur(c))
    elif choice==3:
        condn=str1.palindrome()
        print(condn)
        if (condn):
            msg="YES"
        else:
            msg="NO"
        print("Whether given string is palindrome or not:", msg)
    elif choice==4:
        str1.substring(input("Enter The Substring:"))
        print("Index of first appearance of the substring", str1.substring_index)
    elif choice==5:
        print("Count of the occurrences of each word in a given string", str1.occur_list)
    elif choice==6:
        break
    print()

