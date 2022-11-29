from flask import Flask, request, jsonify
import mysql.connector
app = Flask(__name__)

@app.route('/cree/user', methods=['POST'])
def creeUser():
    mydb = mysql.connector.connect(user='root',
                                   password="root",
                                   host="localhost",
                                   port=3306,
                                   database="project")


    mycursor = mydb.cursor()

    req_Json = request.json
    stid = req_Json['id']
    stname = req_Json['name']
    stsurname = req_Json['lastname']


    try:
        sql = "INSERT INTO users (id, name, lastname) VALUES (%s, %s, %s)"
        val = (stid, stname,stsurname)
        mycursor.execute(sql, val)
        mydb.commit()
        id = mycursor.lastrowid
        return jsonify({"message": "User inserted successed with id: " + str(id) })

    except Exception as e:

        mydb.rollback()
        mydb.close()
        return jsonify({"message": str(e)})


if __name__ == '__main__':
    app.run(debug=True, port=5050)


