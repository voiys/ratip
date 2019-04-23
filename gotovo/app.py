"""
rjecnik = {
	'ovo': 'zamjenica',
	'je': 'glagol',
	'obrada': 'imenica',
	'jezika': 'imenica',
	'pomoću': 'prijedlog',
	'Pythona': 'imenica'
}
while True:
	pitanje = input('Unesi novu rijec u rjecnik\n Unesi "da" ili "ne"\n')
	
	if pitanje in ('da', 'Da', 'd', ''):
		kategorija = input('Unesi vrstu rijeci:\n')
		nova_rijec = input('Unesi novu rijec:\n')
		rjecnik[nova_rijec] = kategorija
	else:
		print(rjecnik)
		break

print(rjecnik)
print(len(rjecnik))
print(rjecnik['jezika'])


pretvoreno = ' '.join([str(x) for x in [5, 'kg', 'jabuka', 'kosta', 10, '$']])
print(pretvoreno)
"""
with open('korpus.txt') as korpus:
	countries = {}
	for line in korpus:
		country = line.split('|')[4]
		if country in countries:
			countries[country] += 1
		else:
			countries[country] = 1
	
	for key, value in sorted(countries.items(), reverse=True, key=lambda n: n[1]):
		print(f'{key:25} ==> {value:5}')
"""
import math

print(math.sqrt(2))

print(math.exp(3))

print(math.pow(3, 3))

br_dec = 20

print("pi na 20 decimala je %.20f" %math.pi)

nova = [element + 2 for element in range(1,5)]

def dodaj2(broj):
	return broj + 2
	
rezultat = list(map(lambda broj: broj+2, range(1,5)))




if __name__ == '__main__':
			for element in nova:
				print(element)
			rez = list(map(dodaj2, range(1, 5)))
			print(rez)
			print(rezultat)
			for x in range(1, 11):
				print("{0:2d} {1:3d} {2:4d}".format(x, x*x, x*x*x)) #oblik brojeva ovisno o broju znamenki
			while True:
				red = int(input("Unesi neki broj: "))
				for i in range(1, red+1):
					for j in range(1, red+1):
						print(i, "*", j, "=", i*j)
				if red == 10:
					quit()
			"""
