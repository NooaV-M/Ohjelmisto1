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

ICAO_input = input("Enter ICAO code:")

def airportget(ICAO_code):
    sql = f"SELECT name, municipality FROM airport WHERE ident = '{ICAO_code}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

fetch_result = airportget(ICAO_input)

if fetch_result:
    print(f"{fetch_result[0][0]}, in {fetch_result[0][1]}")
else:
    print("Invalid ICAO code")