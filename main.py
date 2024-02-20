import pymysql
from pprint import PrettyPrinter
from setup import host, port, user, password, database
from shablons import scheme, big_naryad, small_naryad, DATA_COURCES
import pprint
pp = PrettyPrinter

def assign_naryad(date, data_sources, big_naryad, small_naryad, scheme):
    naryad_set = big_naryad if data_sources.get(date) == "C1" else small_naryad
    try:
        connection = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database)

        assigned = []
        result = {}

        with connection.cursor() as cursor:
            for position, value in naryad_set.items():
                # Адаптуємо код для обробки як big_naryad, так і small_naryad
                if isinstance(value, tuple):
                    count, query_key = value
                else:
                    count = value
                    query_key = position  # Припустимо, що в small_naryad ключі збігаються з потрібними query_key

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
result = ""
formatted_result = None
for i in DATA_COURCES.keys():
    print(i)
    result = assign_naryad(i, DATA_COURCES, big_naryad, small_naryad, scheme)
    print(result)



