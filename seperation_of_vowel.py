vowel=["a","e","i","o","u","A","E","I","O","U"]
user=input("Enter Your word:")
vow=[]
cons=[]
for ch in user:
    if ch in vowel:
        vow.append(ch)
    else:
        cons.append(ch)

v=''.join(vow) + ''.join(cons)


print(v)



