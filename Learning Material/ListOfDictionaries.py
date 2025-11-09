#Cach dung list of dictionaries

ENT303 = [
    {"ho" : "Nguyen", "dem" : "Huu", "ten" : "Duyen"},
    {"ho" : "Pham", "dem" : "Hong", "ten" : "Ha"},
    {"ho" : "Le", "dem": "Quoc", "ten": "Thai"}
]

for student in ENT303:
    print(student["ho"], student["dem"], student["ten"], sep=", ")