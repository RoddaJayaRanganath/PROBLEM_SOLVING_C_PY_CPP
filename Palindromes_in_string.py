string = input("enter string : ")
for i in range(len(string)):
    newlist=[]
    for j in range(i,len(string)):
        newlist.append(string[j])
        if len(newlist) > 1:
            #palindrome check;
            if(newlist == newlist[::-1]):
                #printing palindromes;
                print("".join(newlist))
        
