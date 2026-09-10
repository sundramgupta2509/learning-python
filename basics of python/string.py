str1="Sundram"

str2="Gupta"

print(str1 + " " + str2)  # Sundram Gupta

print(len(str1))   # 7

print(len(str2))   # 5

# Position of letters.

str = "Antra Gupta"

print(str[2])   # t

print(str[5])   #    (space)

print(str[2:7])   # tra G

print(str[:5])   # Antra

print(str[2:])    # tra Gupta

print(str[6:8])   # Gu




x = "my self sundram"
print()
print(x.endswith("ram"))  # True
print()
print(x.capitalize())    # My self sundram
print()
print(x.replace("y", "o"))  # mo self sundram
print()
print(x.replace("self", "name"))   # my name sundram
print()
print("my self sundram".find("ndr"))   # 10
print()
print(x.find("self"))    # 3
print()
print("my name are sundram and my sur name are gupta.".replace("are", "is"))   # my name is sundram and my sur name is gupta. 
print()
print(x.count("s"))   # 2
print()