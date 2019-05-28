

c=input("Change owed: ")
if c<0:
    c=get_int("Change owed: ")
cash=(c*100)
counter1=cash//25
cash=cash-(counter1*25)
counter2=cash//10
cash=cash-(counter2*10)
counter3=cash//5
cash=cash-(counter3*5)
counter4=cash//1
counter=counter1+counter2+counter3+counter4
print(counter)