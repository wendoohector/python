print("Wendel Hector\n\n\n")
 #Premye pati
# nimero 1
# chen_karakte = input("Antre yon fraz avek majiskil: ")
# print("Chen nan an miniskil net:"+chen_karakte.lower())

# # #nimero 2
# chen = input("Antre yon chen karakte: ")
# b = chen.split()
# print(b)

# #nimero 3
# chen_ti = input("Antre yon chen: ")
# d = chen_ti.title()
# print(d)

# #nimero 4
# teks = input("Antre yon text: ")
# delimite = teks.split()
# nouvo = " "
# for mo in delimite:
#      premye = mo[0]
#      nouvo +=premye
# print("["+nouvo+"]")

# #nimero 5
# chen_karakte = input("Antre yon chen: ")
# ansyen = 'a'
# nouvo = '@'
# nouvo_chenn = " "
# for let in chen_karakte:
#     if let == ansyen:
#         nouvo_chenn += nouvo
#     else: nouvo_chenn += let
# print(nouvo_chenn)


#nimero 6
# c_k = input ("Antre yon chenn karakte: ")
# n_c = c_k[:: -1].upper()
# print(n_c)

#nimero 7
# antre = input("Antre yon chenn ki gn plizye <a> ladanl: ")
# karak = 'a'
# endis = -1
# endis = antre.find(karak)
# if endis != -1:
#     print(endis)
# else: print("karakte sa pa nan chenn nan")

#nimero 8
# antre_chen = input("antre yon chen ki gen <a> ladanl: ")
# karak = 'a'
# som = 0
# for e, karakte in enumerate(antre_chen):
#     if karakte.lower() == karak:
#         som +=e
# print(som)

#nimero 9
# Vf = input("Antre yon chen ki gn karakte <a> ladanl: ")
# lis = [ ]

# for w, ka in enumerate(Vf):
#     if ka == 'a':
#         lis.append(w)
# print(lis)

#nimero 10
# fg = input(" Antre yon chen karakte: ")
# vb = fg.replace(" ","")
# kt = len(vb)
# print(vb,kt)


#Pati 2:

#nimero 1
# n = 1000
# lis_d = [ ]
# for i in range (n+1):
#     if i%2==0:
#         lis_d.append(i)
# print(lis_d)

#nimero 2

# lis_a = [ ]
# n = int(input("konyen eleman wap antre: "))
# for i in range(n):
#     el = input(f"Antre eleman {i+1}: ")
#     lis_a.append(el)
#     lis_c = [str(eleman) for eleman in lis_a]
#     print(lis_c)

#nimero 3
# lis_ch = [ ]
# d = input("Antre yon ansanm chen karakte: ")
# w=d.upper()
# s= w.split()
# for f in s:
#     lis_ch.append(f)
# print(lis_ch)

#nimero 4
lis_antye = [ ]
nouvo_lis = [ ]
q = int(input("Konbyen eleman wap antre nan lis la: "))
for h in range(q):
    tu = input(f"Antre eleman {h+1}: ")
    lis_antye.append(tu)
    
for a, div in enumerate(lis_antye):
    if a % 3 == 0:
        nouvo_lis.append(div)
print(nouvo_lis)




