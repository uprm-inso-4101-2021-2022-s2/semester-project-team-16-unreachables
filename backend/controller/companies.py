from flask import jsonify
from DAOs import companies
from utils import macros

class CompanyController:
    '''
    Help on the Company Controller Object
    TODO: Document
    '''

    def build_map_dic(self, row):
        result = {}
        result['id'] = row[0]
        result['company_name'] = row[1]
        result['provided_services'] = row[2]
        return result


    def __build_attr_dic(self, id, cname, p_services):
        result = {}
        result['id'] = id
        result['company_name'] = cname
        result['provided_services'] = p_services
        return result


    def get(self):
        try:
            dao = companies.CompanyDAO()
            usr_list = dao.get()
            result_list = []
            for row in usr_list:
                obj = self.build_map_dic(row)
                result_list.append(obj)
            return jsonify(Companies = result_list), macros.OK
        except:
            return jsonify(macros.COMPANY_ERROR), macros.NOT_FOUND


    def get_by_id(self, id):
        try:
            dao = companies.CompanyDAO()
            query = dao.get_by_id(id)
            result = self.build_map_dic(query)
            return jsonify(Company=result), macros.OK
        except:
            return jsonify(macros.COMPANY_DNE), macros.NOT_FOUND
    

    def get_by_cname(self, cname):
        try:
            dao = companies.CompanyDAO()
            query = dao.get_by_cname(cname)
            result = self.build_map_dic(query)
            return jsonify(Company=result), macros.OK
        except:
            return jsonify(macros.COMPANY_DNE), macros.NOT_FOUND