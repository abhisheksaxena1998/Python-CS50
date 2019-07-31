thislist=[]

k=[]
plaintext=input("plaintext: ")
l=len(plaintext)

arr=input("Enter the key")
la=len(arr)
div=l//la+1
print (div)

for i in range(la):
    k.append(ord(arr[i])-ord('a'))
a=[]
a=k*div
#print (a)    
shiftvalue=[]
shiftvalue=a
#for i in range(l):
    #shiftvalue[i]=a[i]
print (shiftvalue)    
#for z in range (len(plaintext)):
 #   shiftvalue[z]=k[i]
    
    
#k=int(input("Enter key"))

#print (k)
ciphertext=plaintext
l=len(plaintext)
#for z in range(l):
for i in range (l):
    a=plaintext[i]
    if a==' ' or a==',' or a=='!':
        thislist.append(a)
    elif a.isupper():
        b=chr(((ord(a)-65+shiftvalue[i])%26)+65) #append b to a new list.
        thislist.append (b)
    else :
        b=chr(((ord(a)-97+shiftvalue[i])%26)+97) #append b to a new list.
        thislist.append (b)
print ("ciphertext: ",end="")
for x in thislist:
    print (x,end="")
