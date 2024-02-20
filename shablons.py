scheme = {
    "get_sergant": "SELECT * FROM newschema2.kurs WHERE `rank` = 'с-т';",
    "get_kursant_boy": "SELECT * FROM newschema2.kurs WHERE `rank` = 'сол.' AND `sex` = 'Чоловік';",
    "get_girl": "SELECT * FROM newschema2.kurs WHERE `rank` = 'сол.' AND `sex` = 'Жінка';"
}

big_naryad = {
    "ЧК": (1, "get_sergant"),
    "ДК": (2, "get_kursant_boy"),
    "ДЖГ": (1, "get_girl"),
    "ЧНК": (1, "get_sergant"),
    "ПЧНК": (3, "get_kursant_boy"),
    "Ст.ЧП": (1, "get_kursant_boy"),
    "ЧП": (9, "get_kursant_boy")
}
small_naryad = {
    "ЧК": (1, "get_sergant"),
    "ДК": (2, "get_kursant_boy"),
    "ДЖГ": (1, "get_girl")
}

DATA_COURCES = {  # день великих нарядів
    "19.02": "C0",
    "20.02": "C1",
    "21.02": "C2",
    "22.02": "C0",
    "23.02": "C1",
    "24.02": "C2",
    "25.02": "MK"
}


# def main_algoritm():
#     # cursor.execute(scheme["get_kursant_boy"])
#     # m = cursor.fetchall()
#     for course in DATA_COURCES.items():
#         if course[1] == "C1":
#             for position in big_naryad.items():
#                 for i in range(position[1][0]):
#                     cursor.execute(scheme[position[1][1]])
#                     temp = cursor.fetchone()
#                     slow[position[0]] = temp
#     for i in slow.items():
#         print(i)
# main_algoritm()
