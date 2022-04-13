from flask import jsonify
from DAOs import user
from utils import macros

class UserController:

    def build_map_dic(self, row):
        result = {}
        result['id'] = row[0]
        result['fname'] = row[1]
        result['lname'] = row[2]
        result['email'] = row[3]
        result['uname'] = row[4]
        result['pword'] = row[5]
        result['uage'] = row[6]
        result['gender'] = row[7]
        result['phone'] = row[8]
        result['address'] = row[9]
        result['created'] = row[10]
        return result


    def __build_attr_dic(self, id, fname, lname, email, uname, pword, uage, gender, phone, address, created):
        result = {}
        result['id'] = id
        result['fname'] = fname
        result['lname'] = lname
        result['email'] = email
        result['uname'] = uname
        result['pword'] = pword
        result['uage'] = uage
        result['gender'] = gender
        result['phone'] = phone
        result['address'] = address
        result['created'] = created
        return result


    def get(self):
        try:
            dao = user.UserDAO()
            usr_list = dao.get()
            result_list = []
            for row in usr_list:
                obj = self.build_map_dic(row)
                result_list.append(obj)
            return jsonify(Users = result_list), macros.OK
        except:
            return jsonify(macros.USR_ERROR), macros.NOT_FOUND


    def get_by_id(self, id):
        try:
            dao = macros.UserDAO()
            query = dao.get_by_id(id)
            result = self.build_map_dic(query)
            return jsonify(User=result), macros.OK
        except:
            return jsonify(macros.USR_DNE), macros.NOT_FOUND
    

    def get_by_uname(self, uname):
        try:
            dao = macros.UserDAO()
            query = dao.get_by_uname(uname)
            result = self.build_map_dic(query)
            return jsonify(User=result), macros.OK
        except:
            return jsonify(macros.USR_DNE), macros.NOT_FOUND


    def get_by_email(self, email):
        try:
            dao = user.UserDAO()
            query = dao.get_by_email(email)
            result = self.build_map_dic(query)
            return jsonify(User=result), macros.OK
        except:
            return jsonify(macros.USR_DNE), macros.NOT_FOUND