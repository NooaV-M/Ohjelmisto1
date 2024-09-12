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

area_input = input("Enter area code: ")

#closed
#large_airport
#medium_airport
#small_airport
#heliport
def airport_list_get(airport_type, area_code):
    sql = f"SELECT * FROM airport WHERE type = '{airport_type}' AND iso_country = '{area_code}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    return cursor.fetchall()

#print(airport_list_get("large_airport", area_input))

large_airports = len(airport_list_get("large_airport", area_input))
medium_airports = len(airport_list_get("medium_airport", area_input))
small_airports = len(airport_list_get("small_airport", area_input))
heliports = len(airport_list_get("heliport", area_input))
closed = len(airport_list_get("closed", area_input))

print(f"In area code {area_input} there are\n{large_airports} large airports\n{medium_airports} medium airports\n{small_airports} small airports\n{heliports} heliports\nand {closed} closed airports")