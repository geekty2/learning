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

ENTER_BD = {
    "ЧК": "UPDATE newschema2.kurs SET `kurs` = `kurs` + 1 WHERE `pib` = {pib};",
    "ДК": "UPDATE newschema2.kurs SET `kurs` = `kurs` + 1 WHERE `pib` = {pib};",
    "ДЖГ": "UPDATE newschema2.kurs SET `kurs` = `kurs` + 1 WHERE `pib` = {pib};",
    "ЧНК": "UPDATE newschema2.kurs SET `nk` = `nk` + 1 WHERE `pib` = {pib};",
    "ПЧНК": "UPDATE newschema2.kurs SET `nk` = `nk` + 1 WHERE `pib` = {pib};",
    "Ст.ЧП": "UPDATE newschema2.kurs SET `chepe` = `chepe` + 1 WHERE `pib` = {pib};",
    "ЧП": "UPDATE newschema2.kurs SET `chepe` = `chepe` + 1 WHERE `pib` = {pib};"
}
