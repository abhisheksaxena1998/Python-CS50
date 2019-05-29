from sys import argv


def main():
    newarr=[]
    lengtharr=[]
    p=len(argv)
    ban=[]
    f = open("banned.txt", "a")
    f.write("cat\n")
    f.write("dog\n")
    f.close()
    if p<2 or p>2:
        print ("Usage: python caesar.py k")
        exit (1)
    print ("What message would you like to censor?")
    m=input()
    k=m.split(" ")
    f=open("banned.txt","rt")
    for x in f:
        ban.append(x.rstrip('\n'))
    length1=len(k)
    length2=len(ban)
    for elements in k:
        lengtharr.append(len(elements))
    for i in range(length1):
        for j in range (length2):
            if (k[i].lower()==ban[j] ):
                k[i]="*"*lengtharr[i]

    #print (k)
    x = " ".join(k)
    print(x)
    f.close


if __name__ == "__main__":
    main()
