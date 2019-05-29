from sys import argv
thislist=[]
p=len(argv)
if p<2:
    print ("Usage: python caesar.py k")
    exit (1)
k=int(argv[1])

shiftvalue=k%26
print (k)
plaintext=input("plaintext: ")
ciphertext=plaintext
l=len(plaintext)
for i in range (l):
    a=plaintext[i]
    if a==' ' or a==',' or a=='!':
       thislist.append(a)
    elif a.isupper():
        b=chr(((ord(a)-65+shiftvalue)%26)+65) #append b to a new list.
        thislist.append (b)
    else :
        b=chr(((ord(a)-97+shiftvalue)%26)+97) #append b to a new list.
        thislist.append (b)
print ("ciphertext: ",end="")
for x in thislist:
    print (x,end="")
print()
