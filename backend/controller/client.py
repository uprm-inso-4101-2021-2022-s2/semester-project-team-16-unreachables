from flask import jsonify
from DAOs import client
from utils import macros

class ClientController:
    '''
    Help on the Client Controller Object
    TODO: Document
    '''

    def build_map_dic(self, row):
        result = {}
        result['id'] = row[0]
        result['user_id'] = row[1]
        result['geolocation'] = row[2]
        result['fname'] = row[3]
        result['lname'] = row[4]
        result['email'] = row[5]
        result['uname'] = row[6]
        result['pword'] = row[7]
        result['uage'] = row[8]
        result['gender'] = row[9]
        result['phone'] = row[10]
        result['address'] = row[11]
        result['created'] = row[12]
        return result


    def __build_attr_dic(self, id, user_id, geoloc):
        result = {}
        result['id'] = id
        result['user_id'] = user_id
        result['geoloc'] = geoloc
        return result


    def get(self):
        try:
            dao = client.ClientDAO()
            query = dao.get()
            result_list = []
            for row in query:
                obj = self.build_map_dic(row)
                result_list.append(obj)
            return jsonify(Clients = result_list), macros.OK
        except:
            return jsonify(macros.CLIENT_ERROR), macros.NOT_FOUND


    def get_by_id(self, id):
        try:
            dao = client.ClientDAO()
            query = dao.get_by_id(id)
            result = self.build_map_dic(query)
            return jsonify(Client=result), macros.OK
        except:
            return jsonify(macros.CLIENT_DNE), macros.NOT_FOUND
    

    def get_by_uname(self, uname):
        try:
            dao = client.ClientDAO()
            query = dao.get_by_uname(uname)
            result = self.build_map_dic(query)
            return jsonify(Client=result), macros.OK
        except:
            return jsonify(macros.CLIENT_DNE), macros.NOT_FOUND


    def get_by_email(self, email):
        try:
            dao = client.ClientDAO()
            query = dao.get_by_email(email)
            result = self.build_map_dic(query)
            return jsonify(Client=result), macros.OK
        except:
            return jsonify(macros.USR_DNE), macros.NOT_FOUND