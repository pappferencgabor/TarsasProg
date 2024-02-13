with open("dobasok.txt") as file: dobasok = [line.replace(" ", "").rstrip() for line in file][0]
with open("osvenyek.txt") as file: osvenyek = [line.rstrip() for line in file]

print("\n2. feladat")
print(f"A dobások száma: {len(dobasok)}")
print(f"Az ösvények száma: {len(osvenyek)}")

print("\n3. feladat")

osvSort = sorted(osvenyek, key=lambda x: len(x), reverse=True)
szamlalo = 0
for i in osvenyek:
    if len(i) == len(osvSort[0]):
        print(f"Az egyik leghosszabb a(z) {szamlalo+1}. ösvény, hossza: {len(i)}")
        break
    szamlalo += 1

print("\n4. feladat")
sorszam = int(input("Adja meg egy ösvény sorszámát! "))
jatekosok = int(input("Adja meg a játékosok számát! "))

hiba = False
if sorszam < 0 or sorszam > len(osvenyek)-1:
    print("Hibásan adtad meg az ösvény sorszámát!")
    hiba = True
if jatekosok < 2 or jatekosok > 5:
    print("A játékot legalább 2, legfeljebb 5 játékos játszhatja!")
    hiba = True

if hiba:
    exit()

print("\n5. feladat")
stats = { "M": 0, "V": 0, "E": 0 }

if sorszam > -1 and sorszam < len(osvenyek) - 1:
    for i in osvenyek[sorszam]:
        stats[i] += 1
for v, k in stats.items(): print(f"{v}: {k} darab")

# 6. feladat
lines = ""
for i in range(len(osvenyek[sorszam])):
    if osvenyek[sorszam][i] == "E" or osvenyek[sorszam][i] == "V":
        lines += f"{i}\t{osvenyek[sorszam][i]}\n"
with open("kulonleges.txt", "w", encoding="utf-8") as file: file.write(lines)
file.close()

print("\n7. feladat - HIBÁS")
jatekosoklista = [0 for i in range(jatekosok)]
jelenlegi = 0
kor = 0
for i in dobasok:
    jatekosoklista[jelenlegi] += int(i)
 
    jelenlegi += 1
    if jelenlegi == jatekosok: 
        jelenlegi = 0
        kor += 1
 
jatrend = [i for i in sorted(jatekosoklista)]
print(f"A játék a(z) {int((kor - jatrend[-1]))}. körben fejeződött be. A legtávolabb jutó(k) sorszáma: {jatekosoklista.index(jatrend[-1])+1}")

print("\n8. feladat - HIBÁS")
"""jatekosokstat = {}
sorrend = []

for i in range(1, jatekosok+1): jatekosokstat[f'Player{i}'] = 0
jelenlegi = 1

for i in dobasok:
    jatekosokstat[f'Player{jelenlegi}'] += int(i)
 
    jelenlegimezo = jatekosokstat[f'Player{jelenlegi}']
    print(jelenlegimezo)
 
    if jelenlegimezo >= len(osvenyek[sorszam])-1:
        jatekosok -= 1
        sorrend.append(f"{jelenlegi}-{jelenlegimezo}")
        del jatekosokstat[f'Player{jelenlegi}']
    else:
        if osvenyek[sorszam][jelenlegimezo] == "M": jatekosokstat[f'Player{jelenlegi}'] = jelenlegimezo
        elif osvenyek[sorszam][jelenlegimezo] == "E": jatekosokstat[f'Player{jelenlegi}'] = jelenlegimezo + int(i)
        elif osvenyek[sorszam][jelenlegimezo] == "V": jatekosokstat[f'Player{jelenlegi}'] = jelenlegimezo - int(i)
 
    jelenlegi += 1
    if jelenlegi > jatekosok: jelenlegi = 1"""