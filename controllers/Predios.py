from flask import jsonify, request
from db.db import cnx

class Predio():
    global cur
    cur = cnx.cursor()

    def list(self): 
        lista = []
        cur.execute("SELECT * FROM predio")
        rows = cur.fetchall()
        columns =[i[0] for i in cur.description]
        for row in rows:
            registro = zip(columns, row)
            json = dict(registro)
            lista.append(json)
        return jsonify(lista)
        cnx.close

    def create(self, body):
        data = (body['codigo'],body['latitud'],body['longitud'],body['terreno'],body['area'])
        sql = "INSERT INTO predio(codigo, latitud, longitud, terreno, area) VALUES(%s, %s, %s, %s, %s)"
        cur.execute(sql, data)
        cnx.commit()
        return {'estado': "Insertado"}, 200