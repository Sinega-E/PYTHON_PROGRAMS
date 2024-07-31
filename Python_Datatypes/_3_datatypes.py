#once the assigned a value,
#it cannot be replaced
#but the new value is stored in a new location/memory.

#no fixed size of memory for int datatype

#INTEGER DATATYPE
a=124
a=200
print(a)

#FLOAT DATATYPE
b=5e2 #e/E=10
c=6E3
d=4e-4
e=3E-2
print(b)
print(c)
print(d)
print(e)
print(a.__sizeof__())
print(b.__sizeof__())
print(c.__sizeof__())
print(d.__sizeof__())
print(e.__sizeof__())

#BOOLEAN DATATYPE
ab=True
ac=False
print(ab)
print(ac)

#COMPLEX NUMBERS
ad=6+7j # j is complex number
y=complex(ad)

print(y)
print(ad.real)
print(ad.imag)

#LITERALS--->direct data / value written in the program
#int
u=125
v=123,423 #will be considered as tuples
print(v)
w=123_423 # for easy understanding
print(w)  # "_" can be used only between digits

#float
q=2.45_3 # "_" cannot be used before or after "."
print(q)

#complex
e=5_23 + 4j
print(e)
str1="hello"
str2='how are you?'
str3='e' #not a character but it is a string
print(str1)
print(str2)
print(str3)