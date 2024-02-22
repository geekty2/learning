import pymysql
from pprint import PrettyPrinter
from setup import host, port, user, password, database
from shablons import scheme, big_naryad, small_naryad, DATA_COURCES, ENTER_BD
import pprint

pp = PrettyPrinter
assigned = []

result = {}


def assign_naryad(date, data_sources, big_naryad, small_naryad, scheme):
    naryad_set = big_naryad if data_sources.get(date) == "C1" else small_naryad
    try:
        connection = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database)

        with connection.cursor() as cursor:

            for position, value in naryad_set.items():
                count, query_key = value

                cursor.execute(scheme[query_key])
                candidates = list(cursor.fetchall())
                filtered_candidates = [c for c in candidates if c[0] not in assigned]
                filtered_candidates.sort(key=lambda x: x[4])
                selected = filtered_candidates[:count]

                assigned.extend([s[0] for s in selected])

                result[position] = tuple([s[0] for s in selected])

            return result

    except Exception as e:
        print(e)
    finally:
        if connection:
            connection.close()


def write_bd(rewult: dict, enter_bd):
    try:
        connection = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database)

        with connection.cursor() as cursor:
            for N, NAME in rewult.items():
                cursor.execute(enter_bd[N].format(pib=NAME).replace(",", ""))
            return cursor.fetchall()

    except Exception as e:
        print(e)
    finally:
        if connection:
            connection.close()


print(assign_naryad("19.02", DATA_COURCES, big_naryad, small_naryad, scheme))
print(assigned)
print(write_bd(result, ENTER_BD))
print(assign_naryad("20.02", DATA_COURCES, big_naryad, small_naryad, scheme))
print(assigned)
