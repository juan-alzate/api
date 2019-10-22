import mysql.connector as mysql
cnx = mysql.MySQLConnection(
    host="db-server-evergreen-1.mysql.database.azure.com",
    port=3306,
    user="evergreenadmin@db-server-evergreen-1",
    password="1.evergreen",
    database="evergreen",
)