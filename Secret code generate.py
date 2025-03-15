import random
import string


val=int(input("Enter 1 for code and 0 for decode: "))

if (val==1):
    st = input("Enter code: ")
    words=st.split(" ")
    nwrd=[]
    for word in words:
        if(len(word)>=3):
            ran1=''.join(random.choices(string.ascii_letters + string.digits,k=3))
            ran2=''.join(random.choices(string.ascii_letters + string.digits,k=3))
            # ran1="bhk"
            # ran2="ows"
            strn = ran1 + word[1:]+word[0] + ran2
            nwrd.append(strn)
        else:
            nwrd.append(word[::-1])
    print(" ".join(nwrd))

elif (val==0):
    st = input("Enter code: ")
    words=st.split(" ")
    nwrd=[]
    for word in words:
        if(len(word)>=3):
            # ran1="bhk"
            # ran2="ows"
            strn = word[-4]+word[3:-4]
            nwrd.append(strn)
        else:
            nwrd.append(word[::-1])
    print(" ".join(nwrd))
else:
    print("Error!")