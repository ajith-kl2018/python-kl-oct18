# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 20:57:12 2018

@author: shirley.ng
"""

from flask import Flask, render_template, json, request
from flaskext.mysql import MySQL
import logging
from logging.handlers import RotatingFileHandler
from flask_restful import reqparse, abort, Api, Resource

mysql = MySQL()
app = Flask(__name__)
api = Api(app)

# MySQL configurations
"""
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Shir0725'
app.config['MYSQL_DATABASE_DB'] = 'company'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
"""
# MySQL configurations - Ajith PC
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'sqlADMIN321'
app.config['MYSQL_DATABASE_DB'] = 'BucketList'
#app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_HOST'] = '10.211.55.3'

mysql.init_app(app)


#def abort_if_todo_doesnt_exist(cus_code):
#    if todo_id not in TODOS:
#        abort(404, message="Todo {} doesn't exist".format(todo_id))

def selectCustomer(cus_code) :

    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        sqlQuery = "select cus_lname from customer where cus_code="+cus_code

        print("SQL Query:", sqlQuery)
        app.logger.warning("SQL Query:"+str(sqlQuery))

        cursor.execute(sqlQuery)
        data = cursor.fetchall()

        if len(data) is 0:
                
                #return json.dumps({'message':'User created successfully ! </p> <a href=http://127.0.0.1:725/> Back to Home </a></p>'})

                return json.dumps(data)
        else:
            return json.dumps({'error': str(data[0])})

    except Exception as e:
        app.logger.error('An error occurred' + str(e))
        return json.dumps({'error': str(e)})
    finally:
        cursor.close()
        conn.close()


def deleteCustomer(cus_code):

    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        sqlQuery = "delete from customer where cus_code="+cus_code

        print("SQL Query:", sqlQuery)
        app.logger.warning("SQL Query:"+str(sqlQuery))

        cursor.execute(sqlQuery)
        data = cursor.fetchall()

        if len(data) is 0:
                conn.commit()
                #return json.dumps({'message':'User created successfully ! </p> <a href=http://127.0.0.1:725/> Back to Home </a></p>'})

                return json.dumps({'message': 'User deleted successfully !'})
        else:
            return json.dumps({'error': str(data[0])})

    except Exception as e:
        app.logger.error('An error occurred' + str(e))
        return json.dumps({'error': str(e)})
    finally:
        cursor.close()
        conn.close()

def putCustomer(cus_code, cus_lname, cus_fname, cus_initial, cus_areacode, cus_phone, cus_balance):
 
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        sqlQuery = "insert into customer values(" + _cus_code + ",'" + _cus_lname + "','" + _cus_fname + \
            "','" + _cus_initial + "','" + _cus_areacode + \
            "','" + _cus_phone + "','" + _cus_balance + "')"

        print("SQL Query:", sqlQuery)
        app.logger.warning("SQL Query:"+str(sqlQuery))

        cursor.execute(sqlQuery)
        data = cursor.fetchall()
        if len(data) is 0:
                conn.commit()
                #return json.dumps({'message':'User created successfully ! </p> <a href=http://127.0.0.1:725/> Back to Home </a></p>'})
                
                return json.dumps({'message': 'User created successfully !'})
        else:
            return json.dumps({'error':str(data[0])})


    except Exception as e:
        app.logger.error('An error occurred' + str(e))
        return json.dumps({'error': str(e)})
    finally:
        cursor.close()
        conn.close()



#parser = reqparse.RequestParser()
#parser.add_argument('task')

# customer
#   show a single todo item and lets you delete them


class customer(Resource):
    def get(self, cus_code):
        #abort_if_todo_doesnt_exist(cus_code)
        
        return selectCustomer(cus_code)

    def delete(self, cus_code):
        #abort_if_todo_doesnt_exist(cus_code)
        #del TODOS[cus_code]
        return deleteCustomer(cus_code), 204

    def put(self, cus_code):
        #_cus_code = request.form['cus_code']
        _cus_lname = request.form['cus_lname']
        _cus_fname = request.form['cus_fname']
        _cus_initial = request.form['cus_initial']
        _cus_areacode = request.form['cus_areacode']
        _cus_phone = request.form['cus_phone']
        _cus_balance = request.form['cus_balance']

        #args = parser.parse_args()
        #task = {'task': args['task']}

        return putCustomer(_cus_code, _cus_lname, _cus_fname, _cus_initial, _cus_areacode, _cus_phone, _cus_balance), 201


api.add_resource(customer, '/<string:cus_code>')

if __name__ == "__main__":
    handler = RotatingFileHandler('apperror.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    #app.run(port=725)
    app.run(debug=True)
