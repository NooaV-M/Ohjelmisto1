import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="NOOA",
    password="1234",
    autocommit=True,
    collation='utf8mb4_general_ci'
)
from geopy import distance
print("Enter two airports to calculate distance")

ICAO_code1 = input("Enter ICAO code: ").upper()
ICAO_code2 = input("Enter ICAO code: ").upper()

def lat_long_get(ICAO_code):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{ICAO_code}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    return cursor.fetchall()

distance = distance.distance(lat_long_get(ICAO_code1), lat_long_get(ICAO_code2))

print(f"The two airports are\n{distance} apart")