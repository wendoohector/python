print("Wendel Hector\n\n\n")
# import random
# #Premye pati
# # nimero 1
# chen_karakte = input("Antre yon fraz avek majiskil: ")
# print("Chen nan an miniskil net:"+chen_karakte.lower())

# #nimero 2
# chen = input("Antre yon chen karakte: ")
# b = chen.split()
# print(b)

#nimero 3
# chen_ti = input("Antre yon chen: ")
# d = chen_ti.title()
# print(d)

#nimero 4
# teks = input("Antre yon text: ")
# delimite = teks.split()
# nouvo = " "
# for mo in delimite:
#     premye = mo[0]
#     nouvo +=premye
# print("["+nouvo+"]")

#nimero 5
chen_karakte = input("Antre yon chen: ")
ansyen = 'a'
nouvo = '@'
nouvo_chenn = " "
for let in chen_karakte:
    if let == ansyen:
        nouvo_chenn += nouvo
    else: nouvo_chenn += let
print(nouvo_chenn)


