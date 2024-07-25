def findpass(s):
    grp=""
    minlen=len(s)
    for x in range(len(s)):
        if (s[x]!="@" and s[x]!="$"):
            grp=grp + s[x]
        # elif(s[x]=="@" or s[x]=="$"):
        #     grp=""
        elif(grp!=""):
            print("Monster!")
            print(grp)
            if (minlen>len(grp)):
                minlen = len(grp)
                grp=""
    print(minlen)
    return minlen
        



s = input("gg mofo: ")
print(s)
findpass(s)