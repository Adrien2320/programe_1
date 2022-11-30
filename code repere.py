my_empty_dict = {}

my_filled_dict = {"name": "Mertens", "surname": "Adrien"}

print(my_filled_dict["name"])

'rajouter au dictionnaire.'
my_filled_dict["age"] = 22

'affiche toute les clés juste les clés.'
print(my_filled_dict.keys())

'Affiche unique les valeurs dans le sens des clés'
print(my_filled_dict.values())

'affiche la clé et ensuite la valeur'
for key, value in my_filled_dict.items():
    print(f"La clé est {key} et la valeur est {value}")
