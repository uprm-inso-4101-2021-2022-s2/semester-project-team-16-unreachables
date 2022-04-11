from flask import jsonify
from DAOs.employee import EmployeeDAO
from utils.macros import *

class EmployeeController:
    '''
    Help on the Employee Controller Object
    TODO: Document
    '''

    def build_map_dic(self, row):
        result = {}
        result['id'] = row[0]
        result['user_id'] = row[1]
        result['company_id'] = row[2]
        result['reports_resolved'] = row[3]
        result['reports_unresolved'] = row[4]
        result['fname'] = row[5]
        result['lname'] = row[6]
        result['email'] = row[7]
        result['uname'] = row[8]
        result['pword'] = row[9]
        result['uage'] = row[10]
        result['gender'] = row[11]
        result['phone'] = row[12]
        result['address'] = row[13]
        result['created'] = row[14]
        return result


    def __build_attr_dic(self, id, user_id, company_id, r_resolved, r_unresolved):
        result = {}
        result['id'] = id
        result['user_id'] = user_id
        result['company_id'] = company_id
        result['reports_resolved'] = r_resolved
        result['reports_unresolved'] = r_unresolved
        return result


    def get(self):
        try:
            dao = EmployeeDAO()
            query = dao.get()
            result_list = []
            for row in query:
                obj = self.build_map_dic(row)
                result_list.append(obj)
            return jsonify(Employees = result_list), OK
        except:
            return jsonify(EMPLOYEE_ERROR), NOT_FOUND


    def get_by_id(self, id):
        try:
            dao = EmployeeDAO()
            query = dao.get_by_id(id)
            result = self.build_map_dic(query)
            return jsonify(Employee=result), OK
        except:
            return jsonify(EMPLOYEE_DNE), NOT_FOUND
    

    def get_by_uname(self, uname):
        try:
            dao = EmployeeDAO()
            query = dao.get_by_uname(uname)
            result = self.build_map_dic(query)
            return jsonify(Employee=result), OK
        except:
            return jsonify(EMPLOYEE_DNE), NOT_FOUND


    def get_by_email(self, email):
        try:
            dao = EmployeeDAO()
            query = dao.get_by_email(email)
            result = self.build_map_dic(query)
            return jsonify(Employee=result), OK
        except:
            return jsonify(EMPLOYEE_DNE), NOT_FOUND