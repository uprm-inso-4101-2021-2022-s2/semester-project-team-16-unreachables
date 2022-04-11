from flask import jsonify
from DAOs.services import ServiceDAO
from utils.macros import *

class ServiceController:
    '''
    Help on the Service Controller Object
    TODO: Document
    '''

    def build_map_dic(self, row):
        result = {}
        result['id'] = row[0]
        result['service_name'] = row[1]
        result['company_id'] = row[2]
        result['category'] = row[3]
        result['service_description'] = row[4]
        return result


    def build_map_dic_company(self, row):
        result = {}
        result['id'] = row[0]
        result['service_name'] = row[1]
        result['company_id'] = row[2]
        result['category'] = row[3]
        result['service_description'] = row[4]
        result['company_name'] = row[5]
        result['provided_services'] = row[6]
        return result


    def __build_attr_dic(self, id, sname, cid, category, service_desc):
        result = {}
        result['id'] = id
        result['service_name'] = sname
        result['company_id'] = cid
        result['category'] = category
        result['service_description'] = service_desc
        return result


    def get(self):
        try:
            dao = ServiceDAO()
            usr_list = dao.get()
            result_list = []
            for row in usr_list:
                obj = self.build_map_dic(row)
                result_list.append(obj)
            return jsonify(Services = result_list), OK
        except:
            return jsonify(SERVICE_ERROR), NOT_FOUND


    def get_by_id(self, id):
        try:
            dao = ServiceDAO()
            query = dao.get_by_id(id)
            result = self.build_map_dic(query)
            return jsonify(Service=result), OK
        except:
            return jsonify(SERVICE_DNE), NOT_FOUND
    
    
    def get_by_cname(self, cname):
        try:
            dao = ServiceDAO()
            query = dao.get_by_cname(cname)
            result = self.build_map_dic_company(query)
            return jsonify(Service=result), OK
        except:
            return jsonify(COMPANY_DNE), NOT_FOUND


    def get_by_category(self, category):
        try:
            dao = ServiceDAO()
            query = dao.get_by_category(category)
            result = self.build_map_dic(query)
            return jsonify(Service=result), OK
        except:
            return jsonify(SERVICE_DNE), NOT_FOUND