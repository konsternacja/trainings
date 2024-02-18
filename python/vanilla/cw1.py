#!/usr/bin/env python3
# cw1
print('Hello World')

# cw2
seq = 'ATGCATATGACTCAATGCCCATTAAAAA'

total = len(seq)

gc = seq.count('GC')

gc_content = gc/total

print(f"The GC content in this sequence is {gc_content:.1}")

# cw3
txt = 'Kocham Pythona kocham go cały dzień i noc'

drip_txt = txt.replace(' ', 'joł')

print(drip_txt)

# cw4
imie = input('Podaj imie mordeczko: ')
nazwisko = input('Teraz nazwisko: ')


email = str(imie.lower()+'.'+nazwisko.lower()+'@student.uj.edu.pl')

print(email)

# cw5
names_list = ["Dill Doe", "Chris P. Bacon", "Ben Dover"]

names_list.append("Harry Dixon")

b = input("Podaję imię: ")

if b in names_list:
    print(b)
