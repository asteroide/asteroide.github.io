#!/usr/bin/env python
"""Calculate the EBC of a beer

Usage:
	python3 get_ebc.py test
	python3 get_ebc.py malt1_or_ebc,weight1 malt2_or_ebc,weight2 ...

Examples:
	python3 get_ebc.py 6,90 300,10
	-> should give: 35.4
	python3 get_ebc.py 6,95 300,5
	-> should give: 20.7
	python3 get_ebc.py Vienna,90 "Special W",10
	-> should give: 35.4
"""


import sys

EBC = {
	"Vienna": 6,
	"Special W": 300,
	"Carawheat": 115,
	"Biscuit": 50
}

def calcul_ebc(ingredients):
	total_weight = 0
	total_ebc = 0
	for ingredient in ingredients:
		try:
			ingredient[0] = int(ingredient[0])
		except ValueError:
			pass
		if type(ingredient[0]) is int:
			total_ebc += ingredient[0]*int(ingredient[1])
			total_weight += int(ingredient[1])
		else:
			for _ebc in EBC:
				if ingredient[0].lower() == _ebc.lower():
					total_ebc += EBC[_ebc]*int(ingredient[1])
					total_weight += int(ingredient[1])
					break
			else:
				raise Exception(f"Cannot find {ingredient[0]} in database")
	return total_ebc/total_weight

def launch_test():
	data = (
		(6, ((6, 1),)),
		(6, (("Vienna", 1),)),
		(6, (("vienna", 1),)),
		(6, (("Vienna", 5),)),
		(35.4, ((6, 90), (300, 10),)),
		(35.4, (("Vienna", 90), ("Special W", 10),)),
	)
	for _d in data:
		print(f"{calcul_ebc(_d[1])} -> {_d[0]}")

if __name__ == "__main__":
	if "test" in sys.argv:
		launch_test()
	else: 
		ingredients = []
		for arg in sys.argv[1:]:
			ingredients.append(arg.split(","))
		print(calcul_ebc(ingredients))