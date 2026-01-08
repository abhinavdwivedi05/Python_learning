x= "      sid is ver rich      "

#slicing string
print(x[:3])

# modifing string
print(x.strip())
print(x.replace("i","1234"))
b=x.strip()
a=b.split(" ")
print(type(a))
print(a)

#placeholder
price=49
txt=f"the price is {price} dollars"
print(txt)

#string methods
number=x.count("i")
print(number)
print(x.find("ver"))


k=input()
y= k in x
if(y == True):
    print("present") 