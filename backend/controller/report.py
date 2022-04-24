from flask import jsonify
from DAOs import report
from DAOs import user
from utils import macros


class ReportController:
    '''
    Help on the Report Controller Object
    TODO: Document
    '''

    def build_map_dic(self,row):
        result = {}
        result['id'] = row[0]
        result['title'] = row[1]
        result['report_description'] = row[2]
        result['report_status'] = row[3]
        result['municipality'] = row[4]
        return result


    def __build_attr_dic(self, id, title, description, status, municipalitiy):
        result = {}
        result['id'] = id
        result['title'] = title
        result['report_description'] = description
        result['report_status'] = status
        result['municipality'] = municipalitiy
        return result


    def get(self):
        try:
            dao = report.ReportDAO()
            query = dao.get()
            result_list = []
            for row in query:
                obj = self.build_map_dic(row)
                result_list.append(obj)
            return jsonify(Reports = result_list), macros.OK
        except:
            return jsonify(macros.REPORT_ERROR), macros.NOT_FOUND


    def get_by_id(self, id):
        try:
            dao = report.ReportDAO()
            query = dao.get_by_id(id)
            result = self.build_map_dic(query)
            return jsonify(Report=result), macros.OK
        except:
            return jsonify(macros.REPORT_DNE), macros.NOT_FOUND


    def get_by_mun(self, mun):
        try:
            dao = report.ReportDAO()
            query = dao.get_by_mun(mun)
            result = self.build_map_dic(query)
            return jsonify(Report=result), macros.OK
        except:
            return jsonify(macros.REPORT_DNE), macros.NOT_FOUND